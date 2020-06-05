from flask import Flask, jsonify
from flask import request
from flask_cors import CORS
import grabStats

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def hello_world():
    platform = request.headers.get('platform')
    print(platform)
    name = request.headers.get('name')
    print(name)

    return jsonify(grabStats.getStats(platform, name))

if __name__ == '__main__':
    app.run(debug=True)