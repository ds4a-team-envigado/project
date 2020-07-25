from flask import Flask, request, jsonify           # microframework to facilitate coding
from sqlalchemy import create_engine
import json
from pidar_api.location import GeolocatorAdapter
from pidar_api.location.municipality import serialize
from pidar_api.model.pidar_model import PidarModel
from pidar_api.model.pre_evaluation_form import PreEvaluationForm

app = Flask(__name__)           # creating app
geolocator = GeolocatorAdapter()    


@app.route('/getmunicipality', methods=['GET'])
def get_municipality():
    latitude = request.args.get('latitude', 0)
    longitude = request.args.get('longitude', 0)
    municipality = geolocator.get_municipality(latitude, longitude)
    return serialize(municipality), 200


@app.route('/municipalities', methods=['GET'])
def get_municipalities():
    db_string = "postgresql://adr_user:1234@ds4a-demo-instance.cct4rseci702.eu-west-1.rds.amazonaws.com/adr_db"
    db = create_engine(db_string)
    result_set = db.connect().execute("SELECT DISTINCT departamento as code, municipio as name, departamento  as department FROM eva_cultivos")
    json_mun = json.dumps([dict(r) for r in result_set])
    return json_mun, 200



@app.route('/evaluate', methods=['POST'])
def evaluate():
    department = request.args.get('department', 0)
    data = request.form
    form = PreEvaluationForm()
    pidar_model = PidarModel()
    evaluation_response = pidar_model.evaluate(form)
    return serialize(evaluation_response), 201





if __name__ == '__main__':
    app.run(debug=True)
