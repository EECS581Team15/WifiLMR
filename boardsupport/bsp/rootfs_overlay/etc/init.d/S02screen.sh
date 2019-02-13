#!/bin/sh

start()
{
    # Load required modules
    modprobe spi-bcm2835
    modprobe fbtft_device name=adafruit18_green
    modprobe fb_st7735r
    # Load splash screen
    fbv -d 1 /boot/splash.bmp
}

case "$1" in
start)
    start
    ;;
esac
