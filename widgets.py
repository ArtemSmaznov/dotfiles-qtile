from libqtile import widget
import socket
import os
from theme.color_scheme import colors


start_widget = widget.Image(
    filename="/usr/share/icons/Papirus-Dark/64x64/apps/distributor-logo-archlinux.svg",
    use_callbacks={'Button1': lambda qtile: qtile.cmd_spawn('chromium')}
)


def separator(size=6):
    return widget.Sep(
        linewidth=0,
        padding=size,
        foreground=colors[2],
        background=colors[0]
    )


def power_arrow(fg_color, bg_color):
    return widget.TextBox(
        text='',
        background=bg_color,
        foreground=fg_color,
        padding=0,
        fontsize=37
    )


clock = widget.Clock(
    foreground=colors[2],
    background=colors[0],
    format='%l:%M %p'
)

date = widget.Clock(
    foreground=colors[2],
    background=colors[5],
    format='%a %d %b %Y'
)

group_box = widget.GroupBox(
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
)

prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())
prompt_widget = widget.Prompt(
    prompt=prompt,
    font="Ubuntu Mono",
    padding=10,
    foreground=colors[3],
    background=colors[1]
)

window_name = widget.WindowName(
    foreground=colors[6],
    background=colors[0],
    padding=0
)

sys_tray = widget.Systray(
    background=colors[0],
    padding=5
)

# Default widget settings
widget_defaults = dict(
    font='sans',
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()
