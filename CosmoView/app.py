from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    response = requests.get('https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY')
    apod = response.json()
    return render_template('home.html', apod=apod)

if __name__ == '__main__':
    app.run(debug=True)
