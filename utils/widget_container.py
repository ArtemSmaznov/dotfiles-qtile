from libqtile import widget

import preferences as user
import theme

def powerline(
    widgets=[], colors=theme.power_line_colors, separator_font=user.powerline_font
):
    separator = {
        "powerline": "",
        "nerd": "",
        "unicode": "◀",
    }
    separator_size = {
        "powerline": 23,
        "nerd": 64,
        "unicode": 28,
    }
    separator_padding = {
        "powerline": 0,
        "nerd": -14,
        "unicode": -4,
    }
    w_container = []
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
        w_container.extend(
            [
                widget.TextBox(
                    text=separator[separator_font],
                    foreground=current_color,
                    background=previous_color,
                    fontsize=separator_size[separator_font],
                    padding=separator_padding[separator_font],
                ),
                *widgets[iw](current_color, theme.fg_dark),
                widget.Sep(linewidth=0, padding=4, background=current_color),
            ]
        )

    return w_container

def colorized(widgets=[], colors=theme.power_line_colors, separator_gap=8):
    w_container = []
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
        w_container.extend(
            [
                widget.Sep(
                    linewidth=0, padding=separator_gap, background=theme.background
                ),
                *widgets[iw](theme.background, current_color),
            ]
        )

    # Create an extra gap after the widget
    w_container.extend(
        [
            widget.Sep(linewidth=0, padding=4, background=theme.background),
        ]
    )

    return w_container
