import os
import webapp2
import jinja2
from google.appengine.ext import ndb
from google.appengine.api import users
from google.appengine.ext.ndb import metadata
from gpu_features import Features

JINJA_ENVIRONMENT = jinja2.Environment(
loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
extensions=['jinja2.ext.autoescape'],
autoescape=True
)


class AddGPU(webapp2.RequestHandler):

    def get(self):
        featurelist = ['geometryShader','tesselationShader','shaderInt16', 'sparseBinding', 'textureCompressionETC2', 'vertexPipelineStoresAndAtomics']
        logout = users.create_logout_url('/')
        template_values = {
            'logout' : logout,
            'error' : '',
            'featurelist' : featurelist
            }
        template = JINJA_ENVIRONMENT.get_template('addgpu.html')
        self.response.write(template.render(template_values))

    def post(self):
        action = self.request.get('button')
        allgpu = Features.query().fetch()

        if action == 'add':
            name = self.request.get('name')
            geometryShader = self.request.get('geometryShader')
            tesselationShader  = self.request.get('tesselationShader')
            shaderInt16 = self.request.get('shaderInt16')
            sparseBinding = self.request.get('sparseBinding')
            textureCompressionETC2  = self.request.get('textureCompressionETC2')
            vertexPipelineStoresAndAtomics = self.request.get('vertexPipelineStoresAndAtomics')
            
            key = ndb.Key('Features', name)
            gpu = key.get()

            if gpu==None:
                gpu = Features(id=name)
                gpu.geometryShader = geometryShader
                gpu.tesselationShader  = tesselationShader
                gpu.shaderInt16 = shaderInt16
                gpu.sparseBinding = sparseBinding
                gpu.textureCompressionETC2  = textureCompressionETC2
                gpu.vertexPipelineStoresAndAtomics = vertexPipelineStoresAndAtomics
                gpu.put()
                self.redirect('/displaygpu')

            else:
                featurelist = ['geometryShader','tesselationShader','shaderInt16', 'sparseBinding', 'textureCompressionETC2', 'vertexPipelineStoresAndAtomics']
                logout = users.create_logout_url('/')
                template_values = {
                'logout' : logout,
                'error' : 'Sorry, a GPU with that name exists..... Please use a unique name',
                'featurelist' : featurelist
                }
                template = JINJA_ENVIRONMENT.get_template('addgpu.html')
                self.response.write(template.render(template_values))

        if action == 'cancel':
            self.redirect('/displaygpu')

        

        
