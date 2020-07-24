import logging
from geopy.geocoders import Nominatim
from pidar_api.location.municipality import Municipality
from sqlalchemy import create_engine, text

class GeolocatorAdapter():

    def get_municipality(self, latitude, longitude):
        geolocator = Nominatim(user_agent="ds4a")
        lat_long = "{0}, {1}".format(latitude, longitude)
        logging.info(lat_long)
        location = geolocator.reverse(lat_long)
        address = geolocator.geocode(location, addressdetails=True)

        state = ""
        county = ""

        for key in address.raw['address']:
            if key == 'state':
                state = address.raw['address'][key]

            elif key == 'county':
                county = address.raw['address'][key]

        municipality = Municipality()
        municipality.name = county
        # llamo a la función para sacar el codigo del departamento
        if state == "" and county == "":
            municipality.code = 0
        else:
            db_string = "postgresql://adr_user:1234@ds4a-demo-instance.cct4rseci702.eu-west-1.rds.amazonaws.com/adr_db"
            db = create_engine(db_string)
            result_set = db.connect().execute("SELECT DISTINCT cod_mun, municipio, departamento FROM eva_cultivos WHERE municipio=%s AND departamento = %s", (county, state))
            municipality.code = result_set.fetchone()[0]

        municipality.department = state
        return municipality

    def get_municipality_code(self, state, county):
        db_string = "postgresql://adr_user:1234@ds4a-demo-instance.cct4rseci702.eu-west-1.rds.amazonaws.com/adr_db"
        db = create_engine(db_string)
        result_set = db.connect().execute("SELECT DISTINCT cod_mun, municipio, departamento FROM eva_cultivos WHERE municipio=%s AND departamento = %s", (county, state))
        code = result_set.fetchone()[0]
        return code


 



