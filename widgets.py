import theme.default as theme
from libqtile import widget
import socket
import os


start_widget = widget.Image(
    filename="/usr/share/icons/Papirus-Dark/64x64/apps/distributor-logo-archlinux.svg",
    use_callbacks={'Button1': lambda qtile: qtile.cmd_spawn('chromium')}
)


def separator(size=6):
    return widget.Sep(
        linewidth=0,
        padding=size,
        foreground=theme.foreground,
        background=theme.background
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
    foreground=theme.foreground,
    background=theme.background,
    format='%l:%M %p'
)

date = widget.Clock(
    foreground=theme.foreground,
    background=theme.widget_bg_2,
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
    highlight_method="line",
    disable_drag=True,

    active=theme.foreground,
    inactive=theme.inactive,
    highlight_color=theme.selection_bg,

    this_current_screen_border=theme.selection_accent,
    this_screen_border=theme.selection_accent,

    other_current_screen_border=theme.other_selection_accent,
    other_screen_border=theme.other_selection_bg,
)

prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())
prompt_widget = widget.Prompt(
    prompt=prompt,
    font="Ubuntu Mono",
    padding=10,
    foreground=theme.background,
    background=theme.inactive
)

window_name = widget.WindowName(
    foreground=theme.widget_bg_1,
    background=theme.background,
    padding=0
)

sys_tray = widget.Systray(
    background=theme.background,
    padding=5
)

# Default widget settings
widget_defaults = dict(
    font='sans',
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()
