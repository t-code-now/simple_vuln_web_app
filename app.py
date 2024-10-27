# app.py

from flask import Flask, request, render_template_string
import os
import requests


app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Welcome to the Vulnerable Web App</h1><p>Use the specific routes to test vulnerabilities:</p><ul><li>/xss</li><li>/csrf</li><li>/ssrf</li><li>/rce</li></ul>"

# XSS Vulnerability
@app.route('/xss')
def xss():
    user_input = request.args.get('input', '')
    return render_template_string(f"<h1>XSS Vulnerability</h1><p>{user_input}</p>")

# CSRF Vulnerability (No CSRF protection on form)
@app.route('/csrf', methods=['POST'])
def csrf():
    # No CSRF protection here
    data = request.form.get('data', '')
    return f"CSRF Vulnerability - Data received: {data}"

# SSRF Vulnerability
@app.route('/ssrf')
def ssrf():
    url = request.args.get('url')
    if url:
        try:
            response = requests.get(url)  # SSRF here
            return f"SSRF Vulnerability - Fetched URL: {url} - Response: {response.text}"
        except Exception as e:
            return f"Error fetching URL: {e}"
    return "No URL provided"

# RCE Vulnerability
@app.route('/rce')
def rce():
    command = request.args.get('cmd')
    if command:
        output = os.popen(command).read()  # RCE here
        return f"RCE Vulnerability - Command output: {output}"
    return "No command provided"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
