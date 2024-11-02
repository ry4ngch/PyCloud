import tkinter as tk
from tkinter import ttk
from collections import deque

# Note: The following import is actually frames.__init__ under the hood
from frames import Timer, Settings

# Set DPI Awareness for Windows OS
from windows import set_dpi_awareness
import platform

if platform.system == 'Windows':
    set_dpi_awareness()

# Create Constant to store styling information
COLOUR_PRIMARY = '#2e3f4f'
COLOUR_SECONDARY = '#293846'
COLOUR_LIGHT_BACKGROUND = '#fff'
COLOUR_LIGHT_TEXT = '#eee',
COLOUR_DARK_TEXT = '#8095a8'
        

class PomodoroTimer(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Styling
        style = ttk.Style(self)
        style.theme_use('clam')
        style.configure('Timer.TFrame', background=COLOUR_LIGHT_BACKGROUND)
        style.configure('Background.TFrame', background=COLOUR_PRIMARY)
        style.configure(
            'TimerText.TLabel',
            background=COLOUR_LIGHT_BACKGROUND,
            foreground=COLOUR_DARK_TEXT,
            font='Courier 38'
        )
        
        style.configure(
            'LightText.TLabel',
            background=COLOUR_PRIMARY,
            foreground=COLOUR_LIGHT_TEXT
        )
        
        style.configure(
            'PomodoroButton.TButton',
            background=COLOUR_SECONDARY,
            foreground=COLOUR_LIGHT_TEXT
        )
        
        style.configure(
            'PomodoroText.TLabel',
            background=COLOUR_PRIMARY,
            foreground=COLOUR_LIGHT_TEXT,
            font='Courier 18'
        )
        
        ## Add hover effect
        style.map(
            'PomodoroButton.TButton',
            background=[('active', COLOUR_PRIMARY), ('disabled', COLOUR_LIGHT_TEXT)]
        )
        
        self.configure(background = COLOUR_PRIMARY)
        
        self.title('Pomodoro Timer')
        
        # Set column 0 to grow to full width to center the frame
        self.columnconfigure(0, weight=1)
        
        # Set row 1 to grow to full width
        self.rowconfigure(1, weight=1)
        
        # Set default values
        self.pomodoro = tk.StringVar(value=25)
        self.long_break = tk.StringVar(value=15)
        self.short_break = tk.StringVar(value=5)
        
        # set the pomodoro sequence
        self.timer_order = ["Pomodoro", "Short Break", "Pomodoro", "Short Break", "Pomodoro", "Long Break"]
        self.timer_schedule = deque(self.timer_order)
        
        container = tk.Frame(self)
        container.grid()
        
        # configure container to grow to take up full width and center
        container.columnconfigure(0, weight=1)
        
        timer_frame = Timer(container, self, show_settings=lambda: self.show_frame(Settings))
        timer_frame.grid(row=0, column=0, sticky='NSEW')
        settings_frame = Settings(container, self, show_timer=lambda: self.show_frame(Timer))
        settings_frame.grid(row=0, column=0, sticky='NSEW')
        
        # Put the Timer and Settings frames in a dictionary to easier access using tkraise
        self.frames = dict()
        self.frames[Timer] = timer_frame
        self.frames[Settings] = settings_frame
        
        # Set the Timer frame to appear upon the app initialization
        self.show_frame(Timer)
        
        # For debugging, make sure to change container frame from ttk.Frame to tk.Frame for it to work
        # container.configure(highlightbackground="red", highlightcolor="red", highlightthickness="10", bd=0)
        
    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()
        
        # To get timer to reset upon exiting from Settings
        if container.__name__ == "Timer":
            if not frame.timer_running:
                frame.reset_timer()
        
        # The below is a simple solution for showing frames of different sizes
        # uncomment it to get it to work
        # for frame in self.frames.values():
        #     frame.grid_remove()
        # frame = self.frames[container]
        # frame.grid()
        
if __name__ == '__main__':
    app = PomodoroTimer()
    app.mainloop()