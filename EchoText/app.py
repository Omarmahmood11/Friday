from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
from sp_recog import transcribe_audio

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(filename)
        text = transcribe_audio(filename)
        return render_template('index.html', transcription=text)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
