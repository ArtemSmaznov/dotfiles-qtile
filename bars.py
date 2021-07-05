from libqtile import bar

import theme
import widgets
from utils.powerline import powerline


def primary_bar():
    return [
        widgets.general.separator(4),
        widgets.general.start_widget(),
        widgets.general.separator(2),
        widgets.general.prompt_widget(),
        widgets.general.chord(),
        widgets.general.separator(4),
        widgets.general.time(),
        widgets.general.layout_icon(),
        widgets.general.group_box(),
        widgets.general.separator(20),
        widgets.general.task_list(),
        # widget.general.notify(),
        widgets.general.keyboard_layout(),
        widgets.general.sys_tray(),
        widgets.general.separator(5),
        *powerline(
            widgets=[
                widgets.sensor.thermals,
                widgets.sensor.network_graph,
                widgets.sensor.memory_graph,
                widgets.general.volume,
                widgets.general.updater,
                widgets.general.date,
            ],
        ),
        widgets.general.profile(),
    ]


def secondary_bar():
    return [
        widgets.general.separator(),
        widgets.general.time(),
        widgets.general.layout_icon(),
        widgets.general.group_box(),
        widgets.general.separator(40),
        widgets.general.task_list(),
        *powerline(
            widgets=[
                widgets.sensor.thermals,
                widgets.sensor.network_graph,
                widgets.sensor.memory_graph,
                widgets.sensor.cpu_graph,
                widgets.general.volume,
                widgets.general.date,
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
