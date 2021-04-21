import queue
import threading

import PySimpleGUI as sg

from hublogs.hlwatch import watchClipboard
from hublogs.hlwatch import watchCBGui


sg.theme("DarkGreen")  # Add a touch of color

# All the stuff inside your window.
layout = [
    [
        sg.Text(
            "Waiting for hub id to appear on clipboard.",
            key="LINE1",
            auto_size_text=True,
        )
    ],
    [
        sg.Text(
            "Select the hub id from the FLST display.", key="LINE2", auto_size_text=True
        )
    ],
    [sg.Button("Cancel"), sg.Button("OK")],
]

inQ = queue.Queue()
outQ = queue.Queue()

# Create the Window
window = sg.Window("Hublog Downloader", layout)

# start watching the clipboard
thread = threading.Thread(target=watchCBGui, args=[inQ, outQ])
thread.start()

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read(timeout=1)
    # print(f"event: {event}, values: {values}")
    if (
        event == sg.WIN_CLOSED or event == "Cancel"
    ):  # if user closes window or clicks cancel
        inQ.put("STOP")
        break

    if outQ.qsize() > 0:
        line1, line2 = outQ.get()
        window["LINE1"].update(line1)
        window["LINE2"].update(line2)


window.close()

thread.join()
