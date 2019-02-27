#!/bin/sh

export FRAMEBUFFER=/dev/fb1

start()
{
    # Load required modules
    modprobe fbtft_device name=adafruit18 rotate=90
    modprobe fb_st7735r
    # Load splash screen
    fbv -d 1 /boot/splash.bmp &
}

case "$1" in
start)
    start
    ;;
esac
