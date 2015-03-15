import os
import numpy as np
import pandas as pd
import unittest

from catchment_tools import get_grid_cells

class CatchmentCutterTest(unittest.TestCase):

    def setUp(self):
        self.test_grid_file = os.path.join(os.path.dirname(__file__), 'data', 'awap_rainfall20150206.asc')

        self.test_boundary_file = os.path.join(os.path.dirname(__file__), 'data', 'hrs_410730_boundary.json')

    def test_cut_grid(self):
        grid_cells = get_grid_cells(self.test_boundary_file, self.test_grid_file)

        self.assertEqual(len(grid_cells), 8)

        expected = np.array([[148.8, -35.6],
                            [148.8, -35.65],
                            [148.8, -35.7],
                            [148.85, -35.6],
                            [148.85, -35.65],
                            [148.85, -35.7],
                            [148.85, -35.75],
                            [148.9, -35.7]]
                            )

        for i in range(len(expected)):
            self.assertAlmostEqual(grid_cells[i][0], expected[i][0], 2)
            self.assertAlmostEqual(grid_cells[i][1], expected[i][1], 2)


