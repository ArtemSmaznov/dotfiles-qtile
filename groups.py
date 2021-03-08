from libqtile.config import Group, Key
from libqtile.lazy import lazy

from keys.mods import mod, shift
from bindings import keys

group_names = [("Web", {'layout': 'columns'}),
               ("Game", {'layout': 'columns'}),
               ("Dev", {'layout': 'columns'}),
               ("PC", {'layout': 'columns'}),
               ("Mus", {'layout': 'columns'}),
               ("Vid", {'layout': 'columns'}),
               ("Misc", {'layout': 'columns'}),
               ("Gfx", {'layout': 'columns'}),
               ("Vbox", {'layout': 'columns'})]

groups = [Group(name, **kwargs) for name, kwargs in group_names]

for i, (name, kwargs) in enumerate(group_names, 1):
    # Switch to another group with SUPER + #
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))
    # Send current window to another group SUPER + SHIFT + #
    keys.append(Key([mod, shift], str(
        i), lazy.window.togroup(name, switch_group=False)))
