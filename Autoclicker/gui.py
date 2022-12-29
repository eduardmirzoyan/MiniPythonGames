import tkinter as tk

# Create window
window = tk.Tk()
# Set size
window.geometry("420x420")
# Set title
window.title("Title I guess")

# Get icon
icon = tk.PhotoImage(file='icon.png')
window.iconphoto(True, icon)

# Show window, listen for events
window.mainloop()