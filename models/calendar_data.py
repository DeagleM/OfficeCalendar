from dataclasses import dataclass

@dataclass
class Task:
    title: str
    date: str
    notification: str
