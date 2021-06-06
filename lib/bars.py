from libqtile import bar

from lib.powerline import powerline
import lib.widgets as widget
import theme.default as theme


def init_panel_widgets(s='main'):
    if s == 'main':
        return [
            widget.general.separator(4),
            widget.general.start_widget(),
            widget.general.separator(3),
            widget.general.prompt_widget(),
            widget.general.time(),
            widget.general.layout_icon(),
            widget.general.group_box(),

            widget.general.separator(20),
            widget.general.task_list(),
            widget.general.notify(),
            widget.general.keyboard_layout(),
            widget.general.sys_tray(),
            widget.general.separator(5),
            *powerline(
                widgets=[
                    widget.sensor.network_graph,
                    widget.sensor.memory_graph,
                    widget.sensor.thermals,
                    widget.general.volume,
                    widget.general.updater,
                    widget.general.date,
                ],
            ),
            widget.general.profile(),
        ]
    else:
        return [
            widget.general.separator(),
            widget.general.time(),
            widget.general.layout_icon(),
            widget.general.group_box(),

            widget.general.separator(40),
            widget.general.task_list(),
            *powerline(
                widgets=[
                    widget.sensor.network_graph,
                    widget.sensor.memory_graph,
                    widget.sensor.cpu_graph,
                    widget.sensor.thermals,
                    widget.general.volume,
                    widget.general.date,
                ],
            ),
        ]


def init_bar(s='main'):
    return bar.Bar(init_panel_widgets(s), theme.bar_size, background=theme.background, opacity=1)
