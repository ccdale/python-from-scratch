import PySimpleGUI as sg

from hublogs.hlwatch import getHubLogs

sg.theme("DarkGreen")  # Add a touch of color

# All the stuff inside your window.
layout = [
    [sg.Text("Waiting for hub id to appear on clipboard.")],
    [sg.Text("Select the hub id from the FLST display.")],
    [sg.Button("Cancel")],
]

# Create the Window
window = sg.Window("Hublog Downloader", layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if (
        event == sg.WIN_CLOSED or event == "Cancel"
    ):  # if user closes window or clicks cancel
        break

window.close()
