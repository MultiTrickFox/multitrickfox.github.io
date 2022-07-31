from flask import Flask, request, render_template, jsonify
from flask_cors import CORS

#

certificate_file = ''
key_file         = ''

#

app = Flask(__name__, template_folder='', static_folder='/static' if certificate_file else '')
CORS(app)

#


@app.route('/')
def home(): return render_template('index.html')


#
                                                                                       # change to 80
if __name__ == '__main__': app.run(host='0.0.0.0', port=64242 if certificate_file else 64242, ssl_context=(certificate_file, key_file) if certificate_file else None)
