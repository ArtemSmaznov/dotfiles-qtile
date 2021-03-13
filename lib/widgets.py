import os
import socket

from libqtile import widget

import theme.default as theme


def open_app(qtile):
    qtile.cmd_spawn('xterm')


def separator(size=6, backround=theme.background):
    return widget.Sep(
        linewidth=0,
        padding=size,
        background=backround
    )


def start_widget(bg_color=theme.background):
    return widget.Image(
        filename='~/.local/share/icons/Papirus-Dark/64x64/apps/distributor-logo-archlinux.svg',
        mouse_callbacks={"Button1": open_app, },
    )


def time(bg_color=theme.background):
    return widget.Clock(
        font=theme.font_bold,
        foreground=theme.foreground,
        background=bg_color,
        format='%l:%M %p'
    )


def layout_icon(bg_color=theme.background):
    return widget.CurrentLayoutIcon(
        foreground=theme.foreground,
        background=bg_color,
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
        urgent_border=theme.foreground,

        active=theme.foreground,
        inactive=theme.inactive,
        highlight_color=theme.selection_bg,

        this_screen_border=theme.selection_bg,
        this_current_screen_border=theme.selection_accent,

        other_screen_border=theme.other_selection_bg,
        other_current_screen_border=theme.other_selection_accent,
    )


prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())


def prompt_widget(bg_color=theme.background):
    return widget.Prompt(
        prompt=prompt,
        font=theme.font_bold,
        padding=10,
        foreground=bg_color,
        background=theme.selection_bg,
    )


def window_name(bg_color=theme.background):
    return widget.WindowName(
        font=theme.font_bold,
        foreground=theme.foreground,
        background=bg_color,
        padding=0
    )


def task_list(bg_color=theme.background):
    return widget.TaskList(
        font=theme.font_bold,
        highlight_method='block',
        border=theme.other_selection_bg,
        foreground=theme.foreground,
        background=bg_color,
        max_title_width=150,
        padding_x=10,
    )


def keyboard_layout(bg_color=theme.background):
    return widget.KeyboardLayout(
        background=bg_color,
        #  layout_groups=['us', 'ru'],
    )


def sys_tray(bg_color=theme.background):
    return widget.Systray(
        background=bg_color,
        padding=5
    )


def thermals(bg_color=theme.background):
    return [
        widget.TextBox(
            text=" 🌡",
            padding=2,
            foreground=theme.foreground,
            background=bg_color,
            fontsize=11
        ),
        widget.ThermalSensor(
            font=theme.font_bold,
            foreground=theme.foreground,
            foreground_alert=theme.alert,
            background=bg_color,
            threshold=90,
        ),
    ]


def network(bg_color=theme.background):
    return [
        widget.Net(
            font=theme.font_bold,
            interface="eno1",
            format='{down} ↓↑ {up}',
            foreground=theme.foreground,
            background=bg_color,
            padding=5
        ),
    ]


def memory(bg_color=theme.background):
    return [
        widget.TextBox(
            text=" 🖬",
            foreground=theme.foreground,
            background=bg_color,
            padding=0,
            fontsize=14
        ),
        widget.Memory(
            font=theme.font_bold,
            foreground=theme.foreground,
            background=bg_color,
            measure_mem='G',
        ),
    ]


def network_graph(bg_color=theme.background):
    return [
        widget.TextBox(
            text=" ↓↑",
            foreground=theme.foreground,
            background=bg_color,
            padding=0,
            fontsize=14
        ),
        widget.NetGraph(
            interface="eno1",
            foreground=theme.foreground,
            background=bg_color,
            graph_color=theme.foreground,
            border_width=0,
        ),
    ]


def memory_graph(bg_color=theme.background):
    return [
        widget.TextBox(
            text=" 🖬",
            foreground=theme.foreground,
            background=bg_color,
            padding=0,
            fontsize=14
        ),
        widget.MemoryGraph(
            foreground=theme.foreground,
            background=bg_color,
            graph_color=theme.foreground,
            border_width=0,
        ),
    ]


def volume(bg_color=theme.background):
    return [
        widget.TextBox(
            text=" Vol:",
            foreground=theme.foreground,
            background=bg_color,
            padding=0
        ),
        widget.Volume(
            font=theme.font_bold,
            foreground=theme.foreground,
            background=bg_color,
            padding=5
        ),
    ]


def layout(bg_color=theme.background):
    return [
        widget.CurrentLayout(
            font=theme.font_bold,
            foreground=theme.foreground,
            background=bg_color,
        ),
    ]


def date(bg_color=theme.background):
    return [
        widget.Clock(
            font=theme.font_bold,
            foreground=theme.foreground,
            background=bg_color,
            format='%a, %d %b %Y'
        ),
    ]


# Default widget settings
widget_defaults = dict(
    font=theme.font_regular,
    fontsize=11,
    padding=3,
)

extension_defaults = widget_defaults.copy()
