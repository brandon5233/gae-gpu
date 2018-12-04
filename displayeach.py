import webapp2
import jinja2
import os
from google.appengine.api import users
from google.appengine.ext import ndb
from gpu_features import Features

JINJA_ENVIRONMENT = jinja2.Environment(
loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
extensions=['jinja2.ext.autoescape'],
autoescape=True
)

class DisplayEach(webapp2.RequestHandler):
    def post(self):
        self.response.headers['Content-Type'] = 'text/html'
        name = self.request.get('name')
        gpu_key = ndb.Key('Features',name)
        gpu = gpu_key.get()
        logout = users.create_logout_url('/')
        featurelist = ['geometryShader','tesselationShader','shaderInt16', 'sparseBinding', 'textureCompressionETC2', 'vertexPipelineStoresAndAtomics']

        template_values = {
            'gpu' : gpu,
            'logout' : logout,
            'featurelist' : featurelist
            }


        template = JINJA_ENVIRONMENT.get_template('displayeach.html')
        self.response.write(template.render(template_values))

