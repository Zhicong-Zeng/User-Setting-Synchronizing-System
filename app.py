from flask import Flask , render_template , json , request
import os


app = Flask(__name__)


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
      if(common_setting_data.get("ApplicationC")):
        AppC_data = common_setting_data["ApplicationC"]
      
        file_path = os.path.relpath("Data/CommonSettingData.json")
        with open(file_path, 'r') as targetfile:
          data = json.load(targetfile)
        data["CommonSettingData"]["ApplicationC"] = AppC_data
        with open(file_path, 'w') as targetfile:
          json.dump(data, targetfile)
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
      AllData = json.loads(file.read())
      if(AllData.get("CommonSettingData")):
        CommonData = AllData["CommonSettingData"]
        if(CommonData.get("ApplicationC")):
          AppC_Data = CommonData["ApplicationC"]
          DataList.append(AppC_Data)

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

