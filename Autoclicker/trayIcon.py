import pystray
import PIL.Image

# Load image
image = PIL.Image.open("icon.png")

def on_clicked(icon, item):
    if str(item) == "Exit":
        trayIcon.stop()
    else:
        print("Not implemented.")


trayIcon = pystray.Icon("Icon", image, menu=pystray.Menu(
    pystray.MenuItem("Say Hello", on_clicked),
    pystray.MenuItem("Exit", on_clicked)
))

# Start the application
trayIcon.run()
