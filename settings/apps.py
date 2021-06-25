from libqtile.utils import guess_terminal

terminal = guess_terminal()
text_editor = terminal + " -e vim"
# web_browser = 'brave'
web_browser = "brave --disable-features=SendMouseLeaveEvents"
incognito_browser = web_browser + " --incognito"
tor_browser = "torbrowser-launcher"
file_manager = "nemo"
music_player = "youtubemusic-nativefier"
cli_music_player = terminal + " -e tmux attach -t music"
video_player = "celluloid"
game = "/usr/bin/steam-runtime %U"
ide = "emacs"
graphics_editor = "gimp"
vector_editor = "inkscape"
video_editor = "kdenlive"
photos_library = "digikam"
torrent_client = "transmission-qt"
vpn = "/opt/piavpn/bin/pia-client --quiet"
vm = "virtualbox"
launcher = "rofi -show drun"
password_manager = "rofi-pass"

network_manager = "nm-connection-editor"
bluetooth_manager = "blueman-manager"
power_manager = "xfce4-power-manager-settings"
audio_manager = terminal + " -e alsamixer"
lock = "xscreensaver-command -lock"
