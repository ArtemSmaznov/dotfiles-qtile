#!/bin/bash
paplay '/usr/share/mint-artwork-cinnamon/sounds/login.oga' &
/opt/piavpn/bin/pia-client --quiet &
picom -b --experimental-backends --dbus &
nitrogen --restore &
redshift-gtk &
solaar -w hide &
nm-applet &

alacritty &
chromium &
/usr/bin/steam-runtime %U &
