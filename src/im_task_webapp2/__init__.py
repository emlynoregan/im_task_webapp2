from im_task import _launch_task, get_taskroute
import webapp2
from google.appengine.ext import webapp

def get_webapp_url():
    return "%s/(.*)" % get_taskroute()

class TaskHandler(webapp.RequestHandler):
    def post(self, name):
        _launch_task(self.request.body, name, self.request.headers)

class TaskHandler2(webapp2.RequestHandler):
    def post(self, name):
        _launch_task(self.request.body, name, self.request.headers)

def addrouteforwebapp(routes):
    routes.append((get_webapp_url(), TaskHandler))

def addrouteforwebapp2(routes):
    routes.append((get_webapp_url(), TaskHandler2))
