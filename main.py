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
#
# # html boilerplate for the top of every page
# page_header = """
# <!DOCTYPE html>
# <html>
# <head>
#     <title>Caesar</title>
# </head>
# <body>
#     <h1>Caesar</h1>
# """
#
# # html boilerplate for the bottom of every page
# page_footer = """
# </body>
# </html>
# """


import webapp2
import caesar
import cgi

def build_page(textarea_content):
    rot_label = "<label>Rotate by: </label>"
    rot_number = "<input name ='rot' type='number'/>'"

    message_label = "<label>Type a message: </label>"
    textarea = "<textarea  name='message'>" + textarea_content + "</textarea>"

    submit= "<input type='submit'/>"
    form = ("<form method='post'>" +
            rot_label + rot_number + "<br>" +
            message_label + textarea + "<br>"+
            submit + "</form>")

    header = "<h2>Web Caeser</h2>"
    return header + form


class MainHandler(webapp2.RequestHandler):
    """ Handles requests coming in to '/' (the root of our site)
        e.g. www.web-caesar.com/"""

    def get(self):
        content = build_page("")
        self.response.write(content)

    def post(self):
        message = self.request.get("message")
        rot = int(self.request.get("rot"))
        encrypted_message = caesar.encrypt(message, rot)
        escaped_message = cgi.escape(encrypted_message)
        content = build_page(escaped_message)
        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', MainHandler),


], debug=True)
