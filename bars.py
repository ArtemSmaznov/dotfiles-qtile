from libqtile import bar

import theme.default as theme
import widgets as my_widget


def init_panel_widgets(s='main'):
    if s == 'main':
        return [
            my_widget.separator(),
            my_widget.start_widget(),
            my_widget.prompt_widget(),
            my_widget.time(),
            my_widget.layout_icon(),
            my_widget.group_box(),
            my_widget.separator(40),
            my_widget.window_name(),

            *my_widget.network(0),
            *my_widget.memory(1),
            *my_widget.thermals(2),
            *my_widget.volume(1),
            *my_widget.date(2),
            my_widget.separator(10, theme.widget_bg_1),
            my_widget.sys_tray(),
        ]
    else:
        return [
            my_widget.separator(),
            my_widget.layout_icon(),
            my_widget.group_box(),
            my_widget.separator(40),
            my_widget.window_name(),

            *my_widget.date(0),
            my_widget.separator(10, theme.widget_bg_1),
        ]


def init_bar(s='main'):
    return bar.Bar(init_panel_widgets(s), theme.bar_size, background=theme.background, opacity=1)
