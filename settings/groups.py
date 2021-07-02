import re

from libqtile.config import DropDown, Group, Key, ScratchPad
from libqtile.dgroups import Match
from libqtile.lazy import lazy

from keys.bindings import keys
from keys.mods import mod, shift
import settings.apps as apps

# Optional group parameters
# "label": "",
# "layout": "columns",
# 'spawn': apps.web_browser,

# Most icons taken from https://fontawesome.com/
group_names = [
    (
        "internet",
        {
            "label": "",
            "matches": [
                Match(
                    wm_class=[
                        "firefox",
                        "Tor Browser",
                        "Chromium",
                        "Google-chrome",
                        "Brave-browser",
                        "vivaldi-stable",
                    ]
                ),
            ],
        },
    ),
    (
        "gaming",
        {
            "label": "",
            "matches": [
                Match(
                    wm_class=[
                        "Wine",
                        "dolphin-emu",
                        "Lutris",
                        "Citra",
                        "SuperTuxKart",
                        "Steam",
                    ]
                ),
                Match(title="Steam"),
            ],
        },
    ),
    (
        "coding",
        {
            "label": "",
            "spawn": apps.terminal,
            "matches": [
                Match(
                    wm_class=[
                        # 'Alacritty',
                        # 'Terminator',
                        # 'URxvt',
                        # 'UXTerm',
                        # 'kitty',
                        # 'K3rmit',
                        # 'XTerm',
                        "Geany",
                        "Atom",
                        "Subl3",
                        "code-oss",
                        "Emacs",
                        "Cypress",
                        "Oomox",
                        "Unity",
                        "UnityHub",
                        "jetbrains-studio",
                    ]
                ),
            ],
        },
    ),
    (
        "computer",
        {
            "label": "",
            "matches": [
                Match(
                    wm_class=[
                        "dolphin",
                        "ark",
                        "Nemo",
                        "File-roller",
                        "googledocs",
                        "keep",
                        "calendar",
                    ]
                ),
            ],
        },
    ),
    (
        "music",
        {
            "label": "",
            "spawn": apps.cli_music_player,
            "matches": [
                Match(
                    wm_class=[
                        "Spotify",
                        "youtubemusic-nativefier-040164",
                    ]
                ),
            ],
        },
    ),
    (
        "graphics",
        {
            "label": "",
            "matches": [
                Match(
                    wm_class=[
                        "Gimp-2.10",
                        "Gimp",
                        "Inkscape",
                        "Flowblade",
                        "digikam",
                    ]
                ),
            ],
        },
    ),
    (
        "video",
        {
            "label": "",
            "matches": [
                Match(
                    wm_class=[
                        "vlc",
                        "Celluloid",
                        "obs",
                        "kdenlive",
                    ]
                ),
            ],
        },
    ),
    (
        "chat",
        {
            "label": "",
            "matches": [
                Match(
                    wm_class=[
                        "whatsapp-for-linux",
                        "Slack",
                        "discord",
                        "signal",
                    ]
                ),
            ],
        },
    ),
    (
        "sandbox",
        {
            "label": "",
            "matches": [
                Match(
                    wm_class=[
                        "VirtualBox Manage",
                        "VirtualBox Machine",
                    ]
                ),
            ],
        },
    ),
]

groups = [
    *[Group(name, **kwargs) for name, kwargs in group_names],
    ScratchPad(
        "scratchpad",
        [
            DropDown("term", apps.terminal, height=0.6, warp_pointer=False),
        ],
    ),
]

for i, (name, kwargs) in enumerate(group_names, 1):
    # Switch to another group with SUPER + #
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))

    # Send current window to another group SUPER + SHIFT + #
    keys.append(
        Key([mod, shift], str(i), lazy.window.togroup(name, switch_group=False))
    )
