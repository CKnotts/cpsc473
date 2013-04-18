import logging
import template
import webapp2

from google.appengine.ext import db

FILE_LIST = db.Key.from_path('FILE', 'LIST')


class File(db.Model):
    name = db.StringProperty()
    mime_type = db.StringProperty()
    content = db.BlobProperty()
    uploaded_at = db.DateTimeProperty(auto_now_add=True)
    tags = db.StringListProperty()


class ListFilesHandler(webapp2.RequestHandler):

    def get(self):
        files = File.all().ancestor(FILE_LIST).order('-uploaded_at')

        tag = self.request.GET.get('tag')
        if tag:
            files = files.filter('tags =', tag)

        file_list = template.variable()
        for f in files:
            print >>file_list, '<tr>'
            print >>file_list, '<td><a href="/download/%s">%s</a></td>' \
                            % (f.name, f.name)
            print >>file_list, '<td>'
            for tag in f.tags:
                print >>file_list, '<a href="/list?tag=%s">%s</a>' \
                                % (tag, tag)
            print >>file_list, '</td>'
            print >>file_list, '</tr>'

        html = template.render(
            'list.html',
            {'file_list': file_list},
            escaped=False
        )
        self.response.write(html)


class UploadFileHandler(webapp2.RequestHandler):

    def post(self):
        uploaded_file = self.request.POST['uploaded_file']
        tags = self.request.POST['tags']

        try:
            saved_file = File(parent=FILE_LIST)

            saved_file.name = uploaded_file.filename
            saved_file.mime_type = uploaded_file.type
            saved_file.content = uploaded_file.file.read()

            if tags:
                saved_file.tags = [tag.strip() for tag in tags.split(',')]

            saved_file.put()
        except AttributeError:
            self.abort(400)

        self.redirect('/list')


class DownloadFileHandler(webapp2.RequestHandler):

    def get(self, filename):
        result = File.all().ancestor(FILE_LIST).\
                            filter('name =', filename).get()
        if not result:
            self.abort(404)

        self.response.headers['Content-Type'] = str(result.mime_type)
        self.response.write(result.content)

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

app = webapp2.WSGIApplication([
    ('/', ListFilesHandler),
    ('/list', ListFilesHandler),
    ('/upload', UploadFileHandler),
    ('/download/(.*)', DownloadFileHandler)
], debug=True)
