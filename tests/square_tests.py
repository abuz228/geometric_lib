import unittest
from math import pi
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from square import area
from square import perimeter

class TestSquare(unittest.TestCase):
    def test_area_zero(self):
        a=0
        self.assertAlmostEqual(area(a),0)
    
    def test_area_int(self):
        a=5
        ans=25

        self.assertAlmostEqual(area(a),ans)

    def test_area_float(self):
        a=3.2
        ans=10.24
        self.assertAlmostEqual(area(a),ans)

    def test_area_one(self):
        a=1
        ans=1
        self.assertAlmostEqual(area(1),ans)
    
    def test_area_large(self):
        a=593853958398539.3343
        ans=a*a
        self.assertAlmostEqual(area(a),ans)
    
    def test_area_small(self):
        a=0.000000001
        ans=0.000000000000000001
        self.assertAlmostEqual(area(a),ans)

    def test_area_negative(self):
        a=-6
        self.assertAlmostEqual(area(a),-1)

    def test_area_wrong_type(self):
        a1=[1,2,3,4]
        a2="ISRPO"
        self.assertAlmostEqual(area(a1),-1)
        self.assertAlmostEqual(area(a2),-1)

    def test_perimeter_zero(self):
        a=0
        self.assertAlmostEqual(perimeter(a),0)
    
    def test_perimeter_int(self):
        a=5
        ans=20

        self.assertAlmostEqual(perimeter(a),ans)

    def test_perimeter_float(self):
        a=3.4
        ans=13.6
        self.assertAlmostEqual(perimeter(a),ans)

    def test_perimeter_one(self):
        a=1
        ans=4
        self.assertAlmostEqual(perimeter(1),ans)
    
    def test_perimeter_large(self):
        a=593853958398539.3343
        ans=a*4
        self.assertAlmostEqual(perimeter(a),ans)
    
    def test_perimeter_small(self):
        a=0.000000001
        ans=0.000000004
        self.assertAlmostEqual(perimeter(a),ans)

    def test_perimeter_negative(self):
        a=-6
        self.assertAlmostEqual(perimeter(a),-1)

    def test_perimeter_wrong_type(self):
        a1=[1,2,3,4]
        a2="ISRPO"
        self.assertAlmostEqual(perimeter(a1),-1)
        self.assertAlmostEqual(perimeter(a2),-1)
    

    