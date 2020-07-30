from flask import Flask, request, jsonify           # microframework to facilitate coding
from sqlalchemy import create_engine
import json
from pidar_api.location import GeolocatorAdapter
from pidar_api.location.municipality import serialize
from pidar_api.model.pre_evaluation_form import PreEvaluationForm
from pidar_api.pidar_interactor import evaluate_form

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
    pidar_form = {}
    pidar_form['CP'] = request.form.get('chain', '')
    pidar_form['DEPARTAMENTO'] = request.form.get('department', 'ANTIOQUIA')
    pidar_form['Total beneficiarios'] = request.form.get('beneficiaries', '0')
    pidar_form['tipo_proyecto'] = request.form.get('type', '')

    #form = PreEvaluationForm()
    #pidar_model = PidarModel()
    data = evaluate_form(pidar_form)
    return jsonify(pidar_form), 200





if __name__ == '__main__':
    app.run(debug=True)
