import PySimpleGUI as sg

# Set the theme and text color
sg.theme("DarkGreen4")
sg.theme_text_color("#FFFF00")

# Create the window layout
layout = [
    [sg.Text("FTI UNISKA", font=("Helvetica", 24))],
    [sg.Text("FAKULTAS TEKNOLOGI INFORMASI")],
    [sg.Text("UNISKA MAB BANJARMASIN")]
]

# Create the window
window = sg.Window(
    title="Profile",
    layout=layout,
    size=(430, 200),
    font=("Times", 18)
)

# Display the window and wait for an event
window.read()
window.close()
