from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    print(json.dumps(dict(request.args), indent=2, ensure_ascii=False))
    print(str(request.data))
    return str(dict(request.args))

if __name__ == '__main__':
    app.run()
