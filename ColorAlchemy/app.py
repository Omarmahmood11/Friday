import sys
sys.path.insert(1, './DeOldify')
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from deoldify.visualize import *
import warnings
from PIL import Image

warnings.filterwarnings("ignore", category=UserWarning, message=".*?Your .*? set is empty.*?")

app = Flask(__name__)

@app.route('/')
def upload_file():
    return render_template('upload.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_image_file():
   if request.method == 'POST':
      img = request.files['image']
      img_path = "static/" + secure_filename(img.filename)
      img.save(img_path)
      colorized_img_path = colorize(img_path, 35)
      colorized_img_filename = colorized_img_path.split('/')[-1]
      return redirect(url_for('show_colorized_image', filename=secure_filename(img.filename)))


def colorize(img_path, render_factor):
    colorized_img_path = colorizer.plot_transformed_image(path=img_path, render_factor=render_factor, compare=True)
    img = Image.open(colorized_img_path)  # open the image at the returned path
    new_img_path = "static/colorized_" + img_path.split('/')[-1]
    img.save(new_img_path)
    return new_img_path

@app.route('/show/<filename>')
def show_colorized_image(filename):
    return render_template('show.html', filename=filename)

if __name__ == '__main__':
   colorizer = get_image_colorizer(artistic=True)
   app.run(debug = True)
