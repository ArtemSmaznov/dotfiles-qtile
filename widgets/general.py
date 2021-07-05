import os
import socket

import apps
import preferences as user
import theme
from libqtile import qtile, widget

prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())


# ░█░█░▀█▀░█▀▄░█▀▀░█▀▀░▀█▀░█▀▀
# ░█▄█░░█░░█░█░█░█░█▀▀░░█░░▀▀█
# ░▀░▀░▀▀▀░▀▀░░▀▀▀░▀▀▀░░▀░░▀▀▀
# Most icons taken from https://fontawesome.com/


def separator(size=6, backround=theme.background):
    return widget.Sep(linewidth=0, padding=size, background=backround)


def start_widget():
    return widget.Image(
        filename="~/.local/share/icons/Papirus-Dark/64x64/apps/distributor-logo-archlinux.svg",
        mouse_callbacks={
            "Button1": lambda: qtile.cmd_spawn(apps.launcher),
        },
    )


def profile():
    return widget.Image(
        filename="~/.face",
        mouse_callbacks={
            "Button1": lambda: qtile.cmd_spawn("./.local/bin/dmscripts/dmpower"),
        },
    )


def prompt_widget(bg_color=theme.background):
    return widget.Prompt(
        prompt=prompt,
        font=theme.font_bold,
        padding=10,
        foreground=bg_color,
        background=theme.prompt,
    )


def time(bg_color=theme.background):
    return widget.Clock(font=theme.font_bold, background=bg_color, format="%l:%M %p")


def layout():
    return [
        widget.CurrentLayout(
            font=theme.font_bold,
        ),
    ]


def layout_icon(bg_color=theme.background):
    return widget.CurrentLayoutIcon(
        background=bg_color,
        scale=0.6,
    )


def group_box():
    return widget.GroupBox(
        font=theme.font_awesome,
        fontsize=theme.group_icon_size,
        margin_y=3,
        margin_x=0,
        padding_y=5,
        padding_x=3,
        borderwidth=3,
        highlight_method="line",
        disable_drag=True,
        hide_unused=False,
        # Icon colors
        active=theme.foreground,
        inactive=theme.inactive,
        # Background colors
        highlight_color=theme.selection_bg,
        # Border colors - active screen
        this_current_screen_border=theme.foreground,
        other_screen_border=theme.other_selection_bg,
        # Border colors - inactive screen
        other_current_screen_border=theme.other_selection_accent,
        this_screen_border=theme.selection_bg,
        # Border colors - alert
        urgent_border=theme.alert,
    )


def window_name(bg_color=theme.background):
    return widget.WindowName(font=theme.font_bold, background=bg_color, padding=0)


def task_list(bg_color=theme.background):
    return widget.TaskList(
        font=theme.font_bold,
        highlight_method="block",
        border=theme.selection_bg,
        background=bg_color,
        rounded=False,
        txt_floating=" ",
        txt_maximized=" ",
        txt_minimized=" ",
        icon_size=12,
        max_title_width=150,
        padding_x=5,
        padding_y=5,
        margin=0,
    )


# Do not use if notifications are managed by another notificaton server such as Dunst
def notify():
    return widget.Notify(
        foreground=theme.selection_accent,
        foreground_urgent=theme.alert,
        foreground_low=theme.foreground,
    )


def keyboard_layout(bg_color=theme.background):
    return widget.KeyboardLayout(
        foreground=theme.white,
        background=bg_color,
        mouse_callbacks={
            "Button1": lambda: qtile.cmd_spawn("setxkbmap us"),
            "Button3": lambda: qtile.cmd_spawn("setxkbmap ru"),
        },
    )


def sys_tray(bg_color=theme.background):
    return widget.Systray(
        background=bg_color,
    )


# ░█▀█░█▀█░█░█░█▀▀░█▀▄░█░░░▀█▀░█▀█░█▀▀
# ░█▀▀░█░█░█▄█░█▀▀░█▀▄░█░░░░█░░█░█░█▀▀
# ░▀░░░▀▀▀░▀░▀░▀▀▀░▀░▀░▀▀▀░▀▀▀░▀░▀░▀▀▀


def updater(bg_color=theme.background):
    return [
        widget.TextBox(
            text="",
            font=theme.font_awesome,
            fontsize=theme.icon_size - 3,
            padding_x=2,
            background=bg_color,
            mouse_callbacks={
                "Button1": lambda: qtile.cmd_spawn(
                    apps.terminal + " -e sudo pacman -Syu"
                ),
            },
        ),
        widget.CheckUpdates(
            distro="Arch_checkupdates",
            display_format="{updates}",
            no_update_string="n/a",
            update_interval="1800",
            font=theme.font_bold,
            colour_have_updates=theme.foreground,
            colour_no_updates=theme.foreground,
            background=bg_color,
        ),
        widget.CheckUpdates(
            distro="Arch",
            custom_command="pacman -Qu | grep -e nvidia -e linux",
            update_interval="1800",
            display_format="",
            font=theme.font_awesome,
            fontsize=theme.icon_size - 3,
            colour_have_updates=theme.alert,
            # colour_no_updates=theme.foreground,
            background=bg_color,
        ),
        widget.CheckUpdates(
            distro="Arch",
            custom_command="pacman -Qu | grep -e nvidia -e linux",
            update_interval="1800",
            display_format="{updates}",
            font=theme.font_bold,
            colour_have_updates=theme.alert,
            colour_no_updates=theme.foreground,
            background=bg_color,
        ),
    ]


def volume(bg_color=theme.background):
    return [
        widget.TextBox(
            text="",
            font=theme.font_awesome,
            fontsize=theme.icon_size,
            padding_x=2,
            background=bg_color,
        ),
        widget.Volume(
            font=theme.font_bold,
            background=bg_color,
            step=user.volume_step,
            mouse_callbacks={
                "Button3": lambda: qtile.cmd_spawn(apps.audio_manager),
            },
        ),
    ]


def date(bg_color=theme.background):
    return [
        widget.TextBox(
            text="",
            font=theme.font_awesome,
            fontsize=theme.icon_size,
            padding_x=2,
            background=bg_color,
        ),
        widget.Clock(font=theme.font_bold, background=bg_color, format="%a, %d %b %Y"),
    ]


def chord():
    return widget.Chord(
        font=theme.font_bold,
        padding=10,
        foreground=theme.background,
        background=theme.chord,
    )
