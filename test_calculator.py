#!/usr/bin/env python3
"""
Unit tests for Differential Setup Calculator formulas.
"""

import unittest

class TestDifferentialFormulas(unittest.TestCase):
    def test_pre_existing_setup_todds_numbers(self):
        # Todd's numbers from the transcript:
        f_race = 0.473
        od_race = 3.310
        f_pinion = 4.941
        m_target = 2.809  # Suppose target checking distance is 2.809 (meaning we need to adjust)
        
        # 1. Axle Centerline
        axle_centerline = f_race + (od_race / 2.0)
        self.assertAlmostEqual(axle_centerline, 2.128, places=4)
        
        # 2. Current Checking Distance
        checking_dist = f_pinion - axle_centerline
        self.assertAlmostEqual(checking_dist, 2.813, places=4)
        
        # 3. Shim difference
        shim_diff = checking_dist - m_target
        self.assertAlmostEqual(shim_diff, 0.004, places=4) # Need to add 0.004 of shims
        
    def test_manufacturing_setup_todds_numbers(self):
        f_race = 0.473
        od_race = 3.310
        cd_target = 2.813
        t_head = 1.911
        m_target = 4.720 # Target mounting distance
        
        # 1. Axle Centerline
        axle_centerline = f_race + (od_race / 2.0)
        self.assertAlmostEqual(axle_centerline, 2.128, places=4)
        
        # 2. Target Pinion Face to Diff Face
        f_pinion_target = cd_target + axle_centerline
        self.assertAlmostEqual(f_pinion_target, 4.941, places=4)
        
        # 3. Current Mounting Distance
        current_mounting_dist = cd_target + t_head
        self.assertAlmostEqual(current_mounting_dist, 4.724, places=4)
        
        # 4. Shim difference
        shim_diff = current_mounting_dist - m_target
        self.assertAlmostEqual(shim_diff, 0.004, places=4) # Need to add 0.004 of shims

    def test_carrier_shims(self):
        w_housing = 8.000
        w_carrier = 7.950
        p_desired = 0.008
        
        total_shims = (w_housing - w_carrier) + p_desired
        self.assertAlmostEqual(total_shims, 0.058, places=4)

if __name__ == "__main__":
    unittest.main()
