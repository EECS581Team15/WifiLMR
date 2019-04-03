#!/bin/sh

start()
{
	modprobe brcmfmac
}

case "$1" in
start)
    start
    ;;
esac
