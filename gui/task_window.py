import customtkinter as ctk
from utils.helpers import format_date
from datetime import datetime

def open_task_window(parent, logic, year, month, day):
    top = ctk.CTkToplevel(parent)
    top.title("Dodaj zadanie")
    top.geometry("400x300")
    top.lift()
    top.attributes("-topmost", True)
    top.after_idle(top.attributes, "-topmost", False)

    date_str = format_date(datetime(year, month, day))

    label = ctk.CTkLabel(top, text=f"Data: {day}.{month}.{year}", font=ctk.CTkFont(size=16, weight="bold"))
    label.pack(pady=10)

    entry = ctk.CTkEntry(top, placeholder_text="Tytuł zadania")
    entry.pack(pady=10, padx=20, fill="x")

    notif_var = ctk.StringVar(value="same_day")
    notif_options = {
        "Dzień przed": "day_before",
        "Tydzień przed": "week_before",
        "O 9 rano tego samego dnia": "same_day"
    }

    notif_menu = ctk.CTkOptionMenu(top, variable=notif_var, values=list(notif_options.keys()))
    notif_menu.pack(pady=10)

    def save():
        task = {
            "title": entry.get(),
            "notification": notif_options[notif_menu.get()]
        }
        logic.add_task(date_str, task)
        top.destroy()

    save_btn = ctk.CTkButton(top, text="Zapisz", command=save)
    save_btn.pack(pady=10)
