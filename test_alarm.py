import unittest
from alarm import Alarm

class TestAlarm(unittest.TestCase):
    def setUp(self):
        self.a = Alarm()
    
    def test_an_off_alarm_detecting_motion_does_not_ring(self):
        self.a.motionDetected()
        self.assertFalse(self.a.isRinging())

    def test_an_alarm_just_created_is_off(self):
        self.assertFalse(self.a.isActive())

    def test_an_activated_alarm_is_on(self):
        self.a.activate()
        self.assertTrue(self.a.isActive())

    def test_an_activated_alarm_detecting_motion_does_ring(self):
        self.a.activate()
        self.a.motionDetected()
        self.assertTrue(self.a.isRinging())

    def test_an_activated_alarm_detecting_motion_and_reset_does_not_ring(self):
        self.a.activate()
        self.a.motionDetected()
        self.a.reset()
        self.assertFalse(self.a.isRinging())
    
    def test_an_activated_alarm_detecting_motion_and_reset_does_stay_active(self):
        self.a.activate()
        self.a.motionDetected()
        self.a.reset()
        self.assertTrue(self.a.isActive())

    def test_an_alarm_activated_deactivated_and_detecting_motion_does_not_ring(self):
        self.a.activate()
        self.a.deactivate()
        self.a.motionDetected()
        self.assertFalse(self.a.isRinging())
    
    # more test cases

    def test_alarm_is_not_ringing_after_creation(self):
        self.assertFalse(self.a.isRinging())

    def test_off_alarm_detecting_motion_does_not_ring(self):
        self.a.motionDetected()
        self.assertFalse(self.a.isRinging())

    def test_on_alarm_detecting_motion_does_ring(self):
        self.a.activate()
        self.a.motionDetected()
        self.assertTrue(self.a.isRinging())

    def test_alarm_does_not_ring_after_activation_motion_detection_reset(self):
        self.a.activate()
        self.a.motionDetected()
        self.a.reset()
        self.assertFalse(self.a.isRinging())

    def test_alarm_is_on_after_activation_motion_detection_reset(self):
        self.a.activate()
        self.a.motionDetected()
        self.a.reset()
        self.assertTrue(self.a.isActive())

    def test_alarm_is_off_after_activation_deactivation(self):
        self.a.activate()
        self.a.deactivate()
        self.assertFalse(self.a.isActive())
    
    def test_alarm_is_off_after_activation_motion_detection_deactivation(self):
        self.a.activate()
        self.a.motionDetected()
        self.a.deactivate()
        self.assertFalse(self.a.isActive())

    def test_alarm_does_not_ring_after_activation_motion_detection_deactivation(self):
        self.a.activate()
        self.a.motionDetected()
        self.a.deactivate()
        self.assertFalse(self.a.isRinging())

    def test_alarm_does_ring_after_activation_motion_detection_reset_motion_detection(self):
        self.a.activate()
        self.a.motionDetected()
        self.a.reset()
        self.a.motionDetected()
        self.assertTrue(self.a.isRinging())

    def test_off_alarm_does_not_ring_after_three_motion_detections(self):
        self.a.motionDetected()
        self.a.motionDetected()
        self.a.motionDetected()
        self.assertFalse(self.a.isRinging())

    def test_a_ringing_alarm_deactivated_does_not_ring_anymore_if_it_detects_motion(self):
        self.a.activate()
        self.a.motionDetected()
        self.a.deactivate()
        self.a.motionDetected()
        self.assertFalse(self.a.isRinging())

    def test_an_off_alarm_deactivated_raises_an_error(self):
        self.assertRaises(Exception, self.a.deactivate)

    def test_an_on_alarm_activated_raises_an_error(self):
        self.a.activate()
        self.assertRaises(Exception, self.a.activate)

    def test_a_ringing_alarm_activated_raises_an_error(self):
        self.a.activate()
        self.a.motionDetected()
        self.assertRaises(Exception, self.a.activate)

    def test_an_active_quiet_alarm_raises_an_error_on_reset(self):
        self.a.activate()
        self.assertRaises(Exception, self.a.reset)

    def test_an_inactive_quiet_alarm_raises_an_error_on_reset(self):
        self.assertRaises(Exception, self.a.reset)