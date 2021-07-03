from libqtile import bar

from lib.powerline import powerline
import lib.widgets as widget
import theme.default as theme


def primary_bar():
    return [
        widget.general.separator(4),
        widget.general.start_widget(),
        widget.general.separator(2),
        widget.general.prompt_widget(),
        widget.general.chord(),
        widget.general.separator(4),
        widget.general.time(),
        widget.general.layout_icon(),
        widget.general.group_box(),
        widget.general.separator(20),
        widget.general.task_list(),
        # widget.general.notify(),
        widget.general.keyboard_layout(),
        widget.general.sys_tray(),
        widget.general.separator(5),
        *powerline(
            widgets=[
                widget.sensor.thermals,
                widget.sensor.network_graph,
                widget.sensor.memory_graph,
                widget.general.volume,
                widget.general.updater,
                widget.general.date,
            ],
        ),
        widget.general.profile(),
    ]


def secondary_bar():
    return [
        widget.general.separator(),
        widget.general.time(),
        widget.general.layout_icon(),
        widget.general.group_box(),
        widget.general.separator(40),
        widget.general.task_list(),
        *powerline(
            widgets=[
                widget.sensor.thermals,
                widget.sensor.network_graph,
                widget.sensor.memory_graph,
                widget.sensor.cpu_graph,
                widget.general.volume,
                widget.general.date,
            ],
        ),
    ]


def init_bar(s="secondary"):
    if s == "primary":
        my_bar = primary_bar()
    elif s == "secondary":
        my_bar = secondary_bar()
    else:
        my_bar = secondary_bar()

    return bar.Bar(
        my_bar, theme.bar_size, background=theme.background, opacity=theme.bar_opacity
    )
