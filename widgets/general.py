import os
import socket

import apps
import preferences as user
import themes
from libqtile import lazy, qtile, widget
from preferences import dmscripts

myDMScript = os.path.expanduser(dmscripts)
prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

def separator(size=6, backround=themes.background):
    return widget.Sep(linewidth=0, padding=size, background=backround)

def start_widget():
    return widget.Image(
        filename=themes.distributor_logo,
        mouse_callbacks={
            "Button1": lambda: qtile.cmd_spawn(apps.myLauncher),
        },
    )

def profile():
    return widget.Image(
        filename=themes.user_icon,
        mouse_callbacks={
            "Button1": lambda: qtile.cmd_spawn(myDMScript + "dm-power"),
        },
    )

def prompt_widget(bg=themes.prompt, fg=themes.fg_dark):
    return widget.Prompt(
        prompt=prompt,
        font=themes.font_bold,
        padding=10,
        foreground=fg,
        background=bg,
    )

def time(bg=themes.background, fg=themes.foreground):
    return widget.Clock(
        font=themes.font_bold, foregroung=fg, background=bg, format=user.time_format
    )

def date(bg=themes.background, fg=themes.foreground):
    return [
        widget.TextBox(
            text="",
            font=themes.font_awesome,
            fontsize=themes.icon_size,
            padding_x=2,
            foreground=fg,
            background=bg,
        ),
        widget.Clock(
            font=themes.font_bold, foreground=fg, background=bg, format=user.date_format
        ),
    ]

def layout_icon(bg=themes.background, fg=themes.foreground):
    return widget.CurrentLayoutIcon(
        # custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
        foreground=fg,
        background=bg,
        scale=0.6,
        mouse_callbacks={
            "Button1": lambda: qtile.cmd_next_layout(),
            "Button2": lambda: qtile.cmd_to_layout_index(0),
            "Button3": lambda: qtile.cmd_prev_layout(),
            "Button4": lambda: qtile.cmd_next_layout(),
            "Button5": lambda: qtile.cmd_prev_layout(),
        },
    )

def group_box():
    return widget.GroupBox(
        font=themes.font_awesome,
        fontsize=themes.group_icon_size,
        margin_y=3,
        margin_x=0,
        padding_y=5,
        padding_x=3,
        borderwidth=3,
        highlight_method=themes.group_highlight_method,
        disable_drag=True,
        hide_unused=False,
        # Icon colors
        active=themes.foreground,
        inactive=themes.inactive,
        # Background colors
        highlight_color=themes.selection_bg,
        # Border colors
        this_current_screen_border=themes.selection_accent,
        this_screen_border=themes.unfocused_selection_accent,
        other_current_screen_border=themes.other_selection_accent,
        other_screen_border=themes.unfocused_other_selection_accent,
        # Border colors - alert
        urgent_border=themes.alert,
    )

def window_name(bg=themes.background, fg=themes.foreground):
    return widget.WindowName(
        font=themes.font_bold, foreground=fg, background=bg, padding=0
    )

def task_list(bg=themes.background, fg=themes.foreground):
    return widget.TaskList(
        font=themes.font_bold,
        highlight_method=themes.tasklist_highlight_method,
        border=themes.selection_bg,
        foreground=fg,
        background=bg,
        rounded=themes.rounded_hightlights,
        txt_floating=" ",
        txt_maximized=" ",
        txt_minimized=" ",
        icon_size=themes.tasklist_icon_size,
        max_title_width=150,
        padding_x=5,
        padding_y=5,
        margin=0,
    )

def notify():
    return widget.Notify(
        foreground=themes.selection_accent,
        foreground_urgent=themes.alert,
        foreground_low=themes.foreground,
    )

def keyboard_layout(bg=themes.background, fg=themes.foreground):
    return widget.KeyboardLayout(
        foreground=fg,
        background=bg,
        configured_keyboards=user.languages,
        font=themes.font_bold,
        mouse_callbacks={
            # This doesn't work
            # "Button1": lambda: lazy.widget["keyboardlayout"].next_keyboard(),
            "Button1": lambda: qtile.cmd_spawn("setxkbmap us"),
            "Button3": lambda: qtile.cmd_spawn("setxkbmap ru"),
        },
    )

def sys_tray(bg=themes.background, fg=themes.foreground):
    return widget.Systray(
        foreground=fg,
        background=bg,
    )

def updater(bg=themes.background, fg=themes.foreground):
    return [
        widget.TextBox(
            text="",
            font=themes.font_awesome,
            fontsize=themes.icon_size - 3,
            padding_x=2,
            foreground=fg,
            background=bg,
            mouse_callbacks={
                "Button1": lambda: qtile.cmd_spawn(
                    apps.myTerminal + " -e sudo pacman -Syu"
                ),
            },
        ),
        widget.CheckUpdates(
            distro="Arch_checkupdates",
            display_format="{updates}",
            no_update_string="n/a",
            update_interval="1800",
            font=themes.font_bold,
            colour_have_updates=fg,
            colour_no_updates=fg,
            background=bg,
        ),
        widget.CheckUpdates(
            distro="Arch",
            custom_command="pacman -Qu | grep -e nvidia -e linux",
            update_interval="1800",
            display_format="",
            font=themes.font_awesome,
            fontsize=themes.icon_size - 3,
            colour_have_updates=themes.alert,
            # colour_no_updates=themes.foreground,
            background=bg,
        ),
        widget.CheckUpdates(
            distro="Arch",
            custom_command="pacman -Qu | grep -e nvidia -e linux",
            update_interval="1800",
            display_format="{updates}",
            font=themes.font_bold,
            colour_have_updates=themes.alert,
            colour_no_updates=fg,
            background=bg,
        ),
    ]

def volume(bg=themes.background, fg=themes.foreground):
    return [
        widget.TextBox(
            text="",
            font=themes.font_awesome,
            fontsize=themes.icon_size,
            padding_x=2,
            foreground=fg,
            background=bg,
        ),
        widget.Volume(
            font=themes.font_bold,
            foreground=fg,
            background=bg,
            step=user.volume_step,
            mouse_callbacks={
                "Button3": lambda: qtile.cmd_spawn(apps.myCliSysAudio),
            },
        ),
    ]

def chord(bg=themes.chord, fg=themes.fg_dark):
    return widget.Chord(
        font=themes.font_bold,
        padding=10,
        foreground=fg,
        background=bg,
    )
