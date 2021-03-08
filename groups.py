import subprocess
from libqtile.config import Group, Key
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.widget import volume

#  Key modifiers
mod = "mod4"
alt = "mod1"
ctrl = "control"
shift = "shift"

terminal = guess_terminal()
text_editor = 'xed'
web_browser = 'chromium'
tor_browser = 'torbrowser-launcher'
incognito_browser = 'chromium --incognito'
file_manager = 'nemo'
music_player = 'youtubemusic-nativefier'
video_player = 'celluloid'
game = '/usr/bin/steam-runtime %U'
ide = 'code'
graphics_editor = 'gimp'
vector_editor = 'inkscape'
video_editor = 'kdenlive'
photos_library = 'digikam'
torrent_client = 'transmission-qt'
vpn = '/opt/piavpn/bin/pia-client --quiet'
vm = 'virtualbox'

network_manager = 'nm-connection-editor'
bluetooth_manager = 'blueman-manager'
power_manager = 'xfce4-power-manager-settings'
audio_manager = 'cinnamon-settings sound'
package_manager = 'pamac-manager'
lock = 'cinnamon-screensaver-command -l'

keys = [
    # System Control
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "r", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),
    Key([mod, ctrl], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, ctrl], "q", lazy.shutdown(), desc="Shutdown Qtile"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),

    #  Switch focus between monitors
    Key([mod], "period", lazy.next_screen(),
        desc='Move focus to next monitor'),
    Key([mod], "comma", lazy.prev_screen(),
        desc='Move focus to prev monitor'),

    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, shift], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, shift], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, shift], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, shift], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, ctrl], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, ctrl], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, ctrl], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, ctrl], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, shift], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle windows states
    Key([mod], "m",
        lazy.layout.maximize(),
        desc='toggle maximize'),
    Key([mod], "w",
        lazy.window.toggle_floating(),
        desc='toggle floating'),
    Key([mod], "f",
        lazy.window.toggle_fullscreen(),
        desc='toggle fullscreen'),

    # Main Applications launched with SUPER + KEY
    Key([mod], "e", lazy.spawn(file_manager), desc="Launch file manager"),
    Key([mod], "b", lazy.spawn(web_browser), desc="Launch web browser"),
    Key([mod], "i", lazy.spawn(incognito_browser),
        desc="Launch incognito browser"),
    #  desc="Launch web browser in incognito mode"),
    Key([mod], "t", lazy.spawn(tor_browser), desc="Launch tor browser"),
    Key([mod], "c", lazy.spawn(ide), desc="Launch IDE"),


    # Secondary Applications launched with CTRL + ALT + KEY
    Key([ctrl, alt], "t", lazy.spawn(terminal), desc="Launch terminal"),
    Key([ctrl, alt], "m", lazy.spawn(music_player), desc="Launch music player"),
    Key([ctrl, alt], "p", lazy.spawn(photos_library),
        desc="Launch photos library"),
    Key([ctrl, alt], "v", lazy.spawn(video_player), desc="Launch video player"),
    Key([ctrl, alt], "g", lazy.spawn(graphics_editor),
        desc="Launch graphics editor"),
    Key([ctrl, alt], "s", lazy.spawn(game), desc="Launch Steam"),

    # Media keys
    Key([], "XF86AudioRaiseVolume", lazy.spawn('amixer -q sset Master on 5%+')),
    Key([], "XF86AudioLowerVolume", lazy.spawn('amixer -q sset Master on 5%-')),
    Key([], "XF86AudioMute", lazy.spawn('amixer -q sset Master toggle')),


]

group_names = [("Web", {'layout': 'columns'}),
               ("Game", {'layout': 'columns'}),
               ("Dev", {'layout': 'columns'}),
               ("PC", {'layout': 'columns'}),
               ("Mus", {'layout': 'columns'}),
               ("Vid", {'layout': 'columns'}),
               ("Misc", {'layout': 'columns'}),
               ("Gfx", {'layout': 'columns'}),
               ("Vbox", {'layout': 'columns'})]

groups = [Group(name, **kwargs) for name, kwargs in group_names]

for i, (name, kwargs) in enumerate(group_names, 1):
    # Switch to another group with SUPER + #
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))
    # Send current window to another group SUPER + SHIFT + #
    keys.append(Key([mod, "shift"], str(
        i), lazy.window.togroup(name, switch_group=False)))
