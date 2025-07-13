import customtkinter as ctk
from datetime import datetime
from gui.calendar_ui import CalendarUI
from logic.calendar_logic import CalendarLogic

class CalendarApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")
        self.title("Kalendarz")
        self.state("zoomed")

        self.logic = CalendarLogic()
        today = datetime.today()
        self.ui = CalendarUI(self, self.logic, today.year, today.month)

if __name__ == "__main__":
    app = CalendarApp()
    app.mainloop()
