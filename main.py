#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import os
import logging
import jinja2

# Lets set it up so we know where we stored the template files
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class IndexHandler(webapp2.RequestHandler):
    def get(self):
    	template = JINJA_ENVIRONMENT.get_template('templates/index.html')
    	self.response.write(template.render({'title': 'HOME', 'home1': 'HOME', 'food': 'Food', 'family':'Family', 'login': 'login'}))#print the template


class FamilyHandler(webapp2.RequestHandler):
    def get(self):
    	template = JINJA_ENVIRONMENT.get_template('templates/family.html')
    	self.response.write(template.render({'title': 'FAMILY', 'home1': 'Home', 'food': 'Food', 'family':'FAMILY', 'login': 'login'}))#print the template


class FoodHandler(webapp2.RequestHandler):
    def get(self):
    	template = JINJA_ENVIRONMENT.get_template('templates/food.html')
    	self.response.write(template.render({'title': 'FOOD', 'home1': 'Home', 'food': 'FOOD', 'family':'Family', 'login': 'login'}))#print the template

class LoginHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/login.html')
        self.response.write(template.render({'title': 'LOGIN', 'home1': 'Home', 'food': 'food', 'family':'Family', 'login': 'LOGIN'}))#print the template

    def post(self):
                msg = "Login Fail"
                if (self.request.get('user') == "Colleen" and self.request.get('pw') == "pass"): #factch the username & password from the HTML form
                #becuase python doesn't know user is a vaiable, we have to add '', to enable python to fatch the username
                #sebsequently, we need to define the value from html as vaiable
                #when user became the vairable, we don't need to add ''
                        template = JINJA_ENVIRONMENT.get_template('templates/loggedin.html')
                        self.response.write(template.render({'title': 'LOGIN', 'home1': 'Home', 'food': 'food', 'family':'Family', 'login': 'LOGIN'}))#print the template

                else:
                        user = self.request.get('user') #fatch the password from the HTML form
                        password = self.request.get('pw') #fatch the password from the HTML form
                        template = JINJA_ENVIRONMENT.get_template('templates/login.html')
                        self.response.write(template.render({'result':msg, 'title': 'LOGIN', 'home1': 'Home', 'food': 'food', 'family':'Family', 'login': 'LOGIN'}))
                        #print the template
                        logging.info('username = %s & the password is %s', user,password) #log the username & password
                        #%s= ____
                        #username=_____ & password=_____, user, password                       

app = webapp2.WSGIApplication([
    ('/', IndexHandler),
    ('/index.html', IndexHandler),
    ('/family.html', FamilyHandler),
    ('/food.html', FoodHandler),
    ('/login.html', LoginHandler)
], debug=True)
