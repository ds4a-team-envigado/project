import unittest
from pidar_api.location.municipality import Municipality
from pidar_api.location.geolocator_adapter import GeolocatorAdapter




class TestGeolocatorAdapter(unittest.TestCase):


    def test_get_municipality(self):
        geo = GeolocatorAdapter()
        envigado = geo.get_municipality("6.1746593", "-75.5777786")
        self.assertAlmostEqual("Envigado", envigado.name)
        

    def test_without_location(self):
        geo = GeolocatorAdapter()
        without_location =  geo.get_municipality("0", "0")
        self.assertAlmostEqual("", without_location.name)


    def test_get_department(self):
        geo = GeolocatorAdapter()
        magdalena =  geo.get_municipality("9.7923756", "-74.7951948")
        self.assertAlmostEqual("MAGDALENA", magdalena.code) 

    def test_get_new_york(self):
        geo = GeolocatorAdapter()
        new_york =  geo.get_municipality("40.7046976", "-74.0627982")
        self.assertAlmostEqual("", new_york.code)              