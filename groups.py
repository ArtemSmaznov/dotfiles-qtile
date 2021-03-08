from libqtile.config import Group, Key
from libqtile.lazy import lazy
from libqtile.dgroups import Match

from keys.mods import mod, shift
from bindings import keys


group_names = [
    ("Web", {
        'layout': 'columns',
        'label': 'Web',
        'matches': [
            Match(wm_class=[
                "firefox",
                "Tor Browser",
                "Chromium",
                "Google-chrome",
            ]),
        ],
    }),
    ("Game", {
        'layout': 'columns',
        'matches': [
            Match(wm_class=[
                "Wine",
                "dolphin-emu",
                "Lutris",
                "Citra",
                "SuperTuxKart",
            ]),
        ],
    }),
    ("Dev", {
        'layout': 'columns',
        'matches': [
            Match(wm_class=[
                "Alacritty",
                "Terminator",
                "URxvt",
                "UXTerm",
                "kitty",
                "K3rmit",
                "XTerm",
                "Geany",
                "Atom",
                "Subl3",
                "code-oss",
                "Cypress",
                "Oomox",
                "Unity",
                "UnityHub",
                "jetbrains-studio",
            ]),
        ],
    }),
    ("PC", {
        'layout': 'monadtall',
        'matches': [
            Match(wm_class=[
                "dolphin",
                "ark",
                "Nemo",
                "File-roller",
                "googledocs",
                "keep",
                "calendar",
            ]),
        ],
    }),
    ("Mus", {
        'layout': 'columns',
        'matches': [
            Match(wm_class=[
                "Spotify",
                "youtubemusic",
            ]),
        ],
    }),
    ("Vid", {
        'layout': 'columns',
        'matches': [
            Match(wm_class=[
                "vlc",
                "Celluloid",
            ]),
        ],
    }),
    ("Misc", {
        'layout': 'columns',
        'matches': [
            Match(wm_class=[
                "whatsapp",
                "Slack",
                "discord",
                "obs",
            ]),
        ],
    }),
    ("Gfx", {
        'layout': 'columns',
        'matches': [
            Match(wm_class=[
                "Gimp-2.10",
                "Gimp",
                "Inkscape",
                "Flowblade",
                "digikam",
            ]),
        ],
    }),
    ("Vbox", {
        'layout': 'columns',
        'matches': [
            Match(wm_class=[
                "VirtualBox Manage",
                "VirtualBox Machine",
            ]),
        ],
    })
]

groups = [Group(name, **kwargs) for name, kwargs in group_names]

for i, (name, kwargs) in enumerate(group_names, 1):
    # Switch to another group with SUPER + #
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))

# Send current window to another group SUPER + SHIFT + #
    keys.append(Key([mod, shift], str(
        i), lazy.window.togroup(name, switch_group=False)))
