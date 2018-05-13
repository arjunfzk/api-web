from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('my-form.html')

@app.route('/', methods=['POST'])
def my_form_post():
    import requests
    import json
    text = request.form['text']
    text2 = request.form['text2']
    
    x="https://api.lyrics.ovh/v1/"
    x=x+text+'/'+text2
    r=requests.get(x)
    json_data=r.json()
    z =(json_data['lyrics'])
    z=str(z)
    return z
if __name__ == '__main__':
    app.run(debug=True,port=5010)