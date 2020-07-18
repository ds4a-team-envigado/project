import unittest
from pidar_api.location.municipality import Municipality
from pidar_api.location.geolocator_adapter import GeolocatorAdapter




class TestGeolocatorAdapter(unittest.TestCase):
    def test_get_municipality_code(self):
        geo = GeolocatorAdapter()
        plato_code =  geo.get_municipality_code()
        self.assertAlmostEqual("001", plato_code)

"""
    def test_get_municipality(self):
        geo = GeolocatorAdapter()
        plato =  geo.get_municipality("9.7923756", "-74.7951948")
        envigado = geo.get_municipality("6.1746593", "-75.5777786")
        self.assertAlmostEqual("Plato", plato.name)
        self.assertAlmostEqual("Envigado", envigado.name)
        
        """