from flask import Flask, render_template, request, make_response
import pickle
import base64

app = Flask(__name__)

# Default theme
DEFAULT_THEME = 'light'

def serialize_theme(theme):
    # Serialize the theme object using pickle and encode it in base64
    theme_bytes = pickle.dumps(theme)
    theme_base64 = base64.b64encode(theme_bytes).decode('utf-8')
    return theme_base64

def deserialize_theme(theme_base64):
    # Decode base64 and deserialize the theme object using pickle
    theme_bytes = base64.b64decode(theme_base64.encode('utf-8'))
    return pickle.loads(theme_bytes)

@app.route('/')
def index():
    # Get the theme preference from the cookie or use the default theme
    theme_base64 = request.cookies.get('theme', serialize_theme(DEFAULT_THEME))
    theme = deserialize_theme(theme_base64)
    return render_template('index.html', theme=theme)

@app.route('/set_theme/<theme>')
def set_theme(theme):
    # Set the theme preference in the cookie
    theme_base64 = serialize_theme(theme)
    response = make_response(render_template('index.html', theme=theme))
    response.set_cookie('theme', theme_base64, max_age=60*60*24*7)  # Cookie expires in 7 days
    return response

if __name__ == '__main__':
    app.run(debug=True)
