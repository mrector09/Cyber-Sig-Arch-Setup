
from flask import Flask, render_template, request, redirect, url_for, session
import os

app = Flask(__name__)
app.secret_key = 'super_secret_key'

# User credentials for secure login
USERNAME = "M"
PASSWORD = "root"

@app.route("/")
def login():
    return '''
    <html>
    <head><title>Lexarv6 Dashboard - Login</title></head>
    <body>
        <h2>Lexarv6 Secure Login</h2>
        <form action="/dashboard" method="post">
            Username: <input type="text" name="username"><br>
            Password: <input type="password" name="password"><br>
            <input type="submit" value="Login">
        </form>
    </body>
    </html>
    '''

@app.route("/dashboard", methods=["POST"])
def dashboard():
    username = request.form["username"]
    password = request.form["password"]
    if username == USERNAME and password == PASSWORD:
        session["logged_in"] = True
        return redirect(url_for("main_dashboard"))
    else:
        return "Login Failed. Please try again."

@app.route("/main")
def main_dashboard():
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    return '''
    <html>
    <head>
        <title>Lexarv6 Dashboard</title>
        <style>
            body { font-family: Arial; background-color: #0f0f17; color: #00ffcc; text-align: center; }
            .tab { display: none; }
            .tab.active { display: block; }
            button { margin: 5px; padding: 10px; background-color: #00ffcc; border: none; cursor: pointer; }
        </style>
        <script>
            function showTab(tabName) {
                document.querySelectorAll('.tab').forEach(el => el.classList.remove('active'));
                document.getElementById(tabName).classList.add('active');
            }
        </script>
    </head>
    <body>
        <h1>Lexarv6 Web Dashboard</h1>
        <div>
            <button onclick="showTab('system')">System Management</button>
            <button onclick="showTab('security')">Security Management</button>
            <button onclick="showTab('tools')">Advanced Tools</button>
            <button onclick="showTab('programming')">Advanced Programming</button>
            <button onclick="showTab('dashboard')">Web Dashboard Control</button>
        </div>

        <div class="tab active" id="system">
            <h2>System Management</h2>
            <p><a href="/custom_os">Build Custom OS</a></p>
            <p><a href="/optimize_system">System Optimization</a></p>
            <p><a href="/ssh_management">Secure Remote Management (SSH)</a></p>
        </div>

        <div class="tab" id="security">
            <h2>Security Management</h2>
            <p><a href="/vpn">Secure VPN Control</a></p>
            <p><a href="/proxy_hopping">Proxy Hopping (Anonymity)</a></p>
            <p><a href="/firewall">Firewall Configuration</a></p>
            <p><a href="/intrusion_detection">Intrusion Detection</a></p>
        </div>

        <div class="tab" id="tools">
            <h2>Advanced Tools</h2>
            <p><a href="/error_fix">Smart Error Detection and Auto-Fix</a></p>
            <p><a href="/pentesting">Advanced Pentesting Suite</a></p>
            <p><a href="/file_encryption">Secure File Encryption/Decryption</a></p>
            <p><a href="/snapshots">System Snapshot Management</a></p>
        </div>

        <div class="tab" id="programming">
            <h2>Advanced Programming</h2>
            <p><a href="/secure_code">Secure Code Execution (Sandboxed)</a></p>
            <p><a href="/code_debugger">AI Code Debugger</a></p>
            <p><a href="/code_optimization">Code Auto-Completion and Optimization</a></p>
        </div>

        <div class="tab" id="dashboard">
            <h2>Web Dashboard Control</h2>
            <p><a href="/launch_dashboard">Launch Web Dashboard</a></p>
            <p><a href="/customize_dashboard">Customize Dashboard Layout</a></p>
            <p><a href="/system_monitor">System Monitor</a></p>
            <p><a href="/security_control">Security Control Panel</a></p>
        </div>
    </body>
    </html>
    '''

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
