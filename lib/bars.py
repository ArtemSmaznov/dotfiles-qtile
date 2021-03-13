from libqtile import bar

import theme.default as theme
import lib.widgets as my_widget
from utils import power_line


def init_panel_widgets(s='main'):
    if s == 'main':
        return [
            my_widget.separator(4),
            my_widget.start_widget(),
            my_widget.separator(3),
            my_widget.prompt_widget(),
            my_widget.time(),
            my_widget.layout_icon(),
            my_widget.group_box(),

            my_widget.separator(20),
            my_widget.task_list(),
            my_widget.keyboard_layout(),
            my_widget.sys_tray(),
            my_widget.separator(5),
            *power_line(1, my_widget.network_graph),
            *power_line(2, my_widget.memory_graph),
            *power_line(3, my_widget.thermals),
            *power_line(4, my_widget.updater),
            *power_line(5, my_widget.volume),
            *power_line(6, my_widget.date),
        ]
    else:
        return [
            my_widget.separator(),
            my_widget.time(),
            my_widget.layout_icon(),
            my_widget.group_box(),

            my_widget.separator(40),
            my_widget.task_list(),
            *power_line(1, my_widget.network),
            *power_line(2, my_widget.memory_graph),
            *power_line(3, my_widget.thermals),
            *power_line(4, my_widget.date),
        ]


def init_bar(s='main'):
    return bar.Bar(init_panel_widgets(s), theme.bar_size, background=theme.background, opacity=1)
