import themes.material as material
import themes.base16 as color

# ░█▀▀░▀█▀░▀▀█░█▀▀░█▀▀
# ░▀▀█░░█░░▄▀░░█▀▀░▀▀█
# ░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀▀▀

bar_size = 24
bar_opacity = 1
gap = 14


# ░█▀▀░█▀█░█▀█░▀█▀░█▀▀
# ░█▀▀░█░█░█░█░░█░░▀▀█
# ░▀░░░▀▀▀░▀░▀░░▀░░▀▀▀

font_regular = "SF Pro Text Regular"
font_bold = "SF Pro Text Bold"

font_awesome = "Font Awesome 6 Free Solid"
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

fg_dark = color.base01
inactive = color.base02
alert = color.base08
warning = color.base0A

selection_bg = color.base03
selection_accent = color.base0A
unfocused_selection_accent = color.base0A
other_selection_accent = color.base02
unfocused_other_selection_accent = color.base03

prompt = color.base09
chord = color.base0E

power_line_colors = [
    color.base08,
    color.base0B,
    color.base0A,
    color.base0D,
    color.base0E,
    color.base0C,
]

# ░█░░░█▀█░█░█░█▀█░█░█░▀█▀░█▀▀
# ░█░░░█▀█░░█░░█░█░█░█░░█░░▀▀█
# ░▀▀▀░▀░▀░░▀░░▀▀▀░▀▀▀░░▀░░▀▀▀

global_layout = {
    "margin": gap,
    "border_width": 5,
    "border_focus": color.base0E,
    "border_normal": color.base03,
    "border_focus_stack": color.base0B,
    "border_normal_stack": color.base0C,
    "single_border_width": 5,
}

float_layout = {
    "border_width": 5,
    "border_focus": color.base0E,
    "border_normal": color.base03,
}
