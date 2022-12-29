import pystray as pt
import customtkinter as ctk
from PIL import Image, ImageTk


def button_event():
    pass

# Set appearance based on system
ctk.set_appearance_mode("system")
ctk.set_default_color_theme("dark-blue")

# Create window
window = ctk.CTk()
window.geometry("350x600") # Set size
window.resizable(False, False)
window.title("Title")

# Set icon
logo = ImageTk.PhotoImage(file="icon.png")
window.iconphoto(False, logo)

# Fill in window

# Background
frame = ctk.CTkFrame(master=window)
frame.pack(pady=20, padx=20, fill="both", expand=True)

# Add delay input
entry = ctk.CTkEntry(master=frame, placeholder_text="CTkEntry")
entry.pack(padx=20, pady=10)

# Add combobox for button

# Add button
quit_button = ctk.CTkButton(
    master=frame, text="Quit", command=button_event)
quit_button.pack()



# Render it
window.mainloop()