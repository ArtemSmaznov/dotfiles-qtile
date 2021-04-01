from libqtile import layout
from libqtile.config import Match

import theme.default as theme

layout_theme = {"border_width": 3,
                "margin": theme.app_gap,
                "border_focus_stack": '#d75f5f'
                }

layouts = [
    layout.Columns(**layout_theme),
    layout.Max(**layout_theme),
    layout.MonadTall(**layout_theme),
    #  layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    #  layout.Tile(**layout_theme),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

# Run the utility of `xprop` to see the wm class and name of an X client.
floating_layout = layout.Floating(float_rules=[
    # default_float_rules include: utility, notification, toolbar, splash, dialog,
    # file_progress, confirm, download and error.
    *layout.Floating.default_float_rules,
    #  Defaults
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry

    #  Steam
    Match(title='Friends List'),
    Match(wm_class='Steam', title='News'),
    # Match(wm_class='Steam', title='Self Updater'),

    #  Other
    Match(wm_class='Nitrogen'),
])
