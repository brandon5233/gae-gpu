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

class Query(webapp2.RequestHandler):
    def get(self):
        logout = users.create_logout_url('/')
        featurelist = ['geometryShader','tesselationShader','shaderInt16', 'sparseBinding', 'textureCompressionETC2', 'vertexPipelineStoresAndAtomics']
        template_values = {
            'logout' : logout,
            'featurelist' : featurelist,
            'notempty' : "wait"
        }
        template = JINJA_ENVIRONMENT.get_template('query.html')
        self.response.write(template.render(template_values))
        
    def post(self):
        self.response.headers['Content-Type'] = 'text/html'
        featurelist = ['geometryShader','tesselationShader','shaderInt16', 'sparseBinding', 'textureCompressionETC2', 'vertexPipelineStoresAndAtomics']  
        logout = users.create_logout_url('/')
        result =[]

        geometryShader = self.request.get('geometryShader')
        tesselationShader  = self.request.get('tesselationShader')
        shaderInt16 = self.request.get('shaderInt16')
        sparseBinding = self.request.get('sparseBinding')
        textureCompressionETC2  = self.request.get('textureCompressionETC2')
        vertexPipelineStoresAndAtomics = self.request.get('vertexPipelineStoresAndAtomics')
        finalquery=Features.query()

        if geometryShader:
            finalquery = finalquery.filter(Features.geometryShader=="True")
        if tesselationShader:
            finalquery = finalquery.filter(Features.tesselationShader=="True")
        if shaderInt16:
            finalquery = finalquery.filter(Features.shaderInt16=="True")
        if sparseBinding:
            finalquery = finalquery.filter(Features.sparseBinding=="True")
        if textureCompressionETC2:
            finalquery = finalquery.filter(Features.textureCompressionETC2=="True")
        if vertexPipelineStoresAndAtomics:
            finalquery = finalquery.filter(Features.vertexPipelineStoresAndAtomics=="True")
            
        finalquery = finalquery.fetch()
            
       
        
        if finalquery:
            notempty = True
        else:
            notempty = False
            
        template_values = {
            'logout' : logout,
            'featurelist' : featurelist,            
            'relevantgpu' : finalquery,
            'notempty' : notempty
            }


        template = JINJA_ENVIRONMENT.get_template('query.html')
        self.response.write(template.render(template_values))

