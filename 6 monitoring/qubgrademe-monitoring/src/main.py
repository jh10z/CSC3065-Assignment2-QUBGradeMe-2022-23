from flask import Flask,request,redirect,Response
import requests, json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def CheckServiceStatus():
    status = ""
    status += CheckMaxMinService(request.args)
    status += CheckSortModulesService(request.args)
    status += CheckTotalMarkService(request.args)
    status += CheckClassifyGradeService(request.args)
    status += CheckAverageMarkService(request.args)
    status += CheckClassifyModulesService(request.args)
    return status

def CheckMaxMinService(services):
    mockModules = {
        "module_1": "Test1",
        "module_2": "Test2",
        "module_3": "Test3",
        "mark_1": "10",
        "mark_2": "50",
        "mark_3": "70"
    }

    try:
        # Max Min Status Test
        resp = requests.get(services["MaxMin"], params=mockModules)
        resp_json = resp.json()
        if(resp.status_code == 400):
            return "MaxMin Service is Offline. \n"
        elif(resp_json["max_module"] == "Test3 - 70" and resp_json["min_module"] == "Test1 - 10"):
            return "MaxMin Service is Online (" + str(int(resp.elapsed.total_seconds() * 1000)) +"ms) \n"
        else:
            return "MaxMin Service is not working properly (No Correctness in Result)."
    except requests.exceptions.RequestException:
        return "MaxMin Service is Offline. \n"

def CheckSortModulesService(services):
    mockModules = {
        "module_1": "Test1",
        "module_2": "Test2",
        "module_3": "Test3",
        "mark_1": "10",
        "mark_2": "50",
        "mark_3": "70"
    }
    
    try:
        # Sort Modules Status Test
        resp = requests.get(services["SortModules"], params=mockModules)
        resp_json = resp.json()
        if(resp.status_code == 400):
            return "SortModules Service is Offline. \n"
        elif(resp_json["sorted_modules"] == {'module': 'Test3', 'marks': '70'}, {'module': 'Test2', 'marks': '50'}, {'module': 'Test1', 'marks': '10'}):
            return "SortModules Service is Online (" + str(int(resp.elapsed.total_seconds() * 1000)) +"ms) \n"
        else:
            return "SortModules Service is not working properly (No Correctness in Result)."
    except requests.exceptions.RequestException:
        return "SortModules Service is Offline. \n"

def CheckTotalMarkService(services):
    mockModules = {
        "mark_1": "10",
        "mark_2": "50",
        "mark_3": "70"
    }
    
    try:
        # Total Marks Status Test
        resp = requests.post(services["TotalMarks"], json=mockModules)
        resp_json = resp.json()

        if(resp.status_code == 400):
            return "TotalMarks Service is Offline. \n"
        elif(resp_json["total_marks"] == 130):
            return "TotalMarks Service is Online (" + str(int(resp.elapsed.total_seconds() * 1000)) +"ms) \n"
        else:
            return "TotalMarks Service is not working properly (No Correctness in Result)."
    except requests.exceptions.RequestException:
        return "TotalMarks Service is Offline. \n"

def CheckClassifyGradeService(services):
    mockModules = {
        "Module1": "60",
        "Module2": "50",
        "Module3": "70"
    }
    
    try:
        # Classify Grade Status Test
        resp = requests.post(services["ClassifyGrade"], json=mockModules)
        resp_json = resp.json()

        if(resp.status_code == 400):
            return "ClassifyGrade Service is Offline. \n"
        elif(resp_json["classification"] == "Provisional: Commendation"):
            return "ClassifyGrade Service is Online (" + str(int(resp.elapsed.total_seconds() * 1000)) +"ms) \n"
        else:
            return "ClassifyGrade Service Correctness Result Failed."
    except requests.exceptions.RequestException:
        return "ClassifyGrade Service is Offline. \n"

def CheckAverageMarkService(services):
    mockModules = {
        "Module1": "60",
        "Module2": "50",
        "Module3": "70"
    }
    
    try:
        # Average Mark Status Test
        resp = requests.post(services["AverageMark"], json=mockModules)
        resp_json = resp.json()
        
        if(resp.status_code == 400):
            return "AverageMark Service is Offline. \n"
        elif(resp_json["average"] == 60):
            return "AverageMark Service is Online (" + str(int(resp.elapsed.total_seconds() * 1000)) +"ms) \n"
        else:
            return "AverageMark Service Correctness Result Failed."
    except requests.exceptions.RequestException:
        return "AverageMark Service is Offline. \n"

def CheckClassifyModulesService(services):
    mockModules = {
        "m1_grade": "60",
    }
    
    try:
        # Average Mark Status Test
        resp = requests.post(services["ClassifyModules"], json=mockModules)
        resp_json = resp.json()
        print(resp_json)
        if(resp.status_code == 400):
            return "ClassifyModules Service is Offline. \n"
        elif(resp_json["m1_grade"] == "2:1"):
            return "ClassifyModules Service is Online (" + str(int(resp.elapsed.total_seconds() * 1000)) +"ms) \n"
        else:
            return "ClassifyModules Service Correctness Result Failed."
    except requests.exceptions.RequestException:
        return "ClassifyModules Service is Offline. \n"

if __name__ == "__main__":
    app.run(debug = True,port=1360)
    
