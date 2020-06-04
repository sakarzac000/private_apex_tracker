from flask import Flask
from flask import request
import grabStats

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    platform = request.headers.get('platform')
    print(platform)
    name = request.headers.get('name')
    print(name)

    return grabStats.getStats(platform, name)

if __name__ == '__main__':
    app.run(debug=True)