import PySimpleGUI as sg

sg.theme("DarkGreen4")  # Mengatur tema jendela
sg.theme_text_color("#FFFF00")  # Mengatur warna teks

layout = [
    [sg.Text("Contoh Button")],
    [sg.Button("Button Simpan"), sg.Button("Button Keluar")]
]

window = sg.Window(
    title="Contoh Button",
    layout=layout,
    size=(400, 200),
    font=("Times", 18)
)

kejadian, nilai = window.read()  # Mengambil kejadian dan nilai dari interaksi pengguna
print(kejadian, "=>", nilai)  # Mencetak kejadian dan nilai
window.close()  # Menutup jendela
