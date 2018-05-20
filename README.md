# im_task_webapp2
This repo adds [WebApp2](https://webapp2.readthedocs.io/en/latest/) support for the [im_task](https://github.com/emlynoregan/im_task) library. If you use webapp2, and you want to use @task, then install this module.

[![Build Status](https://travis-ci.org/emlynoregan/im_task_webapp2.svg?branch=master)](https://travis-ci.org/emlynoregan/im_task_webapp2)
 
## Install

Use the python package for this library. You can find the package online [here](https://pypi.python.org/pypi/im_task_webapp2).

Change to your Python App Engine project's root folder and do the following:

> pip install im_task_webapp2 --target lib

Or add it to your requirements.txt. You'll also need to set up vendoring, see [app engine vendoring instructions here](https://cloud.google.com/appengine/docs/python/tools/using-libraries-python-27).

### Configuring @task

To use @task with webapp2, you need to set up routes in app.yaml, and you need to register the task routes for the webapp2 app. 

Let's say you have a standard app.yaml file, and a single flask app "app" set up in main.py.

In app.yaml, set up the following route:

	handlers:
		- url: /_ah/task/.*
		  script: main.app
		  login: admin

Note "login: admin"; this locks down the interface to tasks to your own code; you don't want external callers to kick of tasks with unknown code.

In main.py, you need to add the @tasks route to the webapp2 routes before constructing the app:

	import webapp2
	from im_task_webapp2 import addrouteforwebapp2

	routes = [ ... some routes ... ]
	
	addrouteforwebapp2(routes) # adds @task route to webapp2 routes
	
	app = webapp2.WSGIApplication(routes)

Once you've got the route set up in app.yaml and registered in main.py, you should be able to use @task. Good luck!	
