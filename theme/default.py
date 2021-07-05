import theme.colors.material as material
import theme.colors.sweetlove as color

# ░█▀▀░▀█▀░▀▀█░█▀▀░█▀▀
# ░▀▀█░░█░░▄▀░░█▀▀░▀▀█
# ░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀▀▀

bar_size = 24
bar_opacity = 1


# ░█▀▀░█▀█░█▀█░▀█▀░█▀▀
# ░█▀▀░█░█░█░█░░█░░▀▀█
# ░▀░░░▀▀▀░▀░▀░░▀░░▀▀▀

font_regular = "SF Pro Text Regular"
font_bold = "SF Pro Text Bold"

font_awesome = "Font Awesome 5 Free Regular"
icon_size = 14


# ░▀█▀░█▀▀░█▀█░█▀█░█▀▀
# ░░█░░█░░░█░█░█░█░▀▀█
# ░▀▀▀░▀▀▀░▀▀▀░▀░▀░▀▀▀

icons = "~/.local/share/icons/Papirus-Dark/"
distributor_logo = icons + "64x64/apps/distributor-logo-archlinux.svg"
user_icon = "~/.face"


# ░█▀▀░█▀▄░█▀█░█░█░█▀█░█▀▀
# ░█░█░█▀▄░█░█░█░█░█▀▀░▀▀█
# ░▀▀▀░▀░▀░▀▀▀░▀▀▀░▀░░░▀▀▀

# border, block, text, or line
group_highlight_method = "line"

group_icon_size = 16


# ░▀█▀░█▀█░█▀▀░█░█░█░░░▀█▀░█▀▀░▀█▀
# ░░█░░█▀█░▀▀█░█▀▄░█░░░░█░░▀▀█░░█░
# ░░▀░░▀░▀░▀▀▀░▀░▀░▀▀▀░▀▀▀░▀▀▀░░▀░

# border or block
tasklist_highlight_method = "block"

rounded_hightlights = True
tasklist_icon_size = 12


# ░█▀▀░█▀█░█░░░█▀█░█▀▄░█▀▀
# ░█░░░█░█░█░░░█░█░█▀▄░▀▀█
# ░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀░▀░▀▀▀

foreground = color.foreground
background = color.background
inactive = material.grey_800
alert = material.red_A200
warning = material.yellow_300

selection_bg = color.yellow_dark_11
selection_accent = color.red_1

other_selection_bg = color.green_dark_10
other_selection_accent = color.green_2

prompt = color.yellow_3
chord = material.yellow_300


# ░█░░░█▀█░█░█░█▀█░█░█░▀█▀░█▀▀
# ░█░░░█▀█░░█░░█░█░█░█░░█░░▀▀█
# ░▀▀▀░▀░▀░░▀░░▀▀▀░▀▀▀░░▀░░▀▀▀

global_layout = {
    "margin": 6,
    "border_width": 3,
    "border_focus": color.red_dark_9,
    "border_normal": color.black_dark_8,
    "border_focus_stack": color.green_2,
    "border_normal_stack": color.cyan_dark_14,
    "single_border_width": False,
}

float_layout = {
    "border_width": 2,
    "border_focus": color.cyan_6,
    "border_normal": color.black_dark_8,
}
