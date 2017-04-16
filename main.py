# Copyright 2016 Google Inc.
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

import os
import jinja2
import webapp2

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template("templates/index.html")
        self.response.out.write(template.render({
            "request": self.request,
        }))

class ContactHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template("templates/contact.html")
        self.response.out.write(template.render({
            "request": self.request,
        }))

class FactsHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template("templates/facts.html")
        self.response.out.write(template.render({
            "request": self.request,
        }))

class FaqHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template("templates/faq.html")
        self.response.out.write(template.render({
            "request": self.request,
        }))

class StorageHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template("templates/storage.html")
        self.response.out.write(template.render({
            "request": self.request,
        }))


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/contact/', ContactHandler),
    ('/facts/', FactsHandler),
    ('/faq/', FaqHandler),
    ('/storage/', StorageHandler),

], debug=True)