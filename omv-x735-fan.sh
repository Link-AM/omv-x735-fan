#! /bin/sh

case "$1" in
  start)
    echo "Starting omv-x735-fan.py"
    /usr/local/bin/omv-x735-fan.py &
    ;;
  stop)
    echo "Stopping omv-x735-fan.py"
    pkill -f /usr/local/bin/omv-x735-fan.py
    ;;
  *)
    echo "Usage: /etc/init.d/omv-x735-fan.sh {start|stop}"
    exit 1
    ;;
esac

exit 0