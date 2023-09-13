from flask import Flask

app = Flask('app')


@app.route('/')
def hello_world():
  return 'Hello, World i mwita!'

app.run(host='0.0.0.0', port=8080)
