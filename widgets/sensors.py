import theme
from libqtile import widget

def network_graph(bg=theme.background, fg=theme.foreground):
    return [
        widget.TextBox(
            text="",
            font=theme.font_awesome,
            fontsize=theme.icon_size,
            padding_x=2,
            foreground=fg,
            background=bg,
        ),
        widget.NetGraph(
            interface="eno1",
            border_width=0,
            samples=95,
            line_width=2,
            graph_color=fg,
            fill_color="{}.5".format(fg),
            background=bg,
        ),
    ]

def cpu_graph(bg=theme.background, fg=theme.foreground):
    return [
        widget.TextBox(
            text="",
            font=theme.font_awesome,
            fontsize=theme.icon_size,
            padding_x=2,
            foreground=fg,
            background=bg,
        ),
        widget.ThermalSensor(
            font=theme.font_bold,
            foreground_alert=theme.alert,
            foreground=fg,
            background=bg,
            threshold=80,
        ),
        widget.TextBox(
            text="",
            font=theme.font_awesome,
            fontsize=theme.icon_size,
            padding_x=2,
            foreground=fg,
            background=bg,
        ),
        widget.CPUGraph(
            border_width=0,
            samples=95,
            line_width=2,
            graph_color=fg,
            fill_color="{}.5".format(fg),
            background=bg,
        ),
    ]

def memory_graph(bg=theme.background, fg=theme.foreground):
    return [
        widget.TextBox(
            text="",
            font=theme.font_awesome,
            fontsize=theme.icon_size,
            padding_x=2,
            foreground=fg,
            background=bg,
        ),
        widget.MemoryGraph(
            border_width=0,
            samples=95,
            line_width=2,
            graph_color=fg,
            fill_color="{}.5".format(fg),
            background=bg,
        ),
    ]

def thermals(bg=theme.background, fg=theme.foreground):
    return [
        widget.TextBox(
            text="",
            font=theme.font_awesome,
            fontsize=theme.icon_size,
            padding_x=2,
            foreground=fg,
            background=bg,
        ),
        widget.ThermalSensor(
            font=theme.font_bold,
            foreground_alert=theme.alert,
            foreground=fg,
            background=bg,
            threshold=80,
        ),
    ]

def network(bg=theme.background, fg=theme.foreground):
    return [
        widget.TextBox(
            text="",
            font=theme.font_awesome,
            fontsize=theme.icon_size,
            padding_x=2,
            foreground=fg,
            background=bg,
        ),
        widget.Net(
            font=theme.font_bold,
            interface="eno1",
            format="{down} | {up}",
            foreground=fg,
            background=bg,
            padding=5,
        ),
    ]

def memory(bg=theme.background, fg=theme.foreground):
    return [
        widget.TextBox(
            text="",
            font=theme.font_awesome,
            fontsize=theme.icon_size,
            padding_x=2,
            foreground=fg,
            background=bg,
        ),
        widget.Memory(
            font=theme.font_bold,
            foreground=fg,
            background=bg,
            measure_mem="G",
        ),
    ]

def nvidia_sensors(bg=theme.background, fg=theme.foreground):
    return [
        widget.TextBox(
            text="",
            font=theme.font_awesome,
            fontsize=theme.icon_size,
            padding_x=2,
            foreground=fg,
            background=bg,
        ),
        widget.NvidiaSensors(
            font=theme.font_bold,
            foreground_alert=theme.alert,
            foreground=fg,
            background=bg,
        ),
        widget.TextBox(
            text="",
            font=theme.font_awesome,
            fontsize=theme.icon_size,
            padding_x=2,
            foreground=fg,
            background=bg,
        ),
    ]
