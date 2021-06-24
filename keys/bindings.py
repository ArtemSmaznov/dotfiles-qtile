from libqtile.config import Click, Drag, Key, KeyChord
from libqtile.lazy import lazy

from keys.mods import alt, ctrl, mod, shift
import settings.apps as apps
import settings.preferences as user
import utils

keys = [
    # ░█▀▀░█░█░█▀▀░▀█▀░█▀▀░█▄█
    # ░▀▀█░░█░░▀▀█░░█░░█▀▀░█░█
    # ░▀▀▀░░▀░░▀▀▀░░▀░░▀▀▀░▀░▀
    Key([mod, ctrl], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, ctrl], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    # Debugging
    Key([mod, ctrl], "d", lazy.group.next_window(), desc="Debugging hotkey"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "r", lazy.spawn(apps.launcher), desc="Open DMenu"),
    Key(
        [mod, shift], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"
    ),
    # Swith Keyboard Layouts
    Key([alt], "Shift_L", lazy.function(utils.switch_keyboard_layout)),
    # Media keys
    Key([], "XF86AudioRaiseVolume", lazy.function(utils.volume_increase)),
    Key([], "XF86AudioLowerVolume", lazy.function(utils.volume_decrease)),
    Key([], "XF86AudioMute", lazy.function(utils.volume_mute)),
    # Power Control
    Key(
        [alt], "F4", lazy.spawn("./.local/bin/dmscripts/dmpower"), desc="A logout menu"
    ),
    KeyChord(
        [mod],
        "z",
        [
            Key([], "l", lazy.spawn(apps.lock), desc="Lock Screen"),
            Key([], "s", lazy.spawn("systemctl suspend"), desc="Suspend System"),
            Key([], "p", lazy.spawn("systemctl poweroff"), desc="Shutdown System"),
            Key([], "r", lazy.spawn("systemctl reboot"), desc="Restart"),
        ],
    ),
    # ░█▀▀░█▀▀░█▀▄░█▀▀░█▀▀░█▀█░█▀▀░█░█░█▀█░▀█▀
    # ░▀▀█░█░░░█▀▄░█▀▀░█▀▀░█░█░▀▀█░█▀█░█░█░░█░
    # ░▀▀▀░▀▀▀░▀░▀░▀▀▀░▀▀▀░▀░▀░▀▀▀░▀░▀░▀▀▀░░▀░
    Key(
        [ctrl],
        "Print",
        lazy.spawn("/home/artem/.local/bin/dmscripts/dmscreenshot full"),
        desc="Full Desktop Screenshot",
    ),
    Key(
        [],
        "Print",
        lazy.spawn("/home/artem/.local/bin/dmscripts/dmscreenshot screen"),
        desc="Fullscreen Screenshot",
    ),
    Key(
        [mod, shift],
        "Print",
        lazy.spawn("/home/artem/.local/bin/dmscripts/dmscreenshot area"),
        desc="Selection Area Screenshot",
    ),
    Key(
        [alt],
        "Print",
        lazy.spawn("/home/artem/.local/bin/dmscripts/dmscreenshot window"),
        desc="Current Window Screenshot",
    ),
    # ░█▄█░█▀█░█▀█░▀█▀░▀█▀░█▀█░█▀▄░█▀▀
    # ░█░█░█░█░█░█░░█░░░█░░█░█░█▀▄░▀▀█
    # ░▀░▀░▀▀▀░▀░▀░▀▀▀░░▀░░▀▀▀░▀░▀░▀▀▀
    # Switch focus between monitors
    Key([mod, alt], "h", lazy.prev_screen(), desc="Move focus to prev monitor"),
    Key([mod, alt], "l", lazy.next_screen(), desc="Move focus to next monitor"),
    Key([mod], "F1", lazy.to_screen(0), desc="Move focus to first monitor"),
    Key([mod], "F2", lazy.to_screen(1), desc="Move focus to second monitor"),
    # ░█▀▀░█▀▄░█▀█░█░█░█▀█░█▀▀
    # ░█░█░█▀▄░█░█░█░█░█▀▀░▀▀█
    # ░▀▀▀░▀░▀░▀▀▀░▀▀▀░▀░░░▀▀▀
    Key([mod], "Tab", lazy.screen.toggle_group()),
    # ScratchPad
    Key([mod], "quoteleft", lazy.group["scratchpad"].dropdown_toggle("term")),
    Key([mod], "F12", lazy.group["coding"].toscreen(1)),
    # ░█░█░▀█▀░█▀█░█▀▄░█▀█░█░█░█▀▀
    # ░█▄█░░█░░█░█░█░█░█░█░█▄█░▀▀█
    # ░▀░▀░▀▀▀░▀░▀░▀▀░░▀▀▀░▀░▀░▀▀▀
    # Toggle windows states
    Key([mod], "f", lazy.window.toggle_floating(), desc="Toggle floating"),
    Key([mod], "m", lazy.window.toggle_maximize(), desc="Toggle maximize"),
    Key([mod], "F11", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen"),
    Key([mod], "d", lazy.window.toggle_minimize(), desc="Toggle minimize"),
    # ░█░░░█▀█░█░█░█▀█░█░█░▀█▀░█▀▀
    # ░█░░░█▀█░░█░░█░█░█░█░░█░░▀▀█
    # ░▀▀▀░▀░▀░░▀░░▀▀▀░▀▀▀░░▀░░▀▀▀
    # Toggle between different layouts
    Key([mod], "space", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, shift], "space", lazy.prev_layout(), desc="Toggle between layouts"),
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key(
        [alt], "Tab", lazy.group.next_window(), desc="Move window focus to other window"
    ),
    Key(
        [alt, shift],
        "Tab",
        lazy.group.prev_window(),
        desc="Move window focus to other window",
    ),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, shift], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key(
        [mod, shift], "l", lazy.layout.shuffle_right(), desc="Move window to the right"
    ),
    Key([mod, shift], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, shift], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, ctrl], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, ctrl], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, ctrl], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, ctrl], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "equal", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, shift],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    # ░█▀█░█▀█░█▀█░█▀▀
    # ░█▀█░█▀▀░█▀▀░▀▀█
    # ░▀░▀░▀░░░▀░░░▀▀▀
    Key([mod], "Return", lazy.spawn(apps.terminal), desc="Launch terminal"),
    # Main Applications launched with SUPER + KEY
    Key([mod], "e", lazy.spawn(apps.file_manager), desc="Launch file manager"),
    Key([mod], "b", lazy.spawn(apps.web_browser), desc="Launch web browser"),
    Key(
        [mod],
        "i",
        lazy.spawn(apps.incognito_browser),
        desc="Launch browser in incognito",
    ),
    Key([mod], "c", lazy.spawn(apps.ide), desc="Launch IDE"),
    # Secondary Applications launched with CTRL + ALT + KEY
    Key([ctrl, alt], "t", lazy.spawn(apps.terminal), desc="Launch terminal"),
    KeyChord(
        [mod],
        "o",
        [
            Key([], "b", lazy.spawn(apps.web_browser), desc="Launch web browser"),
            Key(
                [],
                "i",
                lazy.spawn(apps.incognito_browser),
                desc="Launch browser in incognito",
            ),
            Key([], "t", lazy.spawn(apps.tor_browser), desc="Launch tor browser"),
            Key([], "m", lazy.spawn(apps.music_player), desc="Launch music player"),
            Key([], "v", lazy.spawn(apps.video_player), desc="Launch video player"),
            Key([], "s", lazy.spawn(apps.game), desc="Launch Steam"),
        ],
    ),
    KeyChord(
        [ctrl, alt],
        "o",
        [
            Key([], "t", lazy.spawn(apps.text_editor), desc="Launch text editor"),
            Key([], "r", lazy.spawn(apps.vector_editor), desc="Launch vector editor"),
            Key([], "p", lazy.spawn(apps.photos_library), desc="Launch photos library"),
            Key(
                [], "g", lazy.spawn(apps.graphics_editor), desc="Launch graphics editor"
            ),
            Key([], "v", lazy.spawn(apps.video_editor), desc="Launch video editor"),
        ],
    ),
]


# ░█▄█░█▀█░█░█░█▀▀░█▀▀
# ░█░█░█░█░█░█░▀▀█░█▀▀
# ░▀░▀░▀▀▀░▀▀▀░▀▀▀░▀▀▀

# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]
