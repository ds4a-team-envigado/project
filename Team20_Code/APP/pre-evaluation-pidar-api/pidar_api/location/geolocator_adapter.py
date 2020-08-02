import logging
from geopy.geocoders import Nominatim
from pidar_api.location.municipality import Municipality
from sqlalchemy import create_engine, text

class GeolocatorAdapter():

    def get_municipality_code(self, state):
        print("get_municipality_code", state)
        db_string = "postgresql://adr_user:1234@ds4a-demo-instance.cct4rseci702.eu-west-1.rds.amazonaws.com/adr_db"
        db = create_engine(db_string)

        if not state:
            return ""

        query = 'SELECT nombre_dpto FROM municipios WHERE nombre_dpto = \'{0}\''.format(state.upper())
        print(query)
        result_set = db.connect().execute(query)

        row = result_set.fetchone()
        if(row == None):
            return ""

        code = row[0]

        return code

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
        municipality.code = self.get_municipality_code(state)
        municipality.department = state
        # llamo a la función para sacar el codigo del departamento

        return municipality




 



