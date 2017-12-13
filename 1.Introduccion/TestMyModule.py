#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import myModule


class TestMyModule(unittest.TestCase):

    def test_suma(self):
        print(myModule.sum(5, 7))
        edad = int(input("Dígame su edad: "))
        print("Su edad son", edad, "años")


if __name__ == "__main__":
    unittest.main()
