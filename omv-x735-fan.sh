#! /bin/sh

### BEGIN INIT INFO
# Provides:          omv-x735-fan.py
# Required-Start:    $remote_fs $syslog
# Required-Stop:     $remote_fs $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
### END INIT INFO

# Carry out specific functions when asked to by the system
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