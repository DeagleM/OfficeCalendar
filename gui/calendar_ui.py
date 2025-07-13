import customtkinter as ctk
import calendar
from datetime import datetime
from utils.helpers import format_date
from gui.task_window import open_task_window

class CalendarUI:
    def __init__(self, parent, logic, year, month):
        self.parent = parent
        self.logic = logic
        self.year = year
        self.month = month
        self.grid_frame = None

        self.create_widgets()

    def create_widgets(self):
        control_frame = ctk.CTkFrame(self.parent)
        control_frame.pack(pady=10)

        self.month_var = ctk.StringVar(value=self.month)
        self.year_var = ctk.StringVar(value=self.year)

        month_box = ctk.CTkOptionMenu(control_frame, values=[str(i) for i in range(1, 13)], variable=self.month_var, command=self.update_calendar)
        year_box = ctk.CTkOptionMenu(control_frame, values=[str(i) for i in range(2000, 2101)], variable=self.year_var, command=self.update_calendar)
        month_box.pack(side="left", padx=10)
        year_box.pack(side="left", padx=10)

        self.grid_frame = ctk.CTkFrame(self.parent)
        self.grid_frame.pack(padx=20, pady=10, expand=True, fill="both")

        self.build_calendar()

    def update_calendar(self, _=None):
        self.month = int(self.month_var.get())
        self.year = int(self.year_var.get())
        for widget in self.grid_frame.winfo_children():
            widget.destroy()
        self.build_calendar()

    def build_calendar(self):
        week_days = ["Pn", "Wt", "Śr", "Cz", "Pt", "Sb", "Nd"]
        for i, day in enumerate(week_days):
            label = ctk.CTkLabel(self.grid_frame, text=day, font=ctk.CTkFont(size=18, weight="bold"))
            label.grid(row=0, column=i, padx=5, pady=5)

        cal = calendar.monthcalendar(self.year, self.month)
        for r, week in enumerate(cal):
            for c, day in enumerate(week):
                if day == 0:
                    continue
                btn = ctk.CTkButton(
                    self.grid_frame,
                    text=str(day),
                    width=100, height=80,
                    fg_color="#f0f0f0", hover_color="#d0d0d0",text_color="black",
                    command=lambda d=day: open_task_window(self.parent, self.logic, self.year, self.month, d)
                )
                btn.grid(row=r + 1, column=c, padx=5, pady=5, sticky="nsew")

        for i in range(7):
            self.grid_frame.grid_columnconfigure(i, weight=1)
