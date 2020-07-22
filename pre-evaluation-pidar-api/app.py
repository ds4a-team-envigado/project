from flask import Flask, request, jsonify           # microframework to facilitate coding

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
    return "", 200



@app.route('/evaluate', methods=['POST'])
def evaluate():
    form = PreEvaluationForm()
    pidar_model = PidarModel()
    evaluation_response = pidar_model.evaluate(form)
    return serialize(evaluation_response), 201





if __name__ == '__main__':
    app.run(debug=True)
