from libqtile import widget

import theme.default as theme
import widgets as my_widget


def power_line(position, w):
    current_color = theme.power_line_colors[position]
    next_color = theme.power_line_colors[position - 1]
    return [
        widget.TextBox(
            text='',
            foreground=current_color,
            background=next_color,
            padding=-10,
            fontsize=48
        ),
        *w(current_color),
        my_widget.separator(3, current_color),
    ]
