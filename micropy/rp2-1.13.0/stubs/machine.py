"""
Module: 'machine' on rp2 v1.13
"""
# MCU: (sysname='rp2', nodename='rp2', release='1.13.0', version='v1.13-290-g556ae7914 on 2021-01-21 (GNU 10.2.0 MinSizeRel)', machine='Raspberry Pi Pico with RP2040')
# Stubber: 1.3.2

class ADC:
    ''
    CORE_TEMP = 4
    def read_u16():
        pass


class I2C:
    ''
    def init():
        pass

    def readfrom():
        pass

    def readfrom_into():
        pass

    def readfrom_mem():
        pass

    def readfrom_mem_into():
        pass

    def readinto():
        pass

    def scan():
        pass

    def start():
        pass

    def stop():
        pass

    def write():
        pass

    def writeto():
        pass

    def writeto_mem():
        pass

    def writevto():
        pass


class PWM:
    ''
    def deinit():
        pass

    def duty_ns():
        pass

    def duty_u16():
        pass

    def freq():
        pass

PWRON_RESET = 1

class Pin:
    ''
    ALT = 3
    IN = 0
    IRQ_FALLING = 4
    IRQ_RISING = 8
    OPEN_DRAIN = 2
    OUT = 1
    PULL_DOWN = 2
    PULL_UP = 1
    def high():
        pass

    def init():
        pass

    def irq():
        pass

    def low():
        pass

    def toggle():
        pass

    def value():
        pass


class SPI:
    ''
    LSB = 0
    MSB = 1
    def deinit():
        pass

    def init():
        pass

    def read():
        pass

    def readinto():
        pass

    def write():
        pass

    def write_readinto():
        pass


class SoftI2C:
    ''
    def init():
        pass

    def readfrom():
        pass

    def readfrom_into():
        pass

    def readfrom_mem():
        pass

    def readfrom_mem_into():
        pass

    def readinto():
        pass

    def scan():
        pass

    def start():
        pass

    def stop():
        pass

    def write():
        pass

    def writeto():
        pass

    def writeto_mem():
        pass

    def writevto():
        pass


class SoftSPI:
    ''
    LSB = 0
    MSB = 1
    def deinit():
        pass

    def init():
        pass

    def read():
        pass

    def readinto():
        pass

    def write():
        pass

    def write_readinto():
        pass


class Timer:
    ''
    ONE_SHOT = 0
    PERIODIC = 1
    def deinit():
        pass

    def init():
        pass


class UART:
    ''
    def any():
        pass

    def read():
        pass

    def readinto():
        pass

    def readline():
        pass

    def sendbreak():
        pass

    def write():
        pass


class WDT:
    ''
    def feed():
        pass

WDT_RESET = 3
def bootloader():
    pass

def freq():
    pass

mem16 = None
mem32 = None
mem8 = None
def reset():
    pass

def reset_cause():
    pass

