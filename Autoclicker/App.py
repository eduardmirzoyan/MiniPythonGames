import pystray as pt
import customtkinter as ctk
from PIL import ImageTk
from pynput.keyboard import Listener, Key, KeyCode
from autoclicker import AutoClicker

class App(ctk.CTk):

    # Create it
    def __init__(self):
        super().__init__()

        # Set appearance based on system
        ctk.set_appearance_mode("system")
        ctk.set_default_color_theme("dark-blue")

        self.geometry("350x600")  # Set size
        self.resizable(False, False)
        self.title("Autoclicker")

        # Set icon
        logo = ImageTk.PhotoImage(file="icon.png")
        self.iconphoto(False, logo)

        # Add delay input
        self.add_delay_input(window=self)

        # Add key button
        self.set_key_button(window=self)

        self.set_toggle_button(window=self)
        self.set_quit_button(window=self)

        # Add apply button
        self.add_apply_button(window=self)

        # Add quit button
        self.add_quit_button(window=self)

        # Create clicker
        # clicker_thread = AutoClicker()
        # clicker_thread.start()

    def add_apply_button(self, window):

        def on_press():
            # TODO
            pass

        # Add button
        quit_button = ctk.CTkButton(
            master=window, text="Apply", command=on_press)
        quit_button.pack(padx=20, pady=20, fill="both")

    def add_quit_button(self, window):
        
        def on_press():
            # Close self
            self.destroy()

        # Add button
        quit_button = ctk.CTkButton(
            master=window, text="Quit", command=on_press)
        quit_button.pack(padx=20, pady=20, fill="both")
    
    def set_key_button(self, window):

        # Set background
        frame = ctk.CTkFrame(master=window)
        frame.pack(pady=20, padx=20, fill="both")

        # Set grid
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure((0, 1), weight=1)

        # Create label
        label = ctk.CTkLabel(master=frame, text="Key")
        # label.pack(padx=20, pady=10)
        label.grid(row=0, column=0, padx=20, pady=20, sticky=ctk.W)

        # Add listner button
        listener_button = ctk.CTkButton(master=frame, text="Set", command=lambda: self.create_input_listener(button=listener_button))
        listener_button.grid(row=0, column=1, padx=20, pady=20, sticky=ctk.E)

    def set_toggle_button(self, window):

        # Set background
        frame = ctk.CTkFrame(master=window)
        frame.pack(pady=20, padx=20, fill="both")

        # Set grid
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure((0, 1), weight=1)

        # Create label
        label = ctk.CTkLabel(master=frame, text="Toggle Key")
        # label.pack(padx=20, pady=10)
        label.grid(row=0, column=0, padx=20, pady=20, sticky=ctk.W)

        # Add listner button
        listener_button = ctk.CTkButton(
            master=frame, text="Set", command=lambda: self.create_input_listener(button=listener_button))
        listener_button.grid(row=0, column=1, padx=20, pady=20, sticky=ctk.E)

    def set_quit_button(self, window):

        # Set background
        frame = ctk.CTkFrame(master=window)
        frame.pack(pady=20, padx=20, fill="both")

        # Set grid
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure((0, 1), weight=1)

        # Create label
        label = ctk.CTkLabel(master=frame, text="Quit Key")
        # label.pack(padx=20, pady=10)
        label.grid(row=0, column=0, padx=20, pady=20, sticky=ctk.W)

        # Add listner button
        listener_button = ctk.CTkButton(
            master=frame, text="Set", command=lambda: self.create_input_listener(button=listener_button))
        listener_button.grid(row=0, column=1, padx=20, pady=20, sticky=ctk.E)

    def add_delay_input(self, window):

        # Set background
        frame = ctk.CTkFrame(master=window)
        frame.pack(pady=20, padx=20, fill="both")

        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure((0, 1), weight=1)

        # Create label
        label = ctk.CTkLabel(master=frame, text="Delay (ms)")
        #label.pack(padx=20, pady=10)
        label.grid(row=0, column=0, padx=20, pady=20, sticky=ctk.W)

        # Create textbox
        entry = ctk.CTkEntry(master=frame, placeholder_text=">= 1")
        entry.grid(row=0, column=1, padx=20, pady=20, sticky=ctk.E)
    

    def create_input_listener(self, button: ctk.CTkButton):
        # Create new window
        new_window = ctk.CTkToplevel(self)
        new_window.geometry("400x200")

        # create label on CTkToplevel window
        label = ctk.CTkLabel(new_window, text="Press ANY key...")
        label.pack(side="top", fill="both", expand=True, padx=40, pady=40)

        # Need to start listening for input now...
        self.listen_for_input(window=new_window, button=button)
    
    def listen_for_input(self, window: ctk.CTkToplevel, button: ctk.CTkButton):

        # On press function
        def on_press(key):
            
            # Update Button text
            button.configure(text=key)

            # Close window
            window.destroy()

            # Stop listener
            return False
            
            
        # Create thread
        listener = Listener(on_press=on_press)
        listener.start()  # start to listen on a separate thread


# Create app
app = App()

# Run app
app.mainloop()