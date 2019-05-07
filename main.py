from flask import Flask
from caesar import rotate_string
from flask import Flask, request
app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{  
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
      <form action="/" method = "POST">
        Rotate By:
        <input type="text" name = "rot" value = '0'><br>
        <textarea name = "text"> {0}</textarea>
        <input type="submit" value="Submit Query">
        </form>
    </body>
</html>
"""

@app.route('/', methods = ['POST'])
def encrypt():
    rot = int(request.form['rot'])
    text = request.form['text']
    secret_message = rotate_string(text, rot)
    return form.format( secret_message )



@app.route('/')
def index():
    return form.format("")

app.run()





