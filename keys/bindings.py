from libqtile.config import Click, Drag, Key
from libqtile.lazy import lazy

from keys.mods import alt, ctrl, mod, shift
import settings.apps as apps
import utils


keys = [
    # System Control
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, shift], "r", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),
    Key([mod], "r", lazy.spawn(
        "rofi -show drun"), desc="Open DMenu"),
    Key([mod, ctrl], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, ctrl], "q", lazy.shutdown(), desc="Shutdown Qtile"),

    # Swith Keyboard Layouts
    Key([alt], "Shift_L", lazy.function(utils.switch_keyboard_layout)),

    # Toggle between different layouts as defined below
    Key([mod], "space", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, shift], "space", lazy.prev_layout(),
        desc="Toggle between layouts"),

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
    Key([alt], "Tab", lazy.layout.next(),
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
    Key([mod], "Return", lazy.spawn(apps.terminal), desc="Launch terminal"),

    # Toggle windows states
    Key([mod], "f",
        lazy.window.toggle_floating(),
        desc='toggle floating'),
    Key([mod], "m",
        lazy.window.toggle_maximize(),
        desc='toggle maximize'),
    Key([mod], "d",
        lazy.window.toggle_minimize(),
        desc='toggle minimize'),
    Key([mod], "F11",
        lazy.window.toggle_fullscreen(),
        desc='toggle fullscreen'),

    # Main Applications launched with SUPER + KEY
    Key([mod], "e", lazy.spawn(apps.file_manager), desc="Launch file manager"),
    Key([mod], "b", lazy.spawn(apps.web_browser), desc="Launch web browser"),
    Key([mod], "i", lazy.spawn(apps.incognito_browser),
        desc="Launch incognito browser"),
    #  desc="Launch web browser in incognito mode"),
    Key([mod], "t", lazy.spawn(apps.tor_browser), desc="Launch tor browser"),
    Key([mod], "c", lazy.spawn(apps.ide), desc="Launch IDE"),


    # Secondary Applications launched with CTRL + ALT + KEY
    Key([ctrl, alt], "t", lazy.spawn(apps.terminal), desc="Launch terminal"),
    Key([ctrl, alt], "m", lazy.spawn(
        apps.music_player), desc="Launch music player"),
    Key([ctrl, alt], "p", lazy.spawn(apps.photos_library),
        desc="Launch photos library"),
    Key([ctrl, alt], "v", lazy.spawn(
        apps.video_player), desc="Launch video player"),
    Key([ctrl, alt], "g", lazy.spawn(apps.graphics_editor),
        desc="Launch graphics editor"),
    Key([ctrl, alt], "s", lazy.spawn(apps.game), desc="Launch Steam"),

    # Media keys
    Key([], "XF86AudioRaiseVolume", lazy.spawn('amixer -q sset Master on 5%+')),
    Key([], "XF86AudioLowerVolume", lazy.spawn('amixer -q sset Master on 5%-')),
    Key([], "XF86AudioMute", lazy.spawn('amixer -q sset Master toggle')),


]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]
