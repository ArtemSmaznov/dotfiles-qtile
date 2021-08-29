import theme.colors.material as material
import theme.colors.gruvbox as color

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

fg_dark = color.bg1
inactive = color.bg2
# inactive = material.grey_800
alert = material.red_A200
warning = material.yellow_300

selection_bg = color.bg3
selection_accent = color.yellow11
unfocused_selection_accent = color.yellow3
other_selection_accent = color.bg2
unfocused_other_selection_accent = color.bg4

prompt = color.orange16
chord = color.orange17


# ░█░░░█▀█░█░█░█▀█░█░█░▀█▀░█▀▀
# ░█░░░█▀█░░█░░█░█░█░█░░█░░▀▀█
# ░▀▀▀░▀░▀░░▀░░▀▀▀░▀▀▀░░▀░░▀▀▀

global_layout = {
    "margin": 10,
    "border_width": 3,
    "border_focus": color.red9,
    "border_normal": color.gray8,
    "border_focus_stack": color.green10,
    "border_normal_stack": color.cyan6,
    "single_border_width": False,
}

float_layout = {
    "border_width": 3,
    "border_focus": color.orange16,
    "border_normal": color.gray8,
}
