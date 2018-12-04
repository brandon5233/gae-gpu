import webapp2
import jinja2
from google.appengine.api import users
import os
from gpu_features import Features

JINJA_ENVIRONMENT = jinja2.Environment(
loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
extensions=['jinja2.ext.autoescape'],
autoescape=True
)

class DisplayGPU(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        allgpu = Features.query().order(Features.key)
        logout = users.create_logout_url('/')
       

        template_values = {
            'allgpu' : allgpu,
            'logout' : logout,
            'idsort' : 'asc'
            }

        template = JINJA_ENVIRONMENT.get_template('displaygpu.html')
        self.response.write(template.render(template_values))

    def post(self):
        self.response.headers['Content-Type'] = 'text/html'
        
        logout = users.create_logout_url('/')
        idsort = self.request.get('idsortorder')
        if idsort == "asc":
            allgpu = Features.query().order(-Features.key)
            idsort = "desc"
        else:
            idsort = "asc"
            allgpu = Features.query().order(Features.key)

        
        template_values = {
            'allgpu' : allgpu,
            'logout' : logout,
            'idsort' : idsort 
            }


        template = JINJA_ENVIRONMENT.get_template('displaygpu.html')
        self.response.write(template.render(template_values))

