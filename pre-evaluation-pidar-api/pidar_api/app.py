from flask import Flask, request, jsonify
from geolocator_adapter import GeolocatorAdapter
from municipality import serialize
from pre_evaluation_form import PreEvaluationForm
from pidar_model import PidarModel

app = Flask(__name__)
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
