import webapp2
import jinja2
from google.appengine.api import users
import os
from displaygpu import DisplayGPU
from gpu_features import Features
from addgpu import AddGPU
from editgpu import EditGPU
from displayeach import DisplayEach
from query import Query

JINJA_ENVIRONMENT = jinja2.Environment(
loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
extensions=['jinja2.ext.autoescape'],
autoescape=True
)

class Login(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'

        url = ''
        url_string = ''
        user = users.get_current_user()

        if user:
            self.redirect('/displaygpu')
        else:
            self.redirect(users.create_login_url(self.request.uri))
            

##        template_values = {
##            'url' : url,
##            'url_string' : url_string,
##            'user' : user
##            }
##
##
##        template = JINJA_ENVIRONMENT.get_template('login.html')
##        self.response.write(template.render(template_values))

app = webapp2.WSGIApplication([
    ('/', Login),
    ('/displaygpu',DisplayGPU),
    ('/features',Features),
    ('/addgpu', AddGPU),
    ('/editgpu',EditGPU),
    ('/displayeach',DisplayEach),
    ('/query' , Query)
    ], debug=True)
