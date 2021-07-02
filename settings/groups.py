import re

from libqtile.config import DropDown, Group, Key, ScratchPad
from libqtile.dgroups import Match, simple_key_binder
from libqtile.lazy import lazy

from keys.bindings import keys
from keys.mods import mod, shift
import settings.apps as apps

# Most icons taken from https://fontawesome.com/

# Optional group parameters
# label="",
# layout="columns",
# spawn=apps.web_browser,

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
        spawn=apps.terminal,
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
                wm_class=[
                    "vlc",
                    "Celluloid",
                    "obs",
                    "kdenlive",
                ]
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
    ScratchPad(
        "scratchpad",
        [
            DropDown("term", apps.terminal, height=0.6, warp_pointer=False),
        ],
    ),
]

# Switch to another group with SUPER + #
# Send current window to another group SUPER + SHIFT + #
dgroups_key_binder = simple_key_binder(mod)
