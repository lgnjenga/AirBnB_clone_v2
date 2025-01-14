from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
  """Displays Hello HBNB!"""
  return render_template('index.html')

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5000)
