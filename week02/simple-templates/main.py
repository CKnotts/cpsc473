import os
import cgi
import string

import webapp2

def template(filename, mapping):
    with open(os.path.join('templates', filename)) as f:
        template = string.Template(f.read())

    escaped = {k: cgi.escape(str(v), quote=True)
                for k, v in mapping.items()}

    return template.substitute(escaped)

class StringTemplateHandler(webapp2.RequestHandler):

    def get(self):
        template = string.Template('Hello from ${class_name}')
        output = template.substitute({'class_name': self.__class__})
        html = cgi.escape(output, quote=True)
        self.response.write(html)

class FileTemplateHandler(webapp2.RequestHandler):

    def get(self):
        self.response.write(
            template('hello.html', {'class_name': self.__class__})
        )

app = webapp2.WSGIApplication([
    ('/templates/string', StringTemplateHandler),
    ('/templates/file', FileTemplateHandler)
], debug=True)

