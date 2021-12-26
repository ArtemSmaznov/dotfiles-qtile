import os
import subprocess
from typing import List

from libqtile import hook

from groups import groups
from keys.bindings import *
from layouts import *
from screens import screens
from widgets import *

auto_fullscreen            = True
bring_front_click          = "floating_only"
cursor_warp                = False
dgroups_app_rules          = []  # type: List
focus_on_window_activation = "smart"
follow_mouse_focus         = False
reconfigure_screens        = True
auto_minimize              = True

@hook.subscribe.startup_once
def autostart():
    autostart_script = os.path.expanduser("~/.config/autostart-scripts/autostart.sh")
    subprocess.call([autostart_script])
