import os

import apps as apps
import utils
from libqtile.config import Click, Drag, Key, KeyChord
from libqtile.lazy import lazy
from preferences import dmscripts

from keys.mods import *

dm = os.path.expanduser(dmscripts)

keys = [
    # ░█▀▀░█░█░█▀▀░▀█▀░█▀▀░█▄█
    # ░▀▀█░░█░░▀▀█░░█░░█▀▀░█░█
    # ░▀▀▀░░▀░░▀▀▀░░▀░░▀▀▀░▀░▀
    Key([mod, ctrl], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, ctrl], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    # Debugging
    Key(
        [mod, ctrl],
        "d",
        lazy.widget["keyboardlayout"].next_keyboard(),
        desc="Debugging hotkey",
    ),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "r", lazy.spawn(apps.launcher), desc="Open DMenu"),
    Key(
        [mod, shift], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"
    ),
    # Swith Keyboard Layouts
    # Key(
    #     [alt],
    #     "Shift_L",
    #     lazy.widget["keyboardlayout"].next_keyboard(),
    #     desc="Next keyboard layout"
    # ),
    Key(
        [shift],
        "Alt_L",
        lazy.widget["keyboardlayout"].next_keyboard(),
        desc="Next keyboard layout",
    ),
    # Media keys
    Key([], "XF86AudioRaiseVolume", lazy.function(utils.volume_increase)),
    Key([], "XF86AudioLowerVolume", lazy.function(utils.volume_decrease)),
    Key([], "XF86AudioMute", lazy.function(utils.volume_mute)),
    # Power Control
    Key([alt], "F4", lazy.spawn(dm + "dmpower"), desc="A logout menu"),
    KeyChord(
        [mod],
        "z",
        [
            Key([], "l", lazy.spawn(dm + "dmpower lock"), desc="Lock Screen"),
            Key([], "s", lazy.spawn(dm + "dmpower suspend"), desc="Suspend System"),
            Key([], "p", lazy.spawn(dm + "dmpower poweroff"), desc="Shutdown System"),
            Key([], "r", lazy.spawn(dm + "dmpower reboot"), desc="Reboot"),
            Key([], "w", lazy.spawn(dm + "dmpower windows"), desc="Reboot to Windows"),
        ],
        mode="(l)ock, (s)uspend, (p)oweroff, (r)eboot, (w)indows",
    ),
    # Notifications
    KeyChord(
        [mod],
        "backslash",
        [
            Key([], "backslash", lazy.spawn(dm + "dmnotify recents")),
            Key([], "r", lazy.spawn(dm + "dmnotify recents")),
            Key([], "a", lazy.spawn(dm + "dmnotify context")),
            Key([], "c", lazy.spawn(dm + "dmnotify close")),
            Key([shift], "c", lazy.spawn(dm + "dmnotify clear")),
        ],
        mode="Notifications",
    ),
    # ░█▀▀░█▀▀░█▀▄░█▀▀░█▀▀░█▀█░█▀▀░█░█░█▀█░▀█▀
    # ░▀▀█░█░░░█▀▄░█▀▀░█▀▀░█░█░▀▀█░█▀█░█░█░░█░
    # ░▀▀▀░▀▀▀░▀░▀░▀▀▀░▀▀▀░▀░▀░▀▀▀░▀░▀░▀▀▀░░▀░
    Key(
        [mod],
        "Print",
        lazy.spawn(dm + "dmscreenshot full"),
        desc="Full Desktop Screenshot",
    ),
    Key(
        [],
        "Print",
        lazy.spawn(dm + "dmscreenshot screen"),
        desc="Fullscreen Screenshot",
    ),
    Key(
        [mod, shift],
        "Print",
        lazy.spawn(dm + "dmscreenshot area"),
        desc="Selection Area Screenshot",
    ),
    Key(
        [alt],
        "Print",
        lazy.spawn(dm + "dmscreenshot window"),
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
    KeyChord(
        [mod],
        "g",
        [
            Key(
                [], "h", lazy.screen.prev_group(), desc="Move to the group on the left"
            ),
            Key(
                [], "l", lazy.screen.next_group(), desc="Move to the group on the right"
            ),
            Key(
                [],
                "d",
                lazy.function(utils.clear_default_groups),
                desc="Delete system 1-9 groups after a bad config",
            ),
        ],
        mode="Groups",
    ),
    # ░█░█░▀█▀░█▀█░█▀▄░█▀█░█░█░█▀▀
    # ░█▄█░░█░░█░█░█░█░█░█░█▄█░▀▀█
    # ░▀░▀░▀▀▀░▀░▀░▀▀░░▀▀▀░▀░▀░▀▀▀
    # Toggle windows states
    Key([mod], "f", lazy.window.toggle_floating(), desc="Toggle floating"),
    Key([mod], "m", lazy.window.toggle_maximize(), desc="Toggle maximize"),
    Key([mod], "F11", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen"),
    Key(
        [mod],
        "d",
        lazy.window.toggle_minimize(),
        lazy.layout.down(),
        desc="Toggle minimize",
    ),
    # ░█░░░█▀█░█░█░█▀█░█░█░▀█▀░█▀▀
    # ░█░░░█▀█░░█░░█░█░█░█░░█░░▀▀█
    # ░▀▀▀░▀░▀░░▀░░▀▀▀░▀▀▀░░▀░░▀▀▀
    # Switch between layouts
    Key([mod], "space", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, shift], "space", lazy.prev_layout(), desc="Toggle between layouts"),
    Key([mod, alt], "space", lazy.to_layout_index(0), desc="Switch to first layout"),
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
    # Secondary Applications
    Key(
        [mod],
        "p",
        lazy.spawn(apps.password_manager),
        desc="Launch password manager",
    ),
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
        mode="Open Primary",
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
        mode="Open Secondary",
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
