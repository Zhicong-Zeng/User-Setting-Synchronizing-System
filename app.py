#from asyncio.windows_events import NULL
from email import message
from webbrowser import get
from flask import Flask , render_template , json , request
import os



app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

print("Hello WOr!")

@app.route("/")
def root():
  return "<p>Hello, User! Please choose your application type!</p>"

DataList = []

@app.route('/ApplicationC',methods = ['POST', 'GET'])
def ApplicationC():
  if request.method == 'POST':
    json_file = request.files['file'].read().decode("utf-8")
    json_obj = json.loads(json_file)
    message = "<p>"
    
    if(json_obj.get("CommonSettingData")):
      common_setting_data = json_obj["CommonSettingData"]
      file_path = os.path.relpath("Data/CommonSettingData.json")
      with open(file_path, 'w') as outfile:
        json.dump(common_setting_data, outfile)
      message += "Succeed change common data"
        
    if(json_obj.get("ApplicationC")):
      application_c = json_obj["ApplicationC"]
      file_path = os.path.relpath("Data/ApplicationC.json")
      with open(file_path, 'w') as outfile:
        json.dump(application_c, outfile)
      message += "Succeed change ApplicationC data"
    
    message += "</p>"
    return message
  
  else:#Get method
    DataList.clear()
    Common_file_path = os.path.relpath("Data/CommonSettingData.json")
    with open(Common_file_path) as file:
      DataList.append(json.load(file))
    AppC_file_path = os.path.relpath("Data/ApplicationC.json")
    with open(AppC_file_path) as file:
      DataList.append(json.load(file))
    return render_template('ApplicationC.html', title="page", jsonfile=json.dumps(DataList))


@app.route('/ApplicationB',methods = ['POST', 'GET'])
def ApplicationB():
  if request.method == 'POST':
    json_file = request.files['file'].read().decode("utf-8")
    json_obj = json.loads(json_file)
    message = "<p>"
    
    if(json_obj.get("CommonSettingData")):
      common_setting_data = json_obj["CommonSettingData"]
      file_path = os.path.relpath("Save_Copy/CommonSettingData.json")
      with open(file_path, 'w') as outfile:
        json.dump(common_setting_data, outfile)
      message += "Succeed change common data"
        
    if(json_obj.get("ApplicationB")):
      application_b = json_obj["ApplicationB"]
      file_path = os.path.relpath("Save_Copy/ApplicationB.json")
      with open(file_path, 'w') as outfile:
        json.dump(application_b, outfile)
      message += "Successfully updated ApplicationB data"
    
    message += "</p>"
    return message
  
  else:#Get method
    DataList.clear()
    Common_file_path = os.path.relpath("Data/CommonSettingData.json")
    with open(Common_file_path) as file:
      DataList.append(json.load(file))
    AppC_file_path = os.path.relpath("Data/ApplicationB.json")
    with open(AppC_file_path) as file:
      DataList.append(json.load(file))
    return render_template('ApplicationB.html', title="page", jsonfile=json.dumps(DataList))





@app.route('/common_get',methods = ['GET'])
def common_get():
  file_path = os.path.relpath("Data/CommonSettingData.json")
  with open(file_path) as file:
    commons = json.load(file)
  return render_template('common.html', title="page", jsonfile=json.dumps(commons))


@app.route('/common_post',methods = ['POST'])
def common_post():
  if request.method == 'POST':
    file = request.files['json'] 
    file_path = os.path.relpath("Data/CommonSettingData.json")
    file.save(file_path)

