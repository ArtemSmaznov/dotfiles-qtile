from libqtile import widget

import theme.default as theme


def powerline(
    widgets=[],
    colors=theme.power_line_colors,
    separator='',
    separator_size=48,
    separator_padding=-10,
):

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
                text=separator,
                foreground=current_color,
                background=previous_color,
                fontsize=separator_size,
                padding=separator_padding,
            ),
            *widgets[iw](current_color)
        ])

    return power_line
