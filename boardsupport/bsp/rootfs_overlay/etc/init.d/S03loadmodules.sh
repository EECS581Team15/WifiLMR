#!/bin/sh

start()
{
	modprobe brcmfmac
	modprobe snd_soc_bcm2835_i2s
	modprobe snd-soc-spdif-rx
	modprobe snd-soc-spdif-tx
	modprobe snd-soc-simple-card
}

case "$1" in
start)
    start
    ;;
esac
