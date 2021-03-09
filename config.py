import os
import subprocess
from typing import List

from libqtile import hook

from groups import groups
from keys.bindings import keys, mouse
from layouts import floating_layout, layouts
from screens import screens
from widgets import extension_defaults, widget_defaults


#  dgroups_key_binder = None
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = False
bring_front_click = False
cursor_warp = False
dgroups_app_rules = []  # type: List
auto_fullscreen = True
focus_on_window_activation = "smart"


@ hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])


# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
