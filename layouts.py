from libqtile import layout
from libqtile.config import Key, Match
from libqtile.lazy import lazy

from keys.bindings import keys
from keys.mods import *
from theme import float_layout, global_layout

layouts = [
    layout.MonadTall(**global_layout),
    layout.Columns(**global_layout),
    layout.Tile(**global_layout),
    # layout.MonadWide(**global_layout),
    # layout.Stack(num_stacks=2),
    # layout.Matrix(),
    # layout.RatioTile(),
    # layout.TreeTab(),
    # layout.VerticalTile(**global_layout),
    # layout.Zoomy(),
    layout.Bsp(**global_layout),
    layout.Max(**global_layout),
]

# Run the utility of `xprop` to see the wm class and name of an X client.
floating_layout = layout.Floating(
    float_rules=[
        # default_float_rules include: utility, notification, toolbar, splash, dialog,
        # file_progress, confirm, download and error.
        *layout.Floating.default_float_rules,
        #  Defaults
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(title="branchdialog"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        #  Steam
        Match(wm_class="Steam", title="Friends List"),
        Match(wm_class="Steam", title="News"),
        Match(wm_class="Steam", title="Guard"),
        Match(wm_class="Steam", title="Screenshot Uploader"),
        # Match(wm_class='Steam', title='Self Updater'),
        #  Other
        Match(wm_class="Nitrogen"),
    ],
    **float_layout
)

# Only map up to 10 Layouts to number keys
def getNumberOfKeysForLayouts():
    if len(layouts) > 10:
        return 10
    else:
        return len(layouts)


# Switch to another Layout with SUPER + ALT + #
for i in range(getNumberOfKeysForLayouts()):
    key = str(i + 1)
    if i + 1 == 10:
        key = "0"

    keys.append(Key([mod, alt], key, lazy.to_layout_index(i)))

# Switch to last Layout
keys.append(Key([mod, alt], "quoteleft", lazy.to_layout_index(len(layouts) - 1)))
