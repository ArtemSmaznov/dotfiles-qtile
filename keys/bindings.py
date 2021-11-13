import os

import apps as apps
import utils
from libqtile.config import Click, Drag, Key, KeyChord
from libqtile.lazy import lazy
from preferences import dmscripts

from keys.mods import *

dm = os.path.expanduser(dmscripts)

keys = [
    #
    # ░█▀▀░█░█░█▀▀░▀█▀░█▀▀░█▄█
    # ░▀▀█░░█░░▀▀█░░█░░█▀▀░█░█
    # ░▀▀▀░░▀░░▀▀▀░░▀░░▀▀▀░▀░▀
    #
    Key([mod, ctrl], "r", lazy.restart(), desc="Restart qTile"),
    Key([mod, ctrl], "q", lazy.shutdown(), desc="Quit qTile"),
    #
    # Debugging
    #
    Key(
        [mod, ctrl],
        "d",
        lazy.hide_show_bar("all"),
        desc="Debugging hotkey",
    ),
    #
    # Swith Keyboard Layouts
    #
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
    #
    # Changing UI
    #
    KeyChord(
        [mod],
        "t",
        [
            Key([], "b", lazy.hide_show_bar("all"), desc="Toggle bars"),
            Key([], "z", lazy.hide_show_bar("all"), desc="Toggle bars"),
        ],
        mode="Toggle",
    ),
    #
    # ░█░█░▀█▀░█▀█░█▀▄░█▀█░█░█░█▀▀
    # ░█▄█░░█░░█░█░█░█░█░█░█▄█░▀▀█
    # ░▀░▀░▀▀▀░▀░▀░▀▀░░▀▀▀░▀░▀░▀▀▀
    #
    Key([mod], "q", lazy.window.kill(), desc="Close focused Window"),
    # Toggle windows states
    Key([mod], "F11", lazy.window.toggle_fullscreen(), desc="Toggle Fullscreen"),
    Key([mod], "f", lazy.window.toggle_floating(), desc="Toggle Floating"),
    Key([mod], "m", lazy.window.toggle_maximize(), desc="Toggle Maximize"),
    Key(
        [mod],
        "d",
        lazy.window.toggle_minimize(),
        lazy.layout.down(),
        desc="Toggle Minimize",
    ),
    # Switch between windows
    Key([alt], "Tab", lazy.group.next_window(), desc="Move focus to next Window"),
    Key(
        [alt, shift],
        "Tab",
        lazy.group.prev_window(),
        desc="Move focus to prev Window",
    ),
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left Window"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right Window"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus to below Window"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus to above Window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key(
        [mod, shift],
        "h",
        lazy.layout.shuffle_left(),
        desc="Swap focused Window with the one to the left",
    ),
    Key(
        [mod, shift],
        "l",
        lazy.layout.shuffle_right(),
        desc="Swap focused Window with the one to the right",
    ),
    Key(
        [mod, shift],
        "j",
        lazy.layout.shuffle_down(),
        desc="Swap focused Window with the one below",
    ),
    Key(
        [mod, shift],
        "k",
        lazy.layout.shuffle_up(),
        desc="Swap focused Window with the one above",
    ),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key(
        [mod, ctrl],
        "h",
        lazy.layout.grow_left(),
        desc="Grow focused Window left",
    ),
    Key(
        [mod, ctrl],
        "l",
        lazy.layout.grow_right(),
        desc="Grow focused Window right",
    ),
    Key([mod, ctrl], "j", lazy.layout.grow_down(), desc="Grow focused Window down"),
    Key([mod, ctrl], "k", lazy.layout.grow_up(), desc="Grow focused Window up"),
    #
    # ░█▄█░█▀█░█▀█░▀█▀░▀█▀░█▀█░█▀▄░█▀▀
    # ░█░█░█░█░█░█░░█░░░█░░█░█░█▀▄░▀▀█
    # ░▀░▀░▀▀▀░▀░▀░▀▀▀░░▀░░▀▀▀░▀░▀░▀▀▀
    #
    # Switch focus between monitors
    Key([mod], "comma", lazy.prev_screen(), desc="Move focus to prev Screen"),
    Key([mod], "period", lazy.next_screen(), desc="Move focus to next Screen"),
    Key([mod], "F1", lazy.to_screen(0), desc="Move focus to 1st Screen"),
    Key([mod], "F2", lazy.to_screen(1), desc="Move focus to 2nd Screen"),
    #
    # ░█░░░█▀█░█░█░█▀█░█░█░▀█▀░█▀▀
    # ░█░░░█▀█░░█░░█░█░█░█░░█░░▀▀█
    # ░▀▀▀░▀░▀░░▀░░▀▀▀░▀▀▀░░▀░░▀▀▀
    #
    # Switch between layouts
    Key([mod], "space", lazy.next_layout(), desc="Switch Laouts"),
    Key([mod, shift], "space", lazy.prev_layout(), desc="Switch Laouts"),
    Key([mod, alt], "space", lazy.to_layout_index(0), desc="Switch to default Layout"),
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
    #
    # ░█▀▀░█▀▄░█▀█░█░█░█▀█░█▀▀
    # ░█░█░█▀▄░█░█░█░█░█▀▀░▀▀█
    # ░▀▀▀░▀░▀░▀▀▀░▀▀▀░▀░░░▀▀▀
    #
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
    #
    # ░█▄█░█▀▀░█▀▄░▀█▀░█▀█
    # ░█░█░█▀▀░█░█░░█░░█▀█
    # ░▀░▀░▀▀▀░▀▀░░▀▀▀░▀░▀
    #
    Key([], "XF86AudioRaiseVolume", lazy.function(utils.volume_increase)),
    Key([], "XF86AudioLowerVolume", lazy.function(utils.volume_decrease)),
    Key([], "XF86AudioMute", lazy.function(utils.volume_mute)),
    #
    # ░█▀█░█▀█░█▀█░█▀▀
    # ░█▀█░█▀▀░█▀▀░▀▀█
    # ░▀░▀░▀░░░▀░░░▀▀▀
    Key([ctrl, alt], "t", lazy.spawn(apps.terminal), desc="Launch Terminal"),
    Key([mod], "Return", lazy.spawn(apps.terminal), desc="Launch Terminal"),
    Key([mod], "c", lazy.spawn(apps.ide), desc="Launch IDE"),
    Key([mod], "e", lazy.spawn(apps.file_manager), desc="Launch File Manager"),
    Key([mod], "b", lazy.spawn(apps.web_browser), desc="Launch Web Browser"),
    Key(
        [mod],
        "i",
        lazy.spawn(apps.incognito_browser),
        desc="Launch Web Browser in Incognito Mode",
    ),
    Key(
        [mod],
        "p",
        lazy.spawn(apps.password_manager),
        desc="Launch password manager",
    ),
    Key([mod], "r", lazy.spawn(apps.launcher), desc="Launch Launcher"),
    Key([mod, shift], "r", lazy.spawncmd(), desc="Launch Prompt Widget"),
    # Primary
    KeyChord(
        [mod],
        "o",
        [
            Key([], "t", lazy.spawn(apps.tor_browser), desc="Launch Tor Browser"),
            Key([], "m", lazy.spawn(apps.music_player), desc="Launch Music Player"),
            Key([], "v", lazy.spawn(apps.video_player), desc="Launch Video Player"),
            Key([], "s", lazy.spawn(apps.game), desc="Launch Steam"),
        ],
        mode="Open Primary",
    ),
    # Secondary
    KeyChord(
        [ctrl, alt],
        "o",
        [
            Key([], "t", lazy.spawn(apps.text_editor), desc="Launch Text Editor"),
            Key([], "p", lazy.spawn(apps.photo_library), desc="Launch Photo Library"),
            Key([], "g", lazy.spawn(apps.image_editor), desc="Launch Image Editor"),
            Key([], "r", lazy.spawn(apps.vector_editor), desc="Launch Vector Editor"),
            Key([], "v", lazy.spawn(apps.video_editor), desc="Launch Video Editor"),
        ],
        mode="Open Secondary",
    ),
    #
    # ░█▀▄░█▄█░░░░░█▀▀░█▀▀░█▀▄░▀█▀░█▀█░▀█▀░█▀▀
    # ░█░█░█░█░▄▄▄░▀▀█░█░░░█▀▄░░█░░█▀▀░░█░░▀▀█
    # ░▀▀░░▀░▀░░░░░▀▀▀░▀▀▀░▀░▀░▀▀▀░▀░░░░▀░░▀▀▀
    #
    KeyChord(
        [mod],
        "s",
        [
            Key([mod], "s", lazy.spawn(dm + "dm-master"), desc="Lock Screen"),
            Key([], "w", lazy.spawn(dm + "dm-wallpaper"), desc="Lock Screen"),
            Key([], "r", lazy.spawn(dm + "dm-record"), desc="Lock Screen"),
            Key([], "p", lazy.spawn(dm + "dm-power"), desc="Lock Screen"),
            Key([], "s", lazy.spawn(dm + "dm-screenshot"), desc="Lock Screen"),
            # Key([], "b", lazy.spawn(dm + "dm-bookman"), desc="Lock Screen"),
            Key([], "n", lazy.spawn(dm + "dm-notify"), desc="Lock Screen"),
            Key([], "backslash", lazy.spawn(dm + "dm-notify"), desc="Lock Screen"),
        ],
        mode="dm-scripts",
    ),
    #
    # ░█▀█░█▀█░█░█░█▀▀░█▀▄
    # ░█▀▀░█░█░█▄█░█▀▀░█▀▄
    # ░▀░░░▀▀▀░▀░▀░▀▀▀░▀░▀
    #
    Key([alt], "F4", lazy.spawn(dm + "dm-power"), desc="Logout Menu"),
    KeyChord(
        [mod],
        "z",
        [
            Key([], "z", lazy.spawn(dm + "dm-power"), desc="dm-power"),
            Key([], "l", lazy.spawn(dm + "dm-power lock"), desc="Lock Screen"),
            Key([], "s", lazy.spawn(dm + "dm-power suspend"), desc="Suspend System"),
            Key([], "p", lazy.spawn(dm + "dm-power poweroff"), desc="Shutdown System"),
            Key([], "r", lazy.spawn(dm + "dm-power reboot"), desc="Reboot System"),
            Key([], "w", lazy.spawn(dm + "dm-power windows"), desc="Reboot to Windows"),
        ],
        mode="(l)ock, (s)uspend, (p)oweroff, (r)eboot, (w)indows",
    ),
    #
    # ░█▀▀░█▀▀░█▀▄░█▀▀░█▀▀░█▀█░█▀▀░█░█░█▀█░▀█▀
    # ░▀▀█░█░░░█▀▄░█▀▀░█▀▀░█░█░▀▀█░█▀█░█░█░░█░
    # ░▀▀▀░▀▀▀░▀░▀░▀▀▀░▀▀▀░▀░▀░▀▀▀░▀░▀░▀▀▀░░▀░
    #
    Key(
        [mod],
        "Print",
        lazy.spawn(dm + "dm-screenshot full"),
        desc="Full Desktop Screenshot",
    ),
    Key(
        [],
        "Print",
        lazy.spawn(dm + "dm-screenshot screen"),
        desc="Fullscreen Screenshot",
    ),
    Key(
        [mod, shift],
        "Print",
        lazy.spawn(dm + "dm-screenshot area"),
        desc="Selection Area Screenshot",
    ),
    Key(
        [alt],
        "Print",
        lazy.spawn(dm + "dm-screenshot window"),
        desc="Active Window Screenshot",
    ),
    #
    # ░█▀█░█▀█░▀█▀░▀█▀░█▀▀░▀█▀░█▀▀░█▀█░▀█▀░▀█▀░█▀█░█▀█░█▀▀
    # ░█░█░█░█░░█░░░█░░█▀▀░░█░░█░░░█▀█░░█░░░█░░█░█░█░█░▀▀█
    # ░▀░▀░▀▀▀░░▀░░▀▀▀░▀░░░▀▀▀░▀▀▀░▀░▀░░▀░░▀▀▀░▀▀▀░▀░▀░▀▀▀
    #
    KeyChord(
        [mod],
        "backslash",
        [
            Key(
                [],
                "backslash",
                lazy.spawn(dm + "dm-notify recents"),
                desc="Show recent Notifications",
            ),
            Key(
                [],
                "r",
                lazy.spawn(dm + "dm-notify recents"),
                desc="Show recent Notifications",
            ),
            Key(
                [shift],
                "c",
                lazy.spawn(dm + "dm-notify clear"),
                desc="Clear all Notifications",
            ),
            Key(
                [],
                "c",
                lazy.spawn(dm + "dm-notify close"),
                desc="Clear last Notification",
            ),
            Key(
                [],
                "a",
                lazy.spawn(dm + "dm-notify context"),
                desc="Open last Notification",
            ),
        ],
        mode="Notifications",
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
