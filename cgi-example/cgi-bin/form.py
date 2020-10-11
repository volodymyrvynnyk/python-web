#!/usr/bin/env python3

import cgi
import http.cookies
import os

cookie = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))
try:
    submit_counter = cookie.get("submit_counter").value
    submit_counter = int(submit_counter)
except Exception:
    submit_counter = 0
submit_counter += 1

form = cgi.FieldStorage()
first_name = form.getvalue('first_name', 'Not set')
second_name = form.getvalue('second_name', 'Not set')
native_language = form.getvalue('native_language', 'Not set')
languages_to_learn = form.getvalue('languages', 'Not set')
languages_to_learn = [languages_to_learn] if isinstance(languages_to_learn, str) else languages_to_learn

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Form processing</title>
        </head>
        <body>""")

print("<h1>Form Processed</h1>")
print(f"<p>First name: {first_name}</p>")
print(f"<p>Second name: {second_name}</p>")
print(f"<p>Native language: {native_language}</p>")
print(f"<p>Languages to learn: {','.join(languages_to_learn)}</p>")
print("<a href='http://localhost:8000'>Back to form</p>")
print(f"Times submitted <b>{submit_counter}</b> times by you")
print("""</body>
        </html>""")

print(f"Set-Cookie: submit_counter={submit_counter}")
