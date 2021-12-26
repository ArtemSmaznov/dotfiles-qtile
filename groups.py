from libqtile.config import DropDown, Group, Key, ScratchPad
from libqtile.dgroups import Match
from libqtile.lazy import lazy

import apps
from keys.bindings import keys
from keys.mods import *

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
            )
        ],
    ),

    Group(
        "gaming",
        label="",
        layout="max",
        matches=[
            Match(
                wm_class=[
                    "Wine",
                    "dolphin-emu",
                    "Lutris",
                    "Citra",
                    "SuperTuxKart",
                    "Steam",
                    "battle.net.exe",
                ]
            ),
            Match(
                title=[
                    "Steam",
                    "Battle.net",
                ]
            ),
        ],
    ),

    Group(
        "coding",
        label="",
        # spawn=apps.myTerminal,
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
                    "pcmanfm",
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
        spawn=apps.myCliMusicPlayer,
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
        layout="max",
        matches=[
            Match(
                wm_class=[
                    "virt-manager",
                    "VirtualBox Manager",
                    "VirtualBox Machine",
                    "Cypress",
                ]
            ),
        ],
    ),

]

s_width = 0.8
s_height = 0.8
s_left_margin = (1.0 - s_height) / 2
s_top_margin = (1.0 - s_height) / 2

# Add a ScratchPad Group
groups.append(
    ScratchPad(
        "scratchpad",
        [
            DropDown(
                "term",
                apps.myTerminal,
                x=s_left_margin,
                y=s_top_margin,
                width=s_width,
                height=s_height,
                warp_pointer=False,
            ),
            DropDown(
                "files",
                apps.myFileManager,
                x=s_left_margin,
                y=s_top_margin,
                width=s_width,
                height=s_height,
                warp_pointer=False,
            ),
            DropDown(
                "music",
                apps.myMusicPlayer,
                x=s_left_margin,
                y=s_top_margin,
                width=s_width,
                height=s_height,
                warp_pointer=False,
            ),
        ],
    ),
)

# Only map up to 10 Groups to number keys
def getNumberOfKeysForGroups():
    if len(groups) > 10:
        return 10
    else:
        return len(groups)


# Switch to another Group with SUPER + #
# Send current window to another Group SUPER + SHIFT + #
for i in range(getNumberOfKeysForGroups()):
    name = groups[i].name

    key = str(i + 1)
    if i + 1 == 10:
        key = "0"

    keys.append(Key([mod], key, lazy.group[name].toscreen()))
    keys.append(Key([mod, shift], key, lazy.window.togroup(name)))
