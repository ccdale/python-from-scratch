import queue
import threading

import PySimpleGUI as sg

from hublogs.hlwatch import watchClipboard
from hublogs.hlwatch import watchCBGui


def hlg():
    try:
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
                    "Select the hub id from the FLST display.",
                    key="LINE2",
                    auto_size_text=True,
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
                window.close()
                line1, line2 = outQ.get()
                layout = [[sg.Text(line1)], [sg.Text(line2)], [sg.Button("Cancel")]]
                window = sg.Window("Hublog Downloader", layout)

        window.close()

        thread.join()
    except Exception as e:
        exci = sys.exc_info()[2]
        lineno = exci.tb_lineno
        fname = exci.tb_frame.f_code.co_name
        ename = type(e).__name__
        msg = f"{ename} Exception at line {lineno} in function {fname}: {e}"
        print(msg)
