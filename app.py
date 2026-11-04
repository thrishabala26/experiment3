from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>My Flask App</title>
        <style>
            body {
                font-family: Arial;
                text-align: center;
                margin-top: 100px;
                background-color: #f2f2f2;
            }
            h1 {
                color: #007bff;
            }
        </style>
    </head>
    <body>
        <h1>Welcome to Flask!</h1>
        <p>Your Python Flask application is running successfully.</p>
    </body>
    </html>
    """

@app.route("/about")
def about():
    return "<h1>About Page</h1><p>This is my Flask application.</p>"

if __name__ == "__main__":
    app.run(debug=True)