#!/bin/bash
paplay '/usr/share/mint-artwork-cinnamon/sounds/login.oga' &
picom -b --experimental-backends --dbus &
nitrogen --restore &
solaar -w hide &
nm-applet &
redshift-gtk &
ckb-next -b &
/opt/piavpn/bin/pia-client --quiet &

alacritty &
chromium &
/usr/bin/steam-runtime %U &
