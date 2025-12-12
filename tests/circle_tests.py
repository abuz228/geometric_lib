import unittest
from math import pi
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from circle import area
from circle import perimeter

class TestCircle(unittest.TestCase):
    def test_area_zero(self):
        r=0
        self.assertAlmostEqual(area(r),0)
    
    def test_area_int(self):
        r=5
        ans=pi*r*r

        self.assertAlmostEqual(area(r),ans)

    def test_area_float(self):
        r=3.4
        ans=pi*r*r
        self.assertAlmostEqual(area(r),ans)

    def test_area_one(self):
        r=1
        ans=pi
        self.assertAlmostEqual(area(1),ans)
    
    def test_area_large(self):
        r=593853958398539.3343
        ans=pi*r*r
        self.assertAlmostEqual(area(r),ans)
    
    def test_area_small(self):
        r=0.000000001
        ans=pi*r*r
        self.assertAlmostEqual(area(r),ans)

    def test_area_negative(self):
        r=-6
        self.assertAlmostEqual(area(r),-1)

    def test_area_wrong_type(self):
        r1=[1,2,3,4]
        r2="ISRPO"
        self.assertAlmostEqual(area(r1),-1)
        self.assertAlmostEqual(area(r2),-1)

    def test_perimeter_zero(self):
        r=0
        self.assertAlmostEqual(perimeter(r),0)
    
    def test_perimeter_int(self):
        r=5
        ans=pi*r*2

        self.assertAlmostEqual(perimeter(r),ans)

    def test_perimeter_float(self):
        r=3.4
        ans=pi*r*2
        self.assertAlmostEqual(perimeter(r),ans)

    def test_perimeter_one(self):
        r=1
        ans=pi*2
        self.assertAlmostEqual(perimeter(1),ans)
    
    def test_perimeter_large(self):
        r=593853958398539.3343
        ans=pi*r*2
        self.assertAlmostEqual(perimeter(r),ans)
    
    def test_perimeter_small(self):
        r=0.000000001
        ans=pi*r*2
        self.assertAlmostEqual(perimeter(r),ans)

    def test_perimeter_negative(self):
        r=-6
        self.assertAlmostEqual(perimeter(r),-1)

    def test_perimeter_wrong_type(self):
        r1=[1,2,3,4]
        r2="ISRPO"
        self.assertAlmostEqual(perimeter(r1),-1)
        self.assertAlmostEqual(perimeter(r2),-1)
    

    