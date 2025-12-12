import unittest
from math import pi
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from rectangle import area
from rectangle import perimeter

class TestRectangle(unittest.TestCase):
    def test_area_zero(self):
        a=0
        b=0
        self.assertAlmostEqual(area(a,b),0)
    
    def test_area_width_is_zero(self):
        a=56
        b=0
        self.assertAlmostEqual(area(a,b),-1)
    
    def test_area_length_is_zero(self):
        a=0
        b=4646
        self.assertAlmostEqual(area(a,b),-1)

    def test_area_int(self):
        a=5
        b=7
        ans=35

        self.assertAlmostEqual(area(a,b),ans)

    def test_area_float(self):
        a=3.2
        b=5.7
        ans=18.24
        self.assertAlmostEqual(area(a,b),ans)

    def test_area_one(self):
        a=1
        b=1
        ans=1
        self.assertAlmostEqual(area(a,b),ans)
    
    def test_area_large(self):
        a=593853958398539.3343
        b=32435353.32424
        ans=a*b
        self.assertAlmostEqual(area(a,b),ans)
    
    def test_area_small(self):
        a=0.000000001
        b=0.0000001
        ans=0.0000000000000001
        self.assertAlmostEqual(area(a,b),ans)

    def test_area_negative(self):
        a=-6
        b=-8
        self.assertAlmostEqual(area(a,b),-1)

    def test_area_lenght_is_negative(self):
        a=0
        b=-8
        self.assertAlmostEqual(area(a,b),-1)

    def test_area_width_is_negative(self):
        a=-6
        b=0
        self.assertAlmostEqual(area(a,b),-1)

    def test_area_wrong_type(self):
        a1=[1,2,3,4]
        b1=7
        a2=10
        b2="ISRPO"
        self.assertAlmostEqual(area(a1,b1),-1)
        self.assertAlmostEqual(area(a2,b2),-1)

    def test_perimeter_zero(self):
        a=0
        b=0
        self.assertAlmostEqual(perimeter(a,b),0)
    
    def test_perimeter_width_is_zero(self):
        a=56
        b=0
        self.assertAlmostEqual(perimeter(a,b),-1)
    
    def test_perimeter_length_is_zero(self):
        a=0
        b=4646
        self.assertAlmostEqual(perimeter(a,b),-1)
    
    def test_perimeter_int(self):
        a=5
        b=4
        ans=18

        self.assertAlmostEqual(perimeter(a,b),ans)

    def test_perimeter_float(self):
        a=3.4
        b=8.54
        ans=23.88
        self.assertAlmostEqual(perimeter(a,b),ans)

    def test_perimeter_one(self):
        a=1
        b=1
        ans=4
        self.assertAlmostEqual(perimeter(a,b),ans)
    
    def test_perimeter_large(self):
        a=593853958398539.3343
        b=442424242.2424
        ans=2*(a+b)
        self.assertAlmostEqual(perimeter(a,b),ans)
    
    def test_perimeter_small(self):
        a=0.000000001
        b=0.0000004
        ans=0.000000802
        self.assertAlmostEqual(perimeter(a,b),ans)

    def test_perimeter_negative(self):
        a=-6
        b=-8
        self.assertAlmostEqual(perimeter(a,b),-1)

    def test_perimeter_lenght_is_negative(self):
        a=0
        b=-8
        self.assertAlmostEqual(perimeter(a,b),-1)

    def test_perimeter_width_is_negative(self):
        a=-6
        b=0
        self.assertAlmostEqual(perimeter(a,b),-1)

    def test_perimeter_wrong_type(self):
        a1=[1,2,3,4]
        b1=6
        a2="ISRPO"
        b2=87
        self.assertAlmostEqual(perimeter(a1,b1),-1)
        self.assertAlmostEqual(perimeter(a2,b2),-1)
    

    