# -*- coding: utf-8 -*-

import unittest
from pub_product import *
if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Test_pub_product))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)


