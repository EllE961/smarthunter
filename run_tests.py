#!/usr/bin/env python3
"""
Test runner for smarthunter
"""
import unittest
import sys

if __name__ == "__main__":
    suite = unittest.defaultTestLoader.discover('tests')
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    sys.exit(0 if result.wasSuccessful() else 1) 