import PySimpleGUI as sg

susunan = [
    [sg.Text("UNISKA MAB", font=("helvetica", 24))],
    [sg.Text("BANJARMASIN", font=("Courier", 18))]
]

window = sg.Window(
    title="New Icon",
    layout=susunan,
    element_justification="center",  # Meratakan elemen ke tengah
    icon="favicon.ico",  # Menyisipkan ikon
    resizable=True,  # Memungkinkan ukuran jendela dapat diubah
    size=(430, 200)
)

window.read()
window.close()
