import tkinter as tk
from tkinter import ttk
from collections import deque
        
class Timer(ttk.Frame):
    def __init__(self, parent=None, controller=None, show_settings=None, **kwargs):
        super().__init__(parent, **kwargs)
        
        # Ensure that all frames take up full width
        self.columnconfigure(0, weight=1)
        
        self.configure(padding=10, style="Background.TFrame") 
        
        self.controller = controller
        pomodoro_time = int(controller.pomodoro.get())
        
        # initialize the timer with 10 sec
        self.current_time = tk.StringVar(value=f"{pomodoro_time:02d}:00")
        
        self.current_timer_label = tk.StringVar(value=controller.timer_schedule[0])
        
        self.timer_running = False
        
        # create a private variable for keeping track of the job when start/stop
        self._timer_decrement_job = None
        
        top_frame = ttk.Frame(self)
        top_frame.columnconfigure((0, 1), weight=1)
        top_frame.grid(row=0, column=0, sticky='NSEW')
        top_frame.configure(style="Background.TFrame")
        
        timer_description = ttk.Label(
            top_frame,
            textvariable=self.current_timer_label,
            style='PomodoroText.TLabel'
        )
        
        timer_description.grid(
            row=0, 
            column=0, 
            sticky='W',
            padx=(10, 0),
            pady=(10, 0)
        )
        
        settings_button = ttk.Button(
            top_frame,
            text="Settings",
            command=show_settings,
            style="PomodoroButton.TButton",
            cursor='hand2'
        )
        
        settings_button.grid(row=0, column=1, sticky='E', padx=10, pady=(10, 0))
        
        timer_frame = ttk.Frame(self, height="100", style="Timer.TFrame")
        timer_frame.grid(row=1, column=0, pady=(10, 0), sticky="NSEW")
        
        timer_counter = ttk.Label(
            timer_frame,
            textvariable=self.current_time,
            style='TimerText.TLabel'
        )
        
        # We use place method instead of grid method to position the timer counter
        # place method acts similar to absolute positioning, but we can also set relative position using relx and rely
        # however, text label has an anchor on the left, therefore we need to add anchor='center' to use the center as the anchor reference
        timer_counter.place(relx=0.5, rely=0.5, anchor='center')
        
        button_container = ttk.Frame(self, style='Background.TFrame', padding=10)
        button_container.grid(row=2, column=0, sticky='EW')
        
        # this button container will house 3 buttons, so we set column 0 and 1 to weight=1 giving them equal space
        button_container.columnconfigure((0, 1, 2), weight=1)
        
        self.start_button = ttk.Button(
            button_container, 
            text="Start", 
            command=self.start_timer,
            cursor='hand2',
            style='PomodoroButton.TButton'
        )
        
        self.start_button.grid(row=0, column=0, sticky='EW')
        
        self.stop_button = ttk.Button(
            button_container, 
            text="Stop",
            state='disabled',
            command=self.stop_timer,
            cursor='hand2',
            style='PomodoroButton.TButton'
        )
        
        self.stop_button.grid(row=0, column=1, sticky='EW')
    
        reset_button = ttk.Button(
            button_container,
            text='Reset',
            command=self.reset_timer,
            cursor='hand2',
            style='PomodoroButton.TButton'
        )
        
        reset_button.grid(row=0, column=2, sticky="EW")
        
        # For debugging, make sure to change frame to tk.Frame instead of ttk.Frame during debugging
        # self.configure(borderwidth=10, relief='solid')
        # top_frame.configure(highlightbackground="red", highlightcolor="red", highlightthickness="10", bd=0)
        # button_container.configure(highlightbackground="green", highlightcolor="green", highlightthickness="10", bd=0)
        # timer_frame.configure( highlightbackground="blue", highlightcolor="blue", highlightthickness="10", bd=0)

    def decrement_time(self):
        current_time = self.current_time.get()
        if self.timer_running and current_time != "00:00":
            minutes, seconds = current_time.split(":")
            
            if int(seconds) > 0:
                seconds = int(seconds) - 1
                minutes = int(minutes)
            else:
                seconds = 59
                minutes = int(minutes) - 1
                
            self.current_time.set(f"{minutes:02d}:{seconds:02d}") 
            
            # Run the function again after 1s
            self._timer_decrement_job = self.after(1000, self.decrement_time)
            
        elif self.timer_running and current_time == "00:00":
            self.controller.timer_schedule.rotate(-1)
            next_up = self.controller.timer_schedule[0]
            self.current_timer_label.set(next_up)
            
            if next_up == "Pomodoro":
                pomodoro_time = int(self.controller.pomodoro.get())
                self.current_time.set(f"{pomodoro_time:02d}:00")
            elif next_up == "Short Break":
                short_break_time = int(self.controller.short_break.get())
                self.current_time.set(f"{short_break_time:02d}:00")
            else:
                long_break_time = int(self.controller.long_break.get())
                self.current_time.set(f"{long_break_time:02d}:00")
            
            # Run the function again after 1s
            self._timer_decrement_job = self.after(1000, self.decrement_time)
            
    def start_timer(self):
        self.timer_running = True
        self.start_button['state'] = 'disabled'
        self.stop_button['state'] = 'enabled'
        self.decrement_time()
    
    def stop_timer(self):
        self.timer_running = False
        self.start_button['state'] = 'enabled'
        self.stop_button['state'] = 'disabled'
        if self._timer_decrement_job:
            self.after_cancel(self._timer_decrement_job)
            self._timer_decrement_job = None
            
    def reset_timer(self):
        self.stop_timer()
        pomodoro_time = int(self.controller.pomodoro.get())
        self.current_time.set(f"{pomodoro_time:02d}:00")
        self.controller.timer_schedule = deque(self.controller.timer_order)
        self.current_timer_label.set(self.controller.timer_schedule[0])
        
        
    