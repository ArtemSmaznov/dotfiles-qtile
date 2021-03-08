from typing import List  # noqa: F401

from libqtile import bar, widget, hook
from libqtile.config import Screen
import os
import socket
import subprocess

from bindings import mouse
from groups import groups, keys
from layouts import layouts, floating_layout

colors = [["#282c34", "#282c34"],  # panel background
          ["#434758", "#434758"],  # background for current screen tab
          ["#ffffff", "#ffffff"],  # font color for group names
          ["#ff5555", "#ff5555"],  # border line color for current tab
          ["#8d62a9", "#8d62a9"],  # border line color for other tab and odd widgets
          ["#668bd7", "#668bd7"],  # color for the even widgets
          ["#e1acff", "#e1acff"]]  # window name

prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

# Default widget settings
widget_defaults = dict(
    font='sans',
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()


def arch_logo():
    return widget.Image(
        filename="/usr/share/icons/Papirus-Dark/64x64/apps/distributor-logo-archlinux.svg",
        use_callbacks={'Button1': lambda qtile: qtile.cmd_spawn('chromium')}
    )


def init_panel_widgets():
    panel_widgets = [
        widget.Sep(
            linewidth=0,
            padding=6,
            foreground=colors[2],
            background=colors[0]
        ),
        arch_logo(),
        widget.Clock(
            foreground=colors[2],
            background=colors[0],
            format='%l:%M %p'
        ),
        widget.GroupBox(
            font="Ubuntu Bold",
            fontsize=11,
            margin_y=3,
            margin_x=0,
            padding_y=5,
            padding_x=3,
            borderwidth=3,
            active=colors[2],
            inactive=colors[2],
            rounded=False,
            highlight_color=colors[1],
            highlight_method="line",
            this_current_screen_border=colors[3],
            this_screen_border=colors[3],
            other_current_screen_border=colors[1],
            other_screen_border=colors[1],
            foreground=colors[2],
            background=colors[0]
        ),
        widget.Prompt(
            prompt=prompt,
            font="Ubuntu Mono",
            padding=10,
            foreground=colors[3],
            background=colors[1]
        ),
        widget.Sep(
            linewidth=0,
            padding=40,
            foreground=colors[2],
            background=colors[0]
        ),
        widget.WindowName(
            foreground=colors[6],
            background=colors[0],
            padding=0
        ),



        widget.TextBox(
            text='',
            background=colors[0],
            foreground=colors[4],
            padding=0,
            fontsize=37
        ),
        widget.TextBox(
            text=" 🌡",
            padding=2,
            foreground=colors[2],
            background=colors[4],
            fontsize=11
        ),
        widget.ThermalSensor(
            foreground=colors[2],
            background=colors[4],
            threshold=90,
            padding=5
        ),
        widget.TextBox(
            text='',
            background=colors[4],
            foreground=colors[5],
            padding=0,
            fontsize=37
        ),
        widget.TextBox(
            text=" 🖬",
            foreground=colors[2],
            background=colors[5],
            padding=0,
            fontsize=14
        ),
        widget.Memory(
            foreground=colors[2],
            background=colors[5],
            padding=5
        ),
        widget.TextBox(
            text='',
            background=colors[5],
            foreground=colors[4],
            padding=0,
            fontsize=37
        ),
        widget.Net(
            interface="eno1",
            format='{down} ↓↑ {up}',
            foreground=colors[2],
            background=colors[4],
            padding=5
        ),
        widget.TextBox(
            text='',
            background=colors[4],
            foreground=colors[5],
            padding=0,
            fontsize=37
        ),
        widget.TextBox(
            text=" Vol:",
            foreground=colors[2],
            background=colors[5],
            padding=0
        ),
        widget.Volume(
            foreground=colors[2],
            background=colors[5],
            padding=5
        ),
        widget.TextBox(
            text='',
            background=colors[5],
            foreground=colors[4],
            padding=0,
            fontsize=37
        ),
        widget.CurrentLayout(
            foreground=colors[2],
            background=colors[4],
            padding=5
        ),
        widget.TextBox(
            text='',
            background=colors[4],
            foreground=colors[5],
            padding=0,
            fontsize=37
        ),
        widget.Clock(
            foreground=colors[2],
            background=colors[5],
            format='%a %d %b %Y'
        ),
        widget.Sep(
            linewidth=0,
            padding=10,
            foreground=colors[0],
            background=colors[5]
        ),
        widget.TextBox(
            text='',
            background=colors[5],
            foreground=colors[4],
            padding=0,
            fontsize=37
        ),
        widget.QuickExit(
            foreground=colors[2],
            background=colors[4]
        ),
        widget.Systray(
            background=colors[0],
            padding=5
        ),
    ]
    return panel_widgets


screens = [
    Screen(
        top=bar.Bar(init_panel_widgets(), 24, background=colors[0]),
    ),
    Screen(top=bar.Bar(init_panel_widgets(), 24, background=colors[0])),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = False
bring_front_click = False
cursor_warp = False

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
