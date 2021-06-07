from django.test import TestCase
from django.test import Client

from ...gaelo_processing.controller import tensorflow_controller


class test_unit_tf_controller(TestCase):

    def test_unit_tf_ctrllr(self):
        results = {'right_arm': [0.9999998807907104, 8.830931363945638e-08],
                   'head': [0.9998007416725159, 0.0001992526522371918],
                   'leg': [3.3905369178910405e-08, 5.459643830363348e-07, 0.9999994039535522],
                   'left_arm': [3.89083290031067e-08, 1.0]}
        tf = tensorflow_controller.prediction(
            "2.16.840.1.113669.632.20.870421.10000713812_mip_ct", 'aquisition_field_model')
        print(tf)
        # self.assertTrue(tf!= None)
        print('test_unit_tf_controller validate')
