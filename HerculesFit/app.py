from flask import Flask, render_template, request
import requests
import random

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        categories_selected = request.form.getlist('category')
        exercises = []
        for category in categories_selected:
            response = requests.get(f'https://wger.de/api/v2/exercise/?category={category}&language=2&status=2')
            exercises.extend(response.json()['results'])
        random.shuffle(exercises)
        return render_template('exercises.html', exercises=exercises[:6])
    else:
        response = requests.get('https://wger.de/api/v2/exercisecategory')
        categories = response.json()['results']
        return render_template('home.html', categories=categories)

@app.route('/exercise/<int:exercise_id>')
def exercise(exercise_id):
    response = requests.get(f'https://wger.de/api/v2/exercise/{exercise_id}')
    exercise = response.json()
    return render_template('exercise.html', exercise=exercise)

if __name__ == '__main__':
    app.run(debug=True)
