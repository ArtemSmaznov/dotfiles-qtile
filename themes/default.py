import themes.colors.material as material
import themes.colors.sweetlove as scheme

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
group_icon_size = 16


# ░█▀▀░█▀█░█░░░█▀█░█▀▄░█▀▀
# ░█░░░█░█░█░░░█░█░█▀▄░▀▀█
# ░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀░▀░▀▀▀

foreground = scheme.foreground
background = scheme.background
inactive = material.grey_800

alert = material.red_A200
warning = material.yellow_300

white = material.grey_50

selection_accent = scheme.color1  # red
selection_bg = scheme.color11  # yellow darker

other_selection_accent = scheme.color2  # green
other_selection_bg = scheme.color10  # green darker

prompt = scheme.color3
chord = material.yellow_300

power_line_colors = [
    # scheme.color9, # red darker
    # scheme.color10, # green darker
    # scheme.color11, # yellow darker
    scheme.color12,  # blue darker
    scheme.color13,  # magenta darker
    scheme.color14,  # cyan darker
]


# ░█░░░█▀█░█░█░█▀█░█░█░▀█▀░█▀▀
# ░█░░░█▀█░░█░░█░█░█░█░░█░░▀▀█
# ░▀▀▀░▀░▀░░▀░░▀▀▀░▀▀▀░░▀░░▀▀▀

global_layout = {
    "margin": 6,
    "border_width": 3,
    "border_focus": scheme.color9,
    "border_normal": scheme.color8,
    "border_focus_stack": scheme.color2,
    "border_normal_stack": scheme.color14,
    "single_border_width": False,
}

float_layout = {
    "border_width": 2,
    "border_focus": scheme.color6,
    "border_normal": scheme.color8,
}
