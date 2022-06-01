from flask import Flask , render_template , json , request
import os
import json


app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route("/")
def root():
    return render_template('Home.html', title="page")

DataList = []


@app.route('/ApplicationA',methods = ['POST', 'GET'])
def ApplicationA():
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
        

    file_path = os.path.relpath("Save_Copy/ApplicationA.json")
    with open(file_path, 'w') as outfile:
      json.dump(json_obj, outfile)
    message += "Successfully updated ApplicationA data"
    
    message += "</p>"
    readAppIntoAppToCommonMapping("ApplicationA")
    DataList.clear()
    AppA_file_path = os.path.relpath("Save_Copy/ApplicationA.json")
    with open(AppA_file_path) as file:
      DataList.append(json.load(file))
    return render_template('ApplicationA.html', title="page", jsonfile=json.dumps(DataList))
  
  else:#Get method
    DataList.clear()
    AppA_file_path = os.path.relpath("Save_Copy/ApplicationA.json")
    with open(AppA_file_path) as file:
      DataList.append(json.load(file))
    return render_template('ApplicationA.html', title="page", jsonfile=json.dumps(DataList))


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
        

    file_path = os.path.relpath("Save_Copy/ApplicationB.json")
    with open(file_path, 'w') as outfile:
      json.dump(json_obj, outfile)
    message += "Successfully updated ApplicationB data"
    
    message += "</p>"
    readAppIntoAppToCommonMapping("ApplicationB")
    DataList.clear()
    AppA_file_path = os.path.relpath("Save_Copy/ApplicationB.json")
    with open(AppA_file_path) as file:
      DataList.append(json.load(file))
    return render_template('ApplicationB.html', title="page", jsonfile=json.dumps(DataList))
  
  else:#Get method
    DataList.clear()
    AppB_file_path = os.path.relpath("Save_Copy/ApplicationB.json")
    with open(AppB_file_path) as file:
      DataList.append(json.load(file))
    return render_template('ApplicationB.html', title="page", jsonfile=json.dumps(DataList))


@app.route('/ApplicationC',methods = ['POST', 'GET'])
def ApplicationC():
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
        
    file_path = os.path.relpath("Save_Copy/ApplicationC.json")
    with open(file_path, 'w') as outfile:
      json.dump(json_obj, outfile)
    message += "Successfully updated ApplicationC data"
    
    message += "</p>"
    readAppIntoAppToCommonMapping("ApplicationC")
    DataList.clear()
    AppA_file_path = os.path.relpath("Save_Copy/ApplicationC.json")
    with open(AppA_file_path) as file:
      DataList.append(json.load(file))
    return render_template('ApplicationC.html', title="page", jsonfile=json.dumps(DataList))
  
  else:#Get method
    DataList.clear()
    AppC_file_path = os.path.relpath("Save_Copy/ApplicationC.json")
    with open(AppC_file_path) as file:
      DataList.append(json.load(file))
    return render_template('ApplicationC.html', title="page", jsonfile=json.dumps(DataList))

@app.route('/Common',methods = ['GET'])
def Common():
  if request.method == 'GET':
    DataList.clear()
    Common_file = os.path.relpath("Save_Copy/CommonSettingData.json")
    with open(Common_file) as file:
      DataList.append(json.load(file))
    return render_template('Common.html', title="page", jsonfile=json.dumps(DataList))


def readAppIntoAppToCommonMapping(ApplcationName):
    appTocommon_dict = readAppTocommonMappingIntoDict()
    metadata_dict = readJsonIntoMetadataMapping()
    file_path = os.path.relpath("Data/" + ApplcationName + ".json")
    with open(file_path) as file:
        app_dict = json.loads(file.read())
    for key in app_dict:
        if (key in appTocommon_dict[ApplcationName]):
            value = app_dict[key]
            result = metadata_dict[appTocommon_dict[ApplcationName][key]]
            if(ApplcationName == "ApplicationA"):
              updateApps("Save_Copy/ApplicationB.json", result[1], value)
              updateApps("Save_Copy/ApplicationC.json", result[2], value)
              updateApps("Save_Copy/CommonSettingData.json", appTocommon_dict[ApplcationName][key], value)
            elif(ApplcationName == "ApplicationB"):
              updateApps("Save_Copy/ApplicationA.json", result[0], value)
              updateApps("Save_Copy/ApplicationC.json", result[2], value)
              updateApps("Save_Copy/CommonSettingData.json", appTocommon_dict[ApplcationName][key], value)
            elif(ApplcationName == "ApplicationC"):
              updateApps("Save_Copy/ApplicationA.json", result[0], value)
              updateApps("Save_Copy/ApplicationB.json", result[1], value)
              updateApps("Save_Copy/CommonSettingData.json", appTocommon_dict[ApplcationName][key], value)
    print("Successfully changed the data")


def readJsonIntoMetadataMapping():
    file_path = os.path.relpath("Data/CommonMetadataMapping.json")
    with open(file_path) as file:
        metadata_dict = json.loads(file.read())
    return metadata_dict
    

def readAppTocommonMappingIntoDict():
    file_path = os.path.relpath("Data/AppToCommonMapping.json")
    with open(file_path) as file:
        appTocommon_dict = json.loads(file.read())
    return appTocommon_dict


def updateApps(appPath, sourceKey, sourceValue):
    file_path = os.path.relpath(appPath)
    with open(file_path) as file:
        application_dict = json.loads(file.read())
    for key in application_dict:
        if(sourceKey == key):
            application_dict[key] = sourceValue
    with open(appPath, 'w') as outfile:
        json.dump(application_dict, outfile)

