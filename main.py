#%%
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # serve the index.html file
    return render_template('index.html')

@app.route('/video')
def video():
    print("vid req")
    return 'Video Page'

if __name__ == '__main__':
    context = ('server.cert', 'server.key')
    app.run(host='0.0.0.0', port=5000, ssl_context=context)


#%%

import time

for i in range(100):
    
