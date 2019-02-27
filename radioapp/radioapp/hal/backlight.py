"""
radioapp.hal.backlight
======================
"""
import logging
import os

PWM_PREFIX = "/sys/class/pwm/pwmchip0/"
PERIOD = 1000000 # 1000Hz as nanoseconds

class Backlight:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.duty_cycle = None
        self.saved_level = 100.0
        try:
            os.stat(PWM_PREFIX) # Throws an exception if path does not exist
        except FileNotFoundError:
            self.logger.error("PWM not found")
        else:
            self.logger.debug("PWM found")
            try:
                os.stat(PWM_PREFIX+"pwm0") # check if pwm0 is already exported
            except FileNotFoundError:
                with open(PWM_PREFIX+"export", 'w') as export:
                    export.write('0')
            with open(PWM_PREFIX+"pwm0/period", 'w') as period:
                period.write(str(PERIOD))
            with open(PWM_PREFIX+"pwm0/enable", 'w') as enable:
                enable.write('1')
            self.duty_cycle = open(PWM_PREFIX+"pwm0/duty_cycle", 'w')
    def set_level(self, percentage):
        """
        Sets the backlight to a percentage [0-100]
        """
        if not (0 <= percentage <= 100):
            self.logger.error("Attempting to set backlight to illegal value %s", percentage)
            return
        self.saved_level = float(percentage)
        self.__set_level(self.saved_level)
    def on(self):
        """
        Sets the backlight to last set level
        """
        self.__set_level(self.saved_level)
    def off(self):
        """
        Turns the backlight off
        """
        self.__set_level(0.0)
    def __set_level(self, percentage):
        if self.duty_cycle is None:
            self.logger.info("Cannot set backlight to %s (device not available)", percentage)
            return
        duty = int((percentage/100.0) * PERIOD)
        self.duty_cycle.write(str(duty))
        self.duty_cycle.seek(0, 0)
