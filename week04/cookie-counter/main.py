import webapp2


class MainHandler(webapp2.RequestHandler):
    def get(self):
        count = self.request.cookies.get('count', '0')
        count = int(count) + 1
        self.response.headers.add_header('Set-Cookie', 'count=%d' % count)

        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('%d\n' % count)


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
