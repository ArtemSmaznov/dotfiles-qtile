from libqtile import bar, widget
import widgets as my_widget
from theme.color_scheme import colors


def init_panel_widgets():
    panel_widgets = [
        my_widget.separator(),
        my_widget.start_widget,
        my_widget.clock,
        my_widget.group_box,
        my_widget.prompt_widget,
        my_widget.separator(40),
        my_widget.window_name,

        my_widget.power_arrow(colors[4], colors[0]),
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
        my_widget.power_arrow(colors[5], colors[4]),
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
        my_widget.power_arrow(colors[4], colors[5]),
        widget.Net(
            interface="eno1",
            format='{down} ↓↑ {up}',
            foreground=colors[2],
            background=colors[4],
            padding=5
        ),
        my_widget.power_arrow(colors[5], colors[4]),
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
        my_widget.power_arrow(colors[4], colors[5]),
        widget.CurrentLayout(
            foreground=colors[2],
            background=colors[4],
            padding=5
        ),
        my_widget.power_arrow(colors[5], colors[4]),
        my_widget.date,
        widget.Sep(
            linewidth=0,
            padding=10,
            foreground=colors[0],
            background=colors[5]
        ),
        my_widget.power_arrow(colors[4], colors[5]),
        widget.QuickExit(
            foreground=colors[2],
            background=colors[4]
        ),
        my_widget.sys_tray,
    ]
    return panel_widgets


def init_bar():
    return bar.Bar(init_panel_widgets(), 24, background=colors[0])
