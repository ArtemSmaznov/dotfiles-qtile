from libqtile import bar, widget
from widgets import start_widget, separator, clock, group_box, prompt_widget, window_name, power_arrow, date, sys_tray

colors = [["#282c34", "#282c34"],  # panel background
          ["#434758", "#434758"],  # background for current screen tab
          ["#ffffff", "#ffffff"],  # font color for group names
          ["#ff5555", "#ff5555"],  # border line color for current tab
          ["#8d62a9", "#8d62a9"],  # border line color for other tab and odd widgets
          ["#668bd7", "#668bd7"],  # color for the even widgets
          ["#e1acff", "#e1acff"]]  # window name


def init_panel_widgets():
    panel_widgets = [
        separator(),
        start_widget,
        clock,
        group_box,
        prompt_widget,
        separator(40),
        window_name,

        power_arrow(colors[4], colors[0]),
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
        power_arrow(colors[5], colors[4]),
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
        power_arrow(colors[4], colors[5]),
        widget.Net(
            interface="eno1",
            format='{down} ↓↑ {up}',
            foreground=colors[2],
            background=colors[4],
            padding=5
        ),
        power_arrow(colors[5], colors[4]),
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
        power_arrow(colors[4], colors[5]),
        widget.CurrentLayout(
            foreground=colors[2],
            background=colors[4],
            padding=5
        ),
        power_arrow(colors[5], colors[4]),
        date,
        widget.Sep(
            linewidth=0,
            padding=10,
            foreground=colors[0],
            background=colors[5]
        ),
        power_arrow(colors[4], colors[5]),
        widget.QuickExit(
            foreground=colors[2],
            background=colors[4]
        ),
        sys_tray,
    ]
    return panel_widgets


def init_bar():
    return bar.Bar(init_panel_widgets(), 24, background=colors[0])
