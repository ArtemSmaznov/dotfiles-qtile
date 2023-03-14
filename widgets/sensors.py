import themes
from libqtile import widget

def network_graph(bg=themes.background, fg=themes.foreground):
    return [
        widget.TextBox(
            text="",
            font=themes.font_awesome,
            fontsize=themes.icon_size,
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

def cpu_graph(bg=themes.background, fg=themes.foreground):
    return [
        widget.TextBox(
            text="",
            font=themes.font_awesome,
            fontsize=themes.icon_size,
            padding_x=2,
            foreground=fg,
            background=bg,
        ),
        widget.ThermalSensor(
            font=themes.font_bold,
            foreground_alert=themes.alert,
            foreground=fg,
            background=bg,
            threshold=80,
        ),
        widget.TextBox(
            text="",
            font=themes.font_awesome,
            fontsize=themes.icon_size,
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

def memory_graph(bg=themes.background, fg=themes.foreground):
    return [
        widget.TextBox(
            text="",
            font=themes.font_awesome,
            fontsize=themes.icon_size,
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

def thermals(bg=themes.background, fg=themes.foreground):
    return [
        widget.TextBox(
            text="",
            font=themes.font_awesome,
            fontsize=themes.icon_size,
            padding_x=2,
            foreground=fg,
            background=bg,
        ),
        widget.ThermalSensor(
            font=themes.font_bold,
            foreground_alert=themes.alert,
            foreground=fg,
            background=bg,
            threshold=80,
        ),
    ]

def network(bg=themes.background, fg=themes.foreground):
    return [
        widget.TextBox(
            text="",
            font=themes.font_awesome,
            fontsize=themes.icon_size,
            padding_x=2,
            foreground=fg,
            background=bg,
        ),
        widget.Net(
            font=themes.font_bold,
            interface="eno1",
            format="{down} | {up}",
            foreground=fg,
            background=bg,
            padding=5,
        ),
    ]

def memory(bg=themes.background, fg=themes.foreground):
    return [
        widget.TextBox(
            text="",
            font=themes.font_awesome,
            fontsize=themes.icon_size,
            padding_x=2,
            foreground=fg,
            background=bg,
        ),
        widget.Memory(
            font=themes.font_bold,
            foreground=fg,
            background=bg,
            measure_mem="G",
        ),
    ]

def nvidia_sensors(bg=themes.background, fg=themes.foreground):
    return [
        widget.TextBox(
            text="",
            font=themes.font_awesome,
            fontsize=themes.icon_size,
            padding_x=2,
            foreground=fg,
            background=bg,
        ),
        widget.NvidiaSensors(
            font=themes.font_bold,
            foreground_alert=themes.alert,
            foreground=fg,
            background=bg,
        ),
        widget.TextBox(
            text="",
            font=themes.font_awesome,
            fontsize=themes.icon_size,
            padding_x=2,
            foreground=fg,
            background=bg,
        ),
    ]
