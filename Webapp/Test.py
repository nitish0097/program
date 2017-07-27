import webapp2
import cgi


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write('''
        <html>
        <head>
            <title>Notes</title>
        </head>
        <body>Hello!
           <form action="/create" method=post>
              <div>
                <input type = "submit" value = "Create Notes" style= "margin-left:540px"> 
              </div>  
           </form>
        </body>
        </html>''')

class Create(webapp2.RequestHandler):
    def post(self):
        self.response.out.write(open('create.html').read())

class Notes(webapp2.RequestHandler):
    def post(self):
        self.response.out.write('<hr>')
        self.response.out.write('<b><i>Name:</i></b>')
        name = self.response.out.write(cgi.escape(self.request.get('Name')))
        self.response.out.write('  <b>Wrote:</b>')
        self.response.out.write('<li>')
        self.response.out.write('<i>Title:</i>')
        title = self.response.out.write(cgi.escape(self.request.get('Title')))
        self.response.out.write('<br>')
        self.response.out.write('<i>Content:</i>')
        content = self.response.out.write(cgi.escape(self.request.get('content')))
        self.response.out.write('</li>')
        self.response.out.write('<hr>')
        self.response.out.write('</body></html>')


app = webapp2.WSGIApplication({
    ('/', MainHandler), ('/submit', Notes),('/create', Create)}, debug=True)
