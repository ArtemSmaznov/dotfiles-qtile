from libqtile.utils import guess_terminal

# cli tools
myTerminal       = guess_terminal()
myCliText        = myTerminal + " -e vim"
myCliTaskManager = myTerminal + " -e htop"
myCliMonitor     = myTerminal + " -e btop"
myCliFiles       = myTerminal + " -e vifmrun"
myCliMusic       = myTerminal + " -e ncmpcpp"
myCliSysAudio    = myTerminal + " -e alsamixer"

# core tools
myLauncher       = "rofi -show drun"
myWebBrowser     = "qutebrowser"
myIncBrowser     = "qutebrowser --target private-window"
myTorBrowser     = "torbrowser-launcher"
myFiles          = "pcmanfm"
myIde            = "emacsclient -c -a 'emacs'"

# extra tools
mySteam          = "/usr/bin/steam-runtime %U"
myTorrent        = "transmission-gtk"
myPassManager    = "rofi-pass"
myVirtManager    = "virt-manager"
myCalculator     = "gnome-calculator"
myAnki           = "anki"

# graphics tools
myImgEditor      = "gimp"
myVctEditor      = "inkscape"
myVidEditor      = "kdenlive"
myPicLibrary     = "digikam"

# chat apps
myWhatsApp       = "whatsapp-for-linux"
myDiscord        = "discord"

# system tools
mySysNetwork     = "nm-connection-editor"
mySysBluetooth   = "blueman-manager"
mySysPower       = "xfce4-power-manager-settings"
