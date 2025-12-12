import unittest
from math import pi
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from triangle import area
from triangle import perimeter

class TestTriangle(unittest.TestCase):
    def test_area_zero(self):
        a=0
        h=0
        self.assertAlmostEqual(area(a,h),0)
    
    def test_area_height_is_zero(self):
        a=5
        h=0
        self.assertAlmostEqual(area(a,h),-1)

    def test_area_side_is_zero(self):
        a=0
        h=5
        self.assertAlmostEqual(area(a,h),-1)

    
    def test_area_int(self):
        a=5
        h=10
        self.assertAlmostEqual(area(a,h),25)

    def test_area_float(self):
        a=3.56
        h=5.343
        ans=a*h/2
        self.assertAlmostEqual(area(a,h),ans)

    
    def test_area_large(self):
        a=593853958398539.3343
        h=343435353.7676
        ans=a*h/2
        self.assertAlmostEqual(area(a,h),ans)
    
    def test_area_small(self):
        a=0.000000001
        h=0.00000000001
        ans=a*h/2
        self.assertAlmostEqual(area(a,h),ans)

    def test_area_negative(self):
        a1=-1
        h1=-3
        a2=-4
        h2=6
        a3=5
        h3=-5

        self.assertAlmostEqual(area(a1,h1),-1)
        self.assertAlmostEqual(area(a2,h2),-1)
        self.assertAlmostEqual(area(a3,h3),-1)


    def test_area_wrong_type(self):
        a1=[1,2,3,4]
        h1=4
        a2=7
        h2="ISRPO"
        self.assertAlmostEqual(area(a1,h1),-1)
        self.assertAlmostEqual(area(a2,h2),-1)


    def test_perimeter_zero(self):
        a=0
        b=0
        c=0
        self.assertAlmostEqual(perimeter(a,b,c),0)
    
    def test_perimeter_one_zero(self):
        a1=0
        b1=4
        c1=6
        self.assertAlmostEqual(perimeter(a1,b1,c1),-1)
        a2=6
        b2=0
        c2=6
        self.assertAlmostEqual(perimeter(a2,b2,c2),-1)
        a3=9
        b3=4
        c3=0
        self.assertAlmostEqual(perimeter(a3,b3,c3),-1)

    def test_perimeter_int(self):
        a=3
        b=4
        c=5
        ans=12

        self.assertAlmostEqual(perimeter(a,b,c),ans)

    def test_perimeter_float(self):
        a=4.5
        b=8.7
        c=7.9
        ans=21.1
        self.assertAlmostEqual(perimeter(a,b,c),ans)

    def test_perimeter_one(self):
        a=1
        b=1
        c=1
        
        self.assertAlmostEqual(perimeter(a,b,c),3)
    
    def test_perimeter_large(self):
        a=593853958398539.3343
        b=343435454.5453
        c=3546353.353535
        self.assertAlmostEqual(perimeter(a,b,c),a+b+c)
    
    def test_perimeter_small(self):
        a=0.000000001
        b=0.0001
        c=0.00000001
        ans=a+b+c
        self.assertAlmostEqual(perimeter(a,b,c),ans)

    def test_perimeter_negative(self):
        a1=-2
        b1=4
        c1=6
        self.assertAlmostEqual(perimeter(a1,b1,c1),-1)
        a2=6
        b2=-1
        c2=6
        self.assertAlmostEqual(perimeter(a2,b2,c2),-1)
        a3=9
        b3=4
        c3=-8
        self.assertAlmostEqual(perimeter(a3,b3,c3),-1)

    def test_perimeter_wrong_type(self):
        a=[1,2,3,4]
        b="ISRPO"
        c="aboba"
        self.assertAlmostEqual(perimeter(a,b,c),-1)
    

    