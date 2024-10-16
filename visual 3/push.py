import PySimpleGUI as sg

# Create the layout with Push elements for alignment
susunan = [
    [sg.Push(), sg.Text("UNISKA MAAB", font=("Helvetica", 24)), sg.Push()],
    [sg.Push(), sg.Text("BANJARMASIN", font=("Courier", 18)), sg.Push()]
]

# Create the window
window = sg.Window(
    title="Elemen Text",
    layout=susunan,
    size=(430, 200)
)

# Display the window and wait for an event
window.read()
window.close()
