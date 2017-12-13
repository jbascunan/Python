#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import myModule


class TestMyModule(unittest.TestCase):

    def test_suma(self):
        print(myModule.sum(5, 7))


if __name__ == "__main__":
    unittest.main()
