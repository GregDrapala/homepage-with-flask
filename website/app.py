from flask import Flask, render_template
app = Flask(__name__)
# czy powinienem tu dodac @app.route('/') czy zmienic /me na / ?
@app.route('/me')
def me():
    return render_template('me.html')

@app.route('/contact', methods=['POST','GET'])
def contact():
    return render_template('contact.html')    

# czy to wszystko o co chodzilo w tym zadaniu?