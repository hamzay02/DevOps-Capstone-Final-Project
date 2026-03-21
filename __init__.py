from flask import Flask
from flask_talisman import Talisman

# Create Flask app
app = Flask(__name__)

# Define Content Security Policy (CSP)
csp = {
    'default-src': '\'self\'',
    'script-src': '\'self\'',
    'style-src': '\'self\'',
    'img-src': '\'self\' data:',
    'font-src': '\'self\'',
    'connect-src': '\'self\'',
}

# Apply Talisman security headers
Talisman(app, content_security_policy=csp)

# Example route (optional, can remove if already in your app)
@app.route('/')
def home():
    return "Hello, Flask with Talisman is running!"
