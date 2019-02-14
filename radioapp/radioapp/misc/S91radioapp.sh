#!/bin/sh
#
# Based on the Buildroot/Busybox logging init script
#

export DISPLAY=:0.0
RADIOAPP=/usr/lib/python3.6/site-packages/radioapp/main.pyc
RADIOAPP_ARGS=""

start() {
	printf "Starting radioapp: "
	start-stop-daemon -S -b -p /var/run/radioapp.pid --exec /usr/bin/python3 -- $RADIOAPP $RADIOAPP_ARGS
	echo "OK"
}

stop() {
	printf "Stopping radioapp: "
	start-stop-daemon -K -q -p /var/run/radioapp.pid
	echo "OK"
}

case "$1" in
  start)
	start
	;;
  stop)
	stop
	;;
  restart|reload)
	stop
	start
	;;
  *)
	echo "Usage: $0 {start|stop|restart|reload}"
	exit 1
esac

exit $?
