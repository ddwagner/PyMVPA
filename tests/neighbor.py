#emacs: -*- mode: python-mode; py-indent-offset: 4; indent-tabs-mode: nil -*-
#ex: set sts=4 ts=4 sw=4 noet:
### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ##
#
#    Copyright (C) 2007 by
#    Michael Hanke <michael.hanke@gmail.com>
#
#    This package is free software; you can redistribute it and/or
#    modify it under the terms of the MIT License.
#
#    This package is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the COPYING
#    file that comes with this package for more details.
#
### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ##
"""Unit tests for PyMVPA finders"""

from mvpa.neighbor import *
import unittest
import numpy as N

class NeighborFinderTests(unittest.TestCase):

    def testDistances(self):
        a = N.array([3,8])
        b = N.array([6,4])
        # test distances or yarik recalls unit testing ;)
        self.failUnless( cartesianDistance(a, b) == 5.0 )
        self.failUnless( manhattenDistance(a, b) == 7 )
        self.failUnless( absminDistance(a, b) == 4 )


    def testDescreteNeighborFinder(self):
        # who said that we will not use FSL's data
        # with negative dimensions? :-)
        elsize = [-2.5, 1.5]
        distance = 3

        # use default function
        finder = DescreteNeighborFinder(elsize)

        # simple check
        target = N.array([ [1,2], [2,1], [2,2], [2,3], [3,2] ])
        self.failUnless( (finder.getNeighbors([2,2], 2.6) == target).all())

        # a bit longer one... not sure what for
        for point in finder([2,2], distance):
            self.failUnless( cartesianDistance(point, [2,2]) <= distance)

        # use manhattenDistance function
        finder = DescreteNeighborFinder(elsize, manhattenDistance)
        for point in finder([2,2], distance):
            self.failUnless( manhattenDistance(point, [2,2]) <= distance)

    def testGetNeighbors(self):
        """Test if generator getNeighbor and method getNeighbors
        return the right thing"""

        class B(NeighborFinder):
            """ Class which overrides only getNeighbor
            """
            def getNeighbor(self):
                for n in [4,5,6]: yield n

        class C(NeighborFinder):
            """ Class which overrides only getNeighbor
            """
            def getNeighbors(self):
                return [1,2,3]

        b = B()
        self.failUnless(b.getNeighbors() == [4,5,6])
        c = C()
        self.failUnless([ x for x in c.getNeighbor()] == [1,2,3])


def suite():
    return unittest.makeSuite(NeighborFinderTests)


if __name__ == '__main__':
    unittest.main()

