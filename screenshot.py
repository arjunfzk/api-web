
from flask import Flask, request, render_template,send_from_directory

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('my-form.html')

@app.route('/', methods=['POST'])
def my_form_post():
    import requests
    import json
    #z=input()
    
    text = request.form['text']
    text2 = request.form['text2']
    #x='http://api.screenshotlayer.com/api/capture?access_key=aa1626836d09ccf550107705e5ae6c35&url=http://google.com'#&viewport=1440x900&fullpage=1
    text='http://api.screenshotlayer.com/api/capture?access_key=aa1626836d09ccf550107705e5ae6c35&url='+text
    r = requests.get(text, allow_redirects=True)
    open(text2+'.jpg', 'wb').write(r.content)
    return send_from_directory('C:\\Users\\HP\\Desktop\\api web',text2+'.jpg')

    
if __name__ == '__main__':
    app.run(debug=True,port=5005)