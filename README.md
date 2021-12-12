# Alarm class example

This code demonstrates the Test Driven Development (TDD) approach. It uses the `unittest` module.

The class under test is an alarm class. Its methods are:

  * `activate()`: turns on the alarm;
  * `deactivate()`: turns off the alarm;
  * `motionDetected()`: the alarm detects environmental motion through its sensors;
  * `reset()`: used to stop the alarm sound when it is ringing;
  * `isActive(): bool`: predicate indicating if the alarm is turned on;
  * `isRinging(): bool`: predicate indicating if the alarm is ringing.

The test methods check that the alarm responds as expected depending on its current state and the received inputs.

## How to run tests

The following command can be used to run the tests:

```
python -m unittest
```
