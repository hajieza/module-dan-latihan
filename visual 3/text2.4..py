import PySimpleGUI as sg

# Set the theme and text color
sg.theme("DarkGreen4")  # Determine the theme
sg.theme_text_color("#FFFF00")

# Create the window layout
layout = [
    [sg.Text("FTI UNISKA", font=("Helvetica", 24), text_color="#FFFFFF")],
    [sg.Text("FAKULTAS TEKNOLOGI INFORMASI", font=("Courier", 18, "italic", "bold", "underline"))],
    [sg.Text("UNISKA MAB BANJARMASIN", text_color="#FFCC00")]
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
