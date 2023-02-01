from flask import Flask, request, jsonify, Response
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'dpport',
    'host': '143.117.100.232',
    'port': 32760
}
db = MongoEngine()
db.init_app(app)

class Profile(db.Document):
    profile_name = db.StringField()
    name_1 = db.StringField()
    name_2 = db.StringField()
    name_3 = db.StringField()
    name_4 = db.StringField()
    name_5 = db.StringField()
    mark_1 = db.StringField()
    mark_2 = db.StringField()
    mark_3 = db.StringField()
    mark_4 = db.StringField()
    mark_5 = db.StringField()
    def to_json(self):
        return {"profile_name": self.profile_name,
                "name_1": self.name_1, "name_2": self.name_2, "name_3": self.name_3, "name_4": self.name_4, "name_5": self.name_5,
                "mark_1": self.mark_1, "mark_2": self.mark_2, "mark_3": self.mark_3, "mark_4": self.mark_4, "mark_5": self.mark_5}

@app.route('/', methods=['GET'])
def query_records():
    name = request.args.get('profile_name')
    user = Profile.objects(profile_name=name).first()
    if not user:
        return Response(response = "Profile does not exist: Please save values first to load." , status = 400)
    else:
        return jsonify(user.to_json())

@app.route('/', methods=['POST'])
def update_record():
    record = request.get_json()
    user = Profile.objects(profile_name=record['profile_name']).first()
    if not user:
        user = Profile(profile_name=record['profile_name'],
                name_1=record['name_1'], name_2=record['name_2'], name_3=record['name_3'], name_4=record['name_4'], name_5=record['name_5'],
                mark_1=record['mark_1'], mark_2=record['mark_2'], mark_3=record['mark_3'], mark_4=record['mark_4'], mark_5=record['mark_5']) 
        user.save()
        return jsonify(user.to_json())
    else:
        user.update(name_1=record['name_1'], name_2=record['name_2'], name_3=record['name_3'], name_4=record['name_4'], name_5=record['name_5'],
                mark_1=record['mark_1'], mark_2=record['mark_2'], mark_3=record['mark_3'], mark_4=record['mark_4'], mark_5=record['mark_5']) 
    user = Profile.objects(profile_name=record['profile_name']).first()
    return jsonify(user.to_json())

if __name__ == "__main__":
    app.run(debug=True, port=1337)