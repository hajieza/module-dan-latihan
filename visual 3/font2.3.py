import PySimpleGUI as sg

# Setting the theme
sg.theme("DarkGreen4")
sg.theme_text_color("#FFFF00")

# Creating the window layout
layout = [
    [sg.Text("FTI UNISKA", font=("Helvetica", 24))],
    [sg.Text("FAKULTAS TEKNOLOGI INFORMASI", 
             font=("Courier", 18, "italic", "bold", "underline"))],
    [sg.Text("UNISKA MAB BANJARMASIN")]
]

# Defining the window
window = sg.Window(
    title="Profile",
    layout=layout,
    size=(430, 200),
    font=("Times", 18)
)

# Running the window
window.read()
window.close()
