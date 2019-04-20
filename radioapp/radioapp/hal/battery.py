"""
Interfaces to the MCP3421 ADC that measures the battery voltage. Corrects for
the voltage divider in front of the ADC and estimates battery life as a
percentage based on a generic Li-ion discharge curve
"""
import random


class Battery:
    R1_OHMS = 1000000
    R2_OHMS = 100000
    HIGH_VOLTAGE = 4.2
    LOW_VOLTAGE = 3.0

    def __init__(self):
        pass

    def read_adc(self):
        """
        Returns the voltage read by the ADC
        """
        return ((random.random() * (self.HIGH_VOLTAGE - self.LOW_VOLTAGE) + self.LOW_VOLTAGE) * self.R2_OHMS) / (self.R1_OHMS + self.R2_OHMS)

    def scale_divider(self, sample):
        print("sample", sample)
        return (sample * (self.R1_OHMS + self.R2_OHMS)) / self.R2_OHMS

    def map_to_charge_percent(self, voltage):
        """
        Simply assumes discharge is linear (which is mostly true)
        """
        print("v", voltage)
        return (voltage - self.LOW_VOLTAGE) / (self.HIGH_VOLTAGE - self.LOW_VOLTAGE)

    def poll(self):
        try:
            sample = self.read_adc()
            voltage = self.scale_divider(sample)
            percent = self.map_to_charge_percent(voltage)
            return percent
        except (FileNotFoundError, PermissionError):
            return 1.0