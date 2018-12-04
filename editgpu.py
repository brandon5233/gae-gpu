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

class EditGPU(webapp2.RequestHandler):
    def post(self):
        action = self.request.get('button')
        propertylist = ['geometryShader','tesselationShader','shaderInt16', 'sparseBinding', 'textureCompressionETC2', 'vertexPipelineStoresAndAtomics']
        ##user = users.get_current_user()
        logout = users.create_logout_url('/')
        if action=='edit':
            name = self.request.get('name')
            gpu_key = ndb.Key('Features',name)
            gpu = gpu_key.get()
            template_values = {
            'propertylist' : propertylist,
            'gpu': gpu,
            'logout': logout
            }
            template = JINJA_ENVIRONMENT.get_template('editgpu.html')
            self.response.write(template.render(template_values))
            
        if action == 'update':
            
            name = self.request.get('name')
            geometryShader = self.request.get('geometryShader')
            tesselationShader  = self.request.get('tesselationShader')
            shaderInt16 = self.request.get('shaderInt16')
            sparseBinding = self.request.get('sparseBinding')
            textureCompressionETC2  = self.request.get('textureCompressionETC2')
            vertexPipelineStoresAndAtomics = self.request.get('vertexPipelineStoresAndAtomics')

            key = ndb.Key('Features', name)
            gpu = key.get()
                    
            gpu.geometryShader = geometryShader
            gpu.tesselationShader  = tesselationShader
            gpu.shaderInt16 = shaderInt16
            gpu.sparseBinding = sparseBinding
            gpu.textureCompressionETC2  = textureCompressionETC2
            gpu.vertexPipelineStoresAndAtomics = vertexPipelineStoresAndAtomics
            gpu.put()
            self.redirect('/displaygpu')

        if action == 'delete':
            name = self.request.get('name')
            key = ndb.Key('Features', name)
            key.delete()
            self.redirect('/displaygpu')

        if action == 'cancel':
            self.redirect('/displaygpu')

        

        
