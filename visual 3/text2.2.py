import PySimpleGUI as sg

# Set the theme and text color
sg.theme("DarkGreen4")  # Determine the theme
sg.theme_text_color("#FFFF00")

# Create the window layout
layout = [
    [sg.Text("TEKNOLOGI INFORMASI", size=(25, 1), justification="center")],
    [sg.Text("TEKNOLOGI INFORMASI", size=(25, 1), justification="left")],
    [sg.Text("TEKNOLOGI INFORMASI", size=(25, 1), justification="right")],
    [sg.Text("TEKNOLOGI INFORMASI + ' '", size=(25, 2), justification="center")],
    [sg.Text("UNISKA MAB BANJARMASIN", text_color="#FFCC00")]
]

# Create the window
window = sg.Window(
    title="Profile",
    layout=layout,
    size=(400, 250),
    font=("Times", 18)
)

# Display the window and wait for an event
window.read()
window.close()
