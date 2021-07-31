from libqtile.config import DropDown, Group, Key, ScratchPad
from libqtile.dgroups import Match
from libqtile.lazy import lazy

import apps
from keys.bindings import keys
from keys.mods import *

# Most icons taken from https://fontawesome.com/

# Optional group parameters
# label="",
# layout="columns",
# spawn=apps.web_browser,

# Define Groups
groups = [
    Group(
        "internet",
        label="",
        matches=[
            Match(
                wm_class=[
                    "firefox",
                    "Tor Browser",
                    "Chromium",
                    "Google-chrome",
                    "Brave-browser",
                    "vivaldi-stable",
                    "qutebrowser",
                    "nyxt",
                ]
            ),
        ],
    ),
    Group(
        "gaming",
        label="",
        matches=[
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
    ),
    Group(
        "coding",
        label="",
        # spawn=apps.terminal,
        matches=[
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
    ),
    Group(
        "computer",
        label="",
        matches=[
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
    ),
    Group(
        "music",
        label="",
        spawn=apps.cli_music_player,
        matches=[
            Match(
                wm_class=[
                    "Spotify",
                    "youtubemusic-nativefier-040164",
                ]
            ),
        ],
    ),
    Group(
        "graphics",
        label="",
        matches=[
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
    ),
    Group(
        "video",
        label="",
        matches=[
            Match(
                title=[
                    "Celluloid",
                ],
            ),
            Match(
                wm_class=[
                    "vlc",
                    "obs",
                    "kdenlive",
                ],
            ),
        ],
    ),
    Group(
        "chat",
        label="",
        matches=[
            Match(
                wm_class=[
                    "whatsapp-for-linux",
                    "Slack",
                    "discord",
                    "signal",
                ]
            ),
        ],
    ),
    Group(
        "sandbox",
        label="",
        matches=[
            Match(
                wm_class=[
                    "VirtualBox Manage",
                    "VirtualBox Machine",
                ]
            ),
        ],
    ),
]

# Add a ScratchPad Group
groups.append(
    ScratchPad(
        "scratchpad",
        [
            DropDown("term", apps.terminal, height=0.6, warp_pointer=False),
        ],
    ),
)

# Switch to another Group with SUPER + #
# Send current window to another Group SUPER + SHIFT + #
for i in range(10):
    name = groups[i].name

    key = str(i + 1)
    if i + 1 == 10:
        key = "0"

    keys.append(Key([mod], key, lazy.group[name].toscreen()))
    keys.append(Key([mod, shift], key, lazy.window.togroup(name)))
