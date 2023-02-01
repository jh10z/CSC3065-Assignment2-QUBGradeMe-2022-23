from flask import Flask, jsonify, request, Response
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['POST'])
def total_marks():
    json_dict = request.get_json()
    total = 0; r = ""
    if(json_dict['mark_1'] == "" and json_dict['mark_2'] == "" and json_dict['mark_3'] == "" and json_dict['mark_4'] == "" and json_dict['mark_5'] == ""):
        return Response(response = "Error: To use functionality, please enter at least one mark.", status = 400)
    
    totalmarks = getTotalMarks(json_dict)
    total = totalmarks["total"]
    response = totalmarks["response"]
    status = totalmarks["status"]

    if(status == 400):
        return Response(response = response, status = 400)

    return jsonify({"total_marks": total})

def getTotalMarks(json_dict):
    total = 0
    response = ""
    status = 200
    for key in json_dict:
        try:
            if (json_dict[key] == ""): #allow empty strings from front end
                json_dict[key] = 0.0    
            else: #otherwise convert to float (throws exception if cant) 
                json_dict[key] = float(json_dict[key])

            if (json_dict[key] < 0 or json_dict[key] > 100): #input validation, number must be between 0 and 100
                response += "Module " + key[5] + " input is not within 0 and 100. \n"
                status = 400
                
        except ValueError: 
            response += "Module " + key[5] + " value is not a number. \n"
            status = 400

        else:
            total += json_dict[key]
    return {"total": total, "response": response, "status": status}

if __name__ == '__main__':
    app.run(debug=True, port=5000)

