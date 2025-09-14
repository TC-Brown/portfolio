import os
from flask import Flask, render_template

# Get the absolute path to the directory containing this file
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Create a Flask application instance with explicit template and static folder paths
app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, 'templates'),
    static_folder=os.path.join(BASE_DIR, 'static')
)

# Route for the home pager
@app.route('/')
def home():
    return render_template('index.html')

# Additional routes for other pages can be added here



# Context processor to make 'static' available in templates
@app.context_processor
def inject_static():
    return dict(static_url='/static/')

if __name__ == '__main__':
    # 'debug=True' reloads the server automatically on code changes
    import sys
    port = 5000
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            print(f"Invalid port argument: {sys.argv[1]}, using default port 5000.")
    app.run(debug=True, host='0.0.0.0', port=port)
