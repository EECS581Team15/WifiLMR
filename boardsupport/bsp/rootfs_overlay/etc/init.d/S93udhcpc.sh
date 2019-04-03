#!/bin/sh

start()
{
	start-stop-daemon -S -b -x udhcpc -- -f -i wlan0
}

case "$1" in
start)
    start
    ;;
esac
