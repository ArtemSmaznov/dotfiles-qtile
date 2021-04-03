from datetime import datetime as time

from libqtile import widget

import lib.widgets as my_widget
import settings.preferences as user
import theme.default as theme

kbr_index = 0


def switch_keyboard_layout(qtile):
    global kbr_index

    if kbr_index+1 < len(user.languages):
        kbr_index = kbr_index + 1
    else:
        kbr_index = 0
    qtile.cmd_spawn('setxkbmap ' + user.languages[kbr_index])


# ░█▀█░█▀█░█░█░█▀▀░█▀▄░█░░░▀█▀░█▀█░█▀▀
# ░█▀▀░█░█░█▄█░█▀▀░█▀▄░█░░░░█░░█░█░█▀▀
# ░▀░░░▀▀▀░▀░▀░▀▀▀░▀░▀░▀▀▀░▀▀▀░▀░▀░▀▀▀


def power_line(index, w):
    index = index - 1
    is_first_iteration = True

    while index >= len(theme.power_line_colors):
        index = index - len(theme.power_line_colors)
        is_first_iteration = False

    current_color = theme.power_line_colors[index]

    if index != 0:
        previous_color = theme.power_line_colors[index - 1]
    else:
        if is_first_iteration:
            previous_color = theme.background
        else:
            previous_color = theme.power_line_colors[len(
                theme.power_line_colors) - 1]

    return [
        widget.TextBox(
            text='',
            foreground=current_color,
            background=previous_color,
            padding=-10,
            fontsize=48
        ),
        *w(current_color),
        my_widget.separator(3, current_color),
    ]


# ░█░█░█▀█░█░░░█░█░█▄█░█▀▀
# ░▀▄▀░█░█░█░░░█░█░█░█░█▀▀
# ░░▀░░▀▀▀░▀▀▀░▀▀▀░▀░▀░▀▀▀

def volume_increase(qtile):
    qtile.cmd_spawn('amixer -q sset Master on ' + str(user.volume_step) + '%+')


def volume_decrease(qtile):
    qtile.cmd_spawn('amixer -q sset Master on ' + str(user.volume_step) + '%-')


def volume_mute(qtile):
    qtile.cmd_spawn('amixer -q sset Master toggle')
