import os
import socket

import apps
import preferences as user
import theme
from libqtile import lazy, qtile, widget
from preferences import dmscripts

dm = os.path.expanduser(dmscripts)
prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())


# ░█░█░▀█▀░█▀▄░█▀▀░█▀▀░▀█▀░█▀▀
# ░█▄█░░█░░█░█░█░█░█▀▀░░█░░▀▀█
# ░▀░▀░▀▀▀░▀▀░░▀▀▀░▀▀▀░░▀░░▀▀▀
#
# Most icons taken from https://fontawesome.com/


def separator(size=6, backround=theme.background):
    return widget.Sep(linewidth=0, padding=size, background=backround)


def start_widget():
    return widget.Image(
        filename=theme.distributor_logo,
        mouse_callbacks={
            "Button1": lambda: qtile.cmd_spawn(apps.launcher),
        },
    )


def profile():
    return widget.Image(
        filename=theme.user_icon,
        mouse_callbacks={
            "Button1": lambda: qtile.cmd_spawn(dm + "dm-power"),
        },
    )


def prompt_widget(bg=theme.prompt, fg=theme.fg_dark):
    return widget.Prompt(
        prompt=prompt,
        font=theme.font_bold,
        padding=10,
        foreground=fg,
        background=bg,
    )


def time(bg=theme.background, fg=theme.foreground):
    return widget.Clock(
        font=theme.font_bold, foregroung=fg, background=bg, format=user.time_format
    )


def date(bg=theme.background, fg=theme.foreground):
    return [
        widget.TextBox(
            text="",
            font=theme.font_awesome,
            fontsize=theme.icon_size,
            padding_x=2,
            foreground=fg,
            background=bg,
        ),
        widget.Clock(
            font=theme.font_bold, foreground=fg, background=bg, format=user.date_format
        ),
    ]


def layout_icon(bg=theme.background, fg=theme.foreground):
    return widget.CurrentLayoutIcon(
        # custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
        foreground=fg,
        background=bg,
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
        highlight_method=theme.group_highlight_method,
        disable_drag=True,
        hide_unused=False,
        # Icon colors
        active=theme.foreground,
        inactive=theme.inactive,
        # Background colors
        highlight_color=theme.selection_bg,
        # Border colors
        this_current_screen_border=theme.selection_accent,
        this_screen_border=theme.unfocused_selection_accent,
        other_current_screen_border=theme.other_selection_accent,
        other_screen_border=theme.unfocused_other_selection_accent,
        # Border colors - alert
        urgent_border=theme.alert,
    )


def window_name(bg=theme.background, fg=theme.foreground):
    return widget.WindowName(
        font=theme.font_bold, foreground=fg, background=bg, padding=0
    )


def task_list(bg=theme.background, fg=theme.foreground):
    return widget.TaskList(
        font=theme.font_bold,
        highlight_method=theme.tasklist_highlight_method,
        border=theme.selection_bg,
        foreground=fg,
        background=bg,
        rounded=theme.rounded_hightlights,
        txt_floating=" ",
        txt_maximized=" ",
        txt_minimized=" ",
        icon_size=theme.tasklist_icon_size,
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


def keyboard_layout(bg=theme.background, fg=theme.foreground):
    return widget.KeyboardLayout(
        foreground=fg,
        background=bg,
        configured_keyboards=user.languages,
        font=theme.font_bold,
        mouse_callbacks={
            # This doesn't work
            # "Button1": lambda: lazy.widget["keyboardlayout"].next_keyboard(),
            "Button1": lambda: qtile.cmd_spawn("setxkbmap us"),
            "Button3": lambda: qtile.cmd_spawn("setxkbmap ru"),
        },
    )


def sys_tray(bg=theme.background, fg=theme.foreground):
    return widget.Systray(
        foreground=fg,
        background=bg,
    )


# ░█▀█░█▀█░█░█░█▀▀░█▀▄░█░░░▀█▀░█▀█░█▀▀
# ░█▀▀░█░█░█▄█░█▀▀░█▀▄░█░░░░█░░█░█░█▀▀
# ░▀░░░▀▀▀░▀░▀░▀▀▀░▀░▀░▀▀▀░▀▀▀░▀░▀░▀▀▀


def updater(bg=theme.background, fg=theme.foreground):
    return [
        widget.TextBox(
            text="",
            font=theme.font_awesome,
            fontsize=theme.icon_size - 3,
            padding_x=2,
            foreground=fg,
            background=bg,
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
            colour_have_updates=fg,
            colour_no_updates=fg,
            background=bg,
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
            background=bg,
        ),
        widget.CheckUpdates(
            distro="Arch",
            custom_command="pacman -Qu | grep -e nvidia -e linux",
            update_interval="1800",
            display_format="{updates}",
            font=theme.font_bold,
            colour_have_updates=theme.alert,
            colour_no_updates=fg,
            background=bg,
        ),
    ]


def volume(bg=theme.background, fg=theme.foreground):
    return [
        widget.TextBox(
            text="",
            font=theme.font_awesome,
            fontsize=theme.icon_size,
            padding_x=2,
            foreground=fg,
            background=bg,
        ),
        widget.Volume(
            font=theme.font_bold,
            foreground=fg,
            background=bg,
            step=user.volume_step,
            mouse_callbacks={
                "Button3": lambda: qtile.cmd_spawn(apps.audio_manager),
            },
        ),
    ]


def chord(bg=theme.chord, fg=theme.fg_dark):
    return widget.Chord(
        font=theme.font_bold,
        padding=10,
        foreground=fg,
        background=bg,
    )
