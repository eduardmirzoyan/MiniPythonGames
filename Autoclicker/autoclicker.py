import time
import threading
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode

# Configurable settings
delay = 0.001
button = Button.left
toggle_key = KeyCode(char='t')
exit_key = KeyCode(char='e')

class AutoClicker(threading.Thread):
    def __init__(self, delay=0.001, button=Button.left):
        super().__init__()

        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True

        self.mouse = Controller()

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False
    
    def exit(self):
        self.stop_clicking()
        self.program_running = False
    
    def run(self):
        while self.program_running:
            while self.running:
                self.mouse.click(self.button)
                time.sleep(self.delay)


# clicker_thread = AutoClicker(delay, button)
# clicker_thread.start()

# def on_press(key):
#     # Check input
#     if key == toggle_key:
#         # Toggle thread state
#         if clicker_thread.running:
#             clicker_thread.stop_clicking()
#         else:
#             clicker_thread.start_clicking()
#     # Exit program
#     elif key == exit_key:
#         clicker_thread.exit()
#         listener.stop()

# with Listener(on_press=on_press) as listener:
#     listener.join()