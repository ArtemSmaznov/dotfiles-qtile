import themes.default as theme
from libqtile import widget

# ░█▀▀░█▀▄░█▀█░█▀█░█░█
# ░█░█░█▀▄░█▀█░█▀▀░█▀█
# ░▀▀▀░▀░▀░▀░▀░▀░░░▀░▀


def network_graph(bg_color=theme.background):
    return [
        widget.TextBox(
            text="",
            font=theme.font_awesome,
            fontsize=theme.icon_size,
            padding_x=2,
            background=bg_color,
        ),
        widget.NetGraph(
            interface="eno1",
            border_width=0,
            samples=95,
            line_width=2,
            graph_color=theme.foreground,
            fill_color="{}.5".format(theme.foreground),
            background=bg_color,
        ),
    ]


def cpu_graph(bg_color=theme.background):
    return [
        widget.TextBox(
            text="",
            font=theme.font_awesome,
            fontsize=theme.icon_size,
            padding_x=2,
            background=bg_color,
        ),
        widget.CPUGraph(
            border_width=0,
            samples=95,
            line_width=2,
            graph_color=theme.foreground,
            fill_color="{}.5".format(theme.foreground),
            background=bg_color,
        ),
    ]


def memory_graph(bg_color=theme.background):
    return [
        widget.TextBox(
            text="",
            font=theme.font_awesome,
            fontsize=theme.icon_size,
            padding_x=2,
            background=bg_color,
        ),
        widget.MemoryGraph(
            border_width=0,
            samples=95,
            line_width=2,
            graph_color=theme.foreground,
            fill_color="{}.5".format(theme.foreground),
            background=bg_color,
        ),
    ]


# ░█▄█░█▀▀░▀█▀░█▀▄░▀█▀░█▀▀
# ░█░█░█▀▀░░█░░█▀▄░░█░░█░░
# ░▀░▀░▀▀▀░░▀░░▀░▀░▀▀▀░▀▀▀


def thermals(bg_color=theme.background):
    return [
        widget.TextBox(
            text="",
            font=theme.font_awesome,
            fontsize=theme.icon_size,
            padding_x=2,
            background=bg_color,
        ),
        widget.ThermalSensor(
            font=theme.font_bold,
            foreground=theme.foreground,
            foreground_alert=theme.alert,
            background=bg_color,
            threshold=80,
        ),
    ]


def network(bg_color=theme.background):
    return [
        widget.TextBox(
            text="",
            font=theme.font_awesome,
            fontsize=theme.icon_size,
            padding_x=2,
            background=bg_color,
        ),
        widget.Net(
            font=theme.font_bold,
            interface="eno1",
            format="{down} | {up}",
            background=bg_color,
            padding=5,
        ),
    ]


def memory(bg_color=theme.background):
    return [
        widget.TextBox(
            text="",
            font=theme.font_awesome,
            fontsize=theme.icon_size,
            padding_x=2,
            background=bg_color,
        ),
        widget.Memory(
            font=theme.font_bold,
            background=bg_color,
            measure_mem="G",
        ),
    ]
