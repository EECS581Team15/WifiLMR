#!/bin/sh

export FRAMEBUFFER=/dev/fb1

start()
{
    # Load required modules
    # Rotation ended up being 270 instead of 90 due a layout error
    modprobe fbtft_device name=adafruit18 rotate=270 gpios=reset:24,dc:7
    modprobe fb_st7735r
}

case "$1" in
start)
    start
    ;;
esac
