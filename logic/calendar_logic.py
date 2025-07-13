from storage.data_handler import load_data, save_data

class CalendarLogic:
    def __init__(self):
        self.tasks_by_date = load_data()

    def get_tasks(self, date_str):
        return self.tasks_by_date.get(date_str, [])

    def add_task(self, date_str, task):
        if not task.get("title"):
            return
        self.tasks_by_date.setdefault(date_str, []).append(task)
        save_data(self.tasks_by_date)
