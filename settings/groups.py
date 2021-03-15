from libqtile.config import DropDown, Group, Key, ScratchPad
from libqtile.dgroups import Match
from libqtile.lazy import lazy

from keys.bindings import keys
from keys.mods import mod, shift
import settings.apps as apps


group_names = [
    ('internet', {
        'label': '1 ',
        'layout': 'columns',
        'matches': [
            Match(wm_class=[
                'firefox',
                'Tor Browser',
                'Chromium',
                'Google-chrome',
            ]),
        ],
    }),
    ('gaming', {
        'label': '2 ',
        'layout': 'max',
        'matches': [
            Match(wm_class=[
                'Wine',
                'dolphin-emu',
                'Lutris',
                'Citra',
                'SuperTuxKart',
                'Steam',
            ]),
        ],
    }),
    ('coding', {
        'label': '3 ',
        'layout': 'columns',
        'matches': [
            Match(wm_class=[
                'Alacritty',
                'Terminator',
                'URxvt',
                'UXTerm',
                'kitty',
                'K3rmit',
                'XTerm',
                'Geany',
                'Atom',
                'Subl3',
                'code-oss',
                'Cypress',
                'Oomox',
                'Unity',
                'UnityHub',
                'jetbrains-studio',
            ]),
        ],
    }),
    ('computer', {
        'label': '4 ',
        'layout': 'monadtall',
        'matches': [
            Match(wm_class=[
                'dolphin',
                'ark',
                'Nemo',
                'File-roller',
                'googledocs',
                'keep',
                'calendar',
            ]),
        ],
    }),
    ('graphics', {
        'label': '5 ',
        'layout': 'columns',
        'matches': [
            Match(wm_class=[
                'Gimp-2.10',
                'Gimp',
                'Inkscape',
                'Flowblade',
                'digikam',
            ]),
        ],
    }),
    ('video', {
        'label': '6 ',
        'layout': 'columns',
        'matches': [
            Match(wm_class=[
                'vlc',
                'Celluloid',
            ]),
        ],
    }),
    ('music', {
        'label': '7 ',
        'layout': 'columns',
        'matches': [
            Match(wm_class=[
                'Spotify',
                'youtubemusic-nativefier-040164',
            ]),
        ],
    }),
    ('misc', {
        'label': '8 ',
        'layout': 'columns',
        'matches': [
            Match(wm_class=[
                'whatsapp',
                'Slack',
                'discord',
                'obs',
            ]),
        ],
    }),
    ('sandbox', {
        'label': '9 ',
        'layout': 'columns',
        'matches': [
            Match(wm_class=[
                'VirtualBox Manage',
                'VirtualBox Machine',
            ]),
        ],
    })
]

groups = [
    *[Group(name, **kwargs) for name, kwargs in group_names],
    ScratchPad('scratchpad', [
        DropDown('term', apps.terminal, height=0.6, warp_pointer=False),
    ]),
]

for i, (name, kwargs) in enumerate(group_names, 1):
    # Switch to another group with SUPER + #
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))

# Send current window to another group SUPER + SHIFT + #
    keys.append(Key([mod, shift], str(
        i), lazy.window.togroup(name, switch_group=False)))