import tkinter as tk
from tkinter import ttk

class View(tk.Tk):
    PAD = 10
    MAX_BUTTONS_PER_ROW = 4
    BUTTON_CAPTIONS = [
        "C", "+/-", "%", "/",
        7, 8, 9, "*",
        4, 5, 6, "-",
        1, 2, 3, "+",
        0, ".", "="
    ]

    def __init__(self, parent):
        super().__init__()
        self.title("PyCalc 1.0")
        self.config(bg="black")
        self._configure_styles()
        self.controller = parent
        self.value_var = tk.StringVar()
        self._make_main_frame()
        self._make_entry()
        self._make_buttons()
        self._center_window()

    def _configure_styles(self):
        style = ttk.Style()
        style.theme_use('alt')

        # configure style for number button
        style.configure(
            'N.TButton',
            foreground="white",
            background="gray"
        )

        # configure all button style during hover state
        style.map(
            'TButton',
            foreground=[('hover', 'black')]
        )

        # configure style for operator button
        style.configure(
            'O.TButton',
            foreground="white",
            background="orange"
        )

        # configure style for miscellaneous button
        style.configure(
            'M.TButton',
            background="white"
        )

        # configure entry style
        style.configure(
            'TEntry'
        )

        style.map(
            'TEntry',
            foreground=[('disabled', 'black')],
            background=[('disabled', 'white')],
            fieldbackground=[('disabled', 'white')]
        )

    def main(self):
        self.mainloop()

    def _make_main_frame(self):
        self.main_frm = ttk.Frame(self)
        self.main_frm.pack(padx=self.PAD, pady=self.PAD)

    def _make_entry(self):
        ent = ttk.Entry(
            self.main_frm,
            textvariable=self.value_var,
            justify='right',
            state="disabled",
            font=('Arial', 30)
        )
        ent.pack(fill="x")

    def _make_buttons(self):
        outer_frm = ttk.Frame(self.main_frm)
        outer_frm.pack()

        for count, caption in enumerate(self.BUTTON_CAPTIONS):
            if count % self.MAX_BUTTONS_PER_ROW == 0 or count == 0:
                frm = ttk.Frame(outer_frm)
                frm.pack(fill='x')
            if isinstance(caption, int):
                style_prefix = 'N'
            elif self._is_operator(caption):
                style_prefix = "O"
            else:
                style_prefix = "M"
            btn = ttk.Button(
                frm,
                text=caption,
                command=(lambda button=caption: self.controller.on_button_click(button)),
                style=f"{style_prefix}.TButton"
            )

            if caption == 0:
                fill = 'x'
                expand = 1
            else:
                fill = "none"
                expand = 0
            btn.pack(side="left", expand=expand, fill=fill)

    def _is_operator(self, caption):
        return caption in ['/', "*", "-", "+", "="]

    def _center_window(self):
        self.update() # update the width and height dimension after all widgets is created
        width = self.winfo_width()
        height = self.winfo_height()
        x_offset = (self.winfo_screenwidth() - width)//2
        y_offset = (self.winfo_screenheight() - height)//2
        self.geometry(
           f'{width}x{height}+{x_offset}+{y_offset}'
        )