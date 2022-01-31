#! /bin/sh

set -e

cd "$(dirname "$0")"

echo "=> Installing omv-x735-fan\n"
sudo cp omv-x735-fan.py /usr/local/bin/
sudo chmod +x /usr/local/bin/omv-x735-fan.py

echo "=> Starting omv-x735-fan\n"
sudo cp omv-x735-fan.sh /etc/init.d/
sudo chmod +x /etc/init.d/omv-x735-fan.sh

sudo update-rc.d omv-x735-fan.sh defaults
sudo /etc/init.d/omv-x735-fan.sh start

echo "=> Done!\n"