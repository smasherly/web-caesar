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

# html boilerplate for the top of every page
page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>Caesar</title>
</head>
<body>
    <h1>Caesar</h1>
"""

# html boilerplate for the bottom of every page
page_footer = """
</body>
</html>
"""


import webapp2
import caesar

class MainHandler(webapp2.RequestHandler):
    """ Handles requests coming in to '/' (the root of our site)
        e.g. www.web-caesar.com/"""

    def get(self):
        edit_header = "<h3>Encrypt your code here</h3>"

        #add a form for user to enter message and roate number
        add_form = """
        <form action="/encrypt" method='get'>
            <p>
            <label>
                Message to be encrypted:
                <br>
                <textarea name="en_text" rows="10" cols="30">Type message here</textarea>
            </label>
            </p>
            </p>
            <label>
            <br>
                Enter rotation number
                <input type="text" name="rot" />
            </label>
            <p>
            <input type="submit" value="Encrypt"/>
        </form>"""
        message= "Helloooooo world!"
        # encrypted_message = caesar.encrypt(message, 13)
        content = page_header + add_form + page_footer
        self.response.write(content)
    # def post(self):
    #     self.response.write(content)

class Encrypted_Text(webapp2.RequestHandler):
    def post(self):
        message= self.request.get("en_text")
        rot= self.request.get("rot")
        encrypted_message = caesar.encrypt(message, rot)

        new_message = "<h1>Your encrypted message is: " + encrypted_message + "</h1>"

        content = page_header + "<p>" + new_message + "</p>" + page_footer
        self.response.write(content)




app = webapp2.WSGIApplication([
    ('/', MainHandler),
    (/encrypt, Encrypted_Text)

], debug=True)
