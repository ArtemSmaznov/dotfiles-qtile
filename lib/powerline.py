from libqtile import widget

import settings.preferences as user
import theme.default as theme


def powerline(
    widgets=[],
    colors=theme.power_line_colors,
    separator_font=user.powerline_font
):

    separator = {
        'powerline': '',
        'nerd': '',
        'unicode': '◀',
    }

    separator_size = {
        'powerline': 23,
        'nerd': 64,
        'unicode': 28,
    }

    separator_padding = {
        'powerline': 0,
        'nerd': -14,
        'unicode': -4,
    }

    power_line = []
    is_first_color_iteration = True

    for iw in range(len(widgets)):
        # Generate a looping color index
        ic = iw
        while ic >= len(colors):
            ic = ic - len(colors)
            is_first_color_iteration = False

        # Set the background color for the current segment
        current_color = colors[ic]

        # Set the background color for the preceding segment
        if ic != 0:
            previous_color = colors[ic - 1]
        else:
            if is_first_color_iteration:
                previous_color = theme.background
            else:
                previous_color = colors[len(colors) - 1]

        # Create a segment
        power_line.extend([
            widget.TextBox(
                text=separator[separator_font],
                foreground=current_color,
                background=previous_color,
                fontsize=separator_size[separator_font],
                padding=separator_padding[separator_font],
            ),
            *widgets[iw](current_color),
            widget.Sep(
                linewidth=0,
                padding=4,
                background=current_color
            )
        ])

    return power_line
