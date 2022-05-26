from flask import Flask , render_template , json , request
import os


app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route("/")
def root():
  return "<p>Hello, World!</p>"


@app.route('/common_get',methods = ['GET'])
def common_get():
  file_path = os.path.relpath("Data\CommonSettingData.json")
  with open(file_path) as file:
    commons = json.load(file)
  return render_template('common.html', title="page", jsonfile=json.dumps(commons))


@app.route('/common_post',methods = ['POST'])
def common_post():
  if request.method == 'POST':
    file = request.files['json'] 
    file_path = os.path.relpath("Data\CommonSettingData.json")
    file.save(file_path)