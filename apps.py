from libqtile.utils import guess_terminal

# cli tools
myTerminal      = guess_terminal()
myCliFiles      = myTerminal + " -e vifmrun"
myCliMusic      = myTerminal + " -e ncmpcpp"
myCliText       = myTerminal + " -e vim"
myCliSysAudio   = myTerminal + " -e alsamixer"
myCliSysMonitor = myTerminal + " -e btop"
myCliSysTasks   = myTerminal + " -e htop"

# core tools
myWebBrowser    = "qutebrowser"
myIncBrowser    = "qutebrowser --target private-window"
myTorBrowser    = "torbrowser-launcher"
myIde           = "emacsclient -c -a 'emacs'"
myFiles         = "pcmanfm"
mySteam         = "/usr/bin/steam-runtime %U"

# extra tools
myLauncher      = "rofi -show drun"
myPassManager   = "rofi-pass"
myVirtManager   = "virt-manager"
myTorrent       = "transmission-gtk"
myCalculator    = "gnome-calculator"
myAnki          = "anki"

# graphics tools
myPhotoLibrary  = "digikam"
myImgEditor     = "gimp"
myVctEditor     = "inkscape"
myVidEditor     = "kdenlive"

# chat apps
myWhatsApp      = "whatsapp-for-linux"
myDiscord       = "discord"

# system tools
mySysPower      = "xfce4-power-manager-settings"
mySysNetwork    = "nm-connection-editor"
mySysBluetooth  = "blueman-manager"
