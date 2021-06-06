from libqtile import bar

from lib.powerline import powerline
import lib.widgets as widget
import theme.default as theme


def init_panel_widgets(s='main'):
    if s == 'main':
        return [
            widget.separator(4),
            widget.start_widget(),
            widget.separator(3),
            widget.prompt_widget(),
            widget.time(),
            widget.layout_icon(),
            widget.group_box(),

            widget.separator(20),
            widget.task_list(),
            widget.notify(),
            widget.keyboard_layout(),
            widget.sys_tray(),
            widget.separator(5),
            *powerline(
                widgets=[
                    widget.network_graph,
                    widget.memory_graph,
                    widget.thermals,
                    widget.volume,
                    widget.updater,
                    widget.date,
                ],
            ),
            widget.profile(),
        ]
    else:
        return [
            widget.separator(),
            widget.time(),
            widget.layout_icon(),
            widget.group_box(),

            widget.separator(40),
            widget.task_list(),
            *powerline(
                widgets=[
                    widget.network_graph,
                    widget.memory_graph,
                    widget.cpu_graph,
                    widget.thermals,
                    widget.volume,
                    widget.date,
                ],
            ),
        ]


def init_bar(s='main'):
    return bar.Bar(init_panel_widgets(s), theme.bar_size, background=theme.background, opacity=1)
