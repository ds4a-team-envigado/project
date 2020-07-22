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
            municipality.code = 000
        else:
            db_string = "postgresql://adr_user:1234@ds4a-demo-instance.cct4rseci702.eu-west-1.rds.amazonaws.com/adr_db"
            db = create_engine(db_string)
            # Hago un groupby por el departamento y traigo el promedio del codigo (como siempre es el mismo me trae el codigo real del depto)
            sql = "SELECT AVG(cod_dep), departamento FROM eva_cultivos GROUP BY departamento" 
            result_set = db.connect().execute((text(sql)))
            code = 0
            # Cuando el departamento sea igual al "state" que le di, entonces sacar el código del depto
            for row in result_set:
                if row['departamento'] == state:
                    code = int(row['avg'])
            municipality.code = code

        municipality.department = state
        return municipality

    def get_municipality_code(self, state):
        db_string = "postgresql://adr_user:1234@ds4a-demo-instance.cct4rseci702.eu-west-1.rds.amazonaws.com/adr_db"
        db = create_engine(db_string)
        # Hago un groupby por el departamento y traigo el promedio del codigo (como siempre es el mismo me trae el codigo real del depto)
        sql = "SELECT AVG(cod_dep), departamento FROM eva_cultivos GROUP BY departamento" 
        result_set = db.connect().execute((text(sql)))
        code = 0
        # Cuando el departamento sea igual al "state" que le di, entonces sacar el código del depto
        for row in result_set:
            if row['departamento'] == state:
                code = int(row['avg'])
        return code



 



