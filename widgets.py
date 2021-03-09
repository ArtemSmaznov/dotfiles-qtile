import os
import socket

from libqtile import widget

import theme.default as theme


def start_widget():
    return widget.Image(
        filename="~/.local/share/icons/Papirus-Dark/64x64/apps/distributor-logo-archlinux.svg",
        use_callbacks={'Button1': lambda qtile: qtile.cmd_spawn('chromium')}
    )


def separator(size=6, backround=theme.background):
    return widget.Sep(
        linewidth=0,
        padding=size,
        background=backround
    )


def time():
    return widget.Clock(
        font=theme.font_bold,
        foreground=theme.foreground,
        background=theme.background,
        format='%l:%M %p'
    )


def layout_icon():
    return widget.CurrentLayoutIcon(
        foreground=theme.foreground,
        background=theme.background,
        scale=0.6,
    )


def group_box():
    return widget.GroupBox(
        font="Ubuntu Bold",
        fontsize=11,
        margin_y=3,
        margin_x=0,
        padding_y=5,
        padding_x=3,
        borderwidth=3,
        highlight_method="line",
        disable_drag=True,
        hide_unused=False,

        active=theme.foreground,
        inactive=theme.inactive,
        highlight_color=theme.selection_bg,

        this_screen_border=theme.selection_bg,
        this_current_screen_border=theme.selection_accent,

        other_screen_border=theme.other_selection_bg,
        other_current_screen_border=theme.other_selection_accent,
    )


def current_screenA():
    return widget.CurrentScreen()


prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())


def prompt_widget():
    return widget.Prompt(
        prompt=prompt,
        font=theme.font_bold,
        padding=10,
        foreground=theme.foreground,
        background=theme.selection_bg,
    )


def window_name():
    return widget.WindowName(
        font=theme.font_bold,
        foreground=theme.foreground,
        background=theme.background,
        padding=0
    )


def sys_tray():
    return widget.Systray(
        background=theme.background,
        padding=5
    )


# Default widget settings
widget_defaults = dict(
    font=theme.font_regular,
    fontsize=11,
    padding=3,
)


def power_arrow(colors):
    if colors == 0:
        fg = theme.widget_bg_1
        bg = theme.background
        pass
    elif colors == 1:
        fg = theme.widget_bg_2
        bg = theme.widget_bg_1
        pass
    elif colors == 2:
        fg = theme.widget_bg_1
        bg = theme.widget_bg_2
        pass
    else:
        fg = theme.widget_bg_2
        bg = theme.background
        pass

    return widget.TextBox(
        text='',
        background=bg,
        foreground=fg,
        padding=-10,
        fontsize=48
    )


def thermals(position):
    return [
        power_arrow(position),
        widget.TextBox(
            text=" 🌡",
            padding=2,
            foreground=theme.foreground,
            background=theme.widget_bg_1,
            fontsize=11
        ),
        widget.ThermalSensor(
            foreground=theme.foreground,
            background=theme.widget_bg_1,
            threshold=90,
            padding=5
        ),
    ]


def memory(position):
    return [
        power_arrow(position),
        widget.TextBox(
            text=" 🖬",
            foreground=theme.foreground,
            background=theme.widget_bg_2,
            padding=0,
            fontsize=14
        ),
        widget.MemoryGraph(
            foreground=theme.foreground,
            background=theme.widget_bg_2,
            graph_color=theme.foreground,
            border_width=0,
        ),
    ]


def network(position):
    return [
        power_arrow(position),
        widget.Net(
            font=theme.font_bold,
            interface="eno1",
            format='{down} ↓↑ {up}',
            foreground=theme.foreground,
            background=theme.widget_bg_1,
            padding=5
        ),
    ]


def volume(position):
    return [
        power_arrow(position),
        widget.TextBox(
            text=" Vol:",
            foreground=theme.foreground,
            background=theme.widget_bg_2,
            padding=0
        ),
        widget.Volume(
            font=theme.font_bold,
            foreground=theme.foreground,
            background=theme.widget_bg_2,
            padding=5
        ),
    ]


def layout(position):
    return [
        power_arrow(position),
        widget.CurrentLayout(
            font=theme.font_bold,
            foreground=theme.foreground,
            background=theme.widget_bg_1,
        ),
    ]


def date(position):
    return [
        power_arrow(position),
        widget.Clock(
            font=theme.font_bold,
            foreground=theme.foreground,
            background=theme.widget_bg_1,
            format='%a, %d %b %Y'
        ),
    ]


extension_defaults = widget_defaults.copy()
