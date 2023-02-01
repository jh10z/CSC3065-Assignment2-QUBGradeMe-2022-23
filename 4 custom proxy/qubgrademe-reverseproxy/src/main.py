from flask import Flask,request,redirect,Response
import requests, json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def index():
    return 'Proxy is running'

@app.route("/service/<path>", methods=["GET","POST"])
def proxy(path):
    global SITE_NAME
    with open('./config/proxy-config.json') as json_file:
        data = json.load(json_file)
        SITE_NAME = data[path]
    if request.method=="GET":
        resp = requests.get(f"{SITE_NAME}", params = request.args)
        excluded_headers = ["content-encoding", "content-length", "transfer-encoding", "connection"]
        headers = [(name, value) for (name, value) in  resp.raw.headers.items() if name.lower() not in excluded_headers]
        response = Response(resp.content, resp.status_code, headers)
        return response
    elif request.method=="POST":
        resp = requests.post(f"{SITE_NAME}", json = request.json)
        excluded_headers = ["content-encoding", "content-length", "transfer-encoding", "connection"]
        headers = [(name, value) for (name, value) in resp.raw.headers.items() if name.lower() not in excluded_headers]
        response = Response(resp.content, resp.status_code, headers)
        print(response.get_json())
        return response

@app.route("/admin/save", methods=["GET"])
def save():
    global data
    with open('./config/proxy-config.json', 'r') as json_file:
        data = json.load(json_file)
        for key in request.args:
            data[key] = request.args[key]

    with open('./config/proxy-config.json', 'w') as json_file:
        json.dump(data, json_file)
    return data

@app.route("/admin/delete", methods=["GET"])
def delete():
    global data
    with open('./config/proxy-config.json', 'r') as json_file:
        data = json.load(json_file)
        data.pop(request.args["selected"], None)

    with open('./config/proxy-config.json', 'w') as json_file:
        json.dump(data, json_file)
    return data

@app.route("/monitoring", methods=["GET"])
def monitor():
    global services, data
    with open('./config/proxy-config.json', 'r') as json_file:
        data = json.load(json_file)
        services = {
            "MaxMin": data['MaxMin'],
            "SortModules": data['SortModules'],
            "TotalMarks": data['TotalMarks'],
            "ClassifyGrade": data['ClassifyGrade'],
            "AverageMark": data['AverageMark'],
            "ClassifyModules": data['ClassifyModules']
        }

    if request.method=="GET":
        resp = requests.get(data['Monitoring'], params = services)
        excluded_headers = ["content-encoding", "content-length", "transfer-encoding", "connection"]
        headers = [(name, value) for (name, value) in  resp.raw.headers.items() if name.lower() not in excluded_headers]
        response = Response(resp.content, resp.status_code, headers)
        print(response)
        return response

if __name__ == "__main__":
    app.run(debug = True, port=1300)

    