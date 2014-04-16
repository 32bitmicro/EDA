# -*- coding: utf-8 -*-
#
# Copyright (c) 2014, Paweł Wodnicki
# All rights reserved.

'''
Created on Apr 15, 2014

@author: Pawel Paweł Wodnicki
'''

import unittest
from eda import *

class Test_Point(unittest.TestCase):
    def setUp(self):
        print
        print("test Point - start")
    def tearDown(self):
        print("test Point - done")
    def test_Point(self):
        point = Point();
        # test initialization
        self.assertTrue(point._x == 0);
        self.assertTrue(point._y == 0);
        self.assertTrue(point.layernum == 0);
        point = Point(1,2,3);
        self.assertTrue(point._x == 1);
        self.assertTrue(point._y == 2);
        self.assertTrue(point.layernum == 3);
        # test scale
        point.scale(2);
        self.assertTrue(point._x == 2);
        self.assertTrue(point._y == 4);
        self.assertTrue(point.layernum == 3);
        # test offset
        point.offset(2,-2);
        self.assertTrue(point._x == 4);
        self.assertTrue(point._y == 2);
        self.assertTrue(point.layernum == 3);
        # test scale 0
        point.scale(0);
        self.assertTrue(point._x == 0);
        self.assertTrue(point._y == 0);
        self.assertTrue(point.layernum == 3);
        #print str(point)
        self.assertTrue(str(point) == "0.000 0.000");


class Test_Rectangle(unittest.TestCase):
    def setUp(self):
        print
        print("test Rectangle - start")
    def tearDown(self):
        print("test Rectangle - done")
    def test_Rectangle(self):
        rect = Rectangle();
        # test initialization
        self.assertTrue(rect.ll._x == 0);
        self.assertTrue(rect.ll._y == 0);
        self.assertTrue(rect.ur._x == 0);
        self.assertTrue(rect.ur._y == 0);
        self.assertTrue(rect.layernum == 0);
        rect = Rectangle(1,2,3,4,5);
        self.assertTrue(rect.ll._x == 1);
        self.assertTrue(rect.ll._y == 2);
        self.assertTrue(rect.ur._x == 3);
        self.assertTrue(rect.ur._y == 4);
        self.assertTrue(rect.layernum == 5);
        # test scale
        rect.scale(2);
        self.assertTrue(rect.ll._x == 2);
        self.assertTrue(rect.ll._y == 4);
        self.assertTrue(rect.layernum == 5);
        # test offset
        rect.offset(2,-2);
        self.assertTrue(rect.ll._x == 4);
        self.assertTrue(rect.ll._y == 2);
        self.assertTrue(rect.layernum == 5);
        # test scale 0
        rect.scale(0);
        self.assertTrue(rect.ll._x == 0);
        self.assertTrue(rect.ll._y == 0);
        self.assertTrue(rect.layernum == 5);
        #print str(rect)
        self.assertTrue(str(rect) == "0.000 0.000 , 0.000 0.000");

    def test_Rectangle_normalize(self):
        rect = Rectangle(1,2,3,4,5);
        self.assertTrue(rect.ll._x == 1);
        self.assertTrue(rect.ll._y == 2);
        self.assertTrue(rect.ur._x == 3);
        self.assertTrue(rect.ur._y == 4);
        rect.normalize()
        self.assertTrue(rect.ll._x == 1);
        self.assertTrue(rect.ll._y == 2);
        self.assertTrue(rect.ur._x == 3);
        self.assertTrue(rect.ur._y == 4);
        rect = Rectangle(3,4,1,2,5);
        rect.normalize()
        self.assertTrue(rect.ll._x == 1);
        self.assertTrue(rect.ll._y == 2);
        self.assertTrue(rect.ur._x == 3);
        self.assertTrue(rect.ur._y == 4);
        
    def test_Rectangle_size(self):
        rect = Rectangle(1,2,3,4,5);
        self.assertTrue(rect.sizeX() == 2);
        self.assertTrue(rect.sizeY() == 2);        
        rect.normalize()
        self.assertTrue(rect.sizeX() == 2);
        self.assertTrue(rect.sizeY() == 2);  
        rect = Rectangle(3,4,1,2,5);
        rect.normalize()
        self.assertTrue(rect.sizeX() == 2);
        self.assertTrue(rect.sizeY() == 2);  
        
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()