import json
from datetime import datetime

class ClassSession:
    def __init__(self, name, day, start_time, end_time, location):
        self.name = name
        self.day = day
        self.start_time = start_time
        self.end_time = end_time
        self.location = location

    def __str__(self):
        return f"{self.name:<15} | {self.day:<9} | {self.start_time} - {self.end_time} | {self.location}"

    def to_dict(self):
        return {
            "name": self.name,
            "day": self.day,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "location": self.location
        }

    @staticmethod
    def from_dict(data):
        return ClassSession(
            data["name"], data["day"], data["start_time"], data["end_time"], data["location"]
        )

schedule = []


def add_class():
    print("\n📝 Add a New Class")
    name = input("Enter class name: ")
    day = input("Enter day (e.g. Monday): ")
    start_time = input("Enter start time (HH:MM): ")
    end_time = input("Enter end time (HH:MM): ")
    location = input("Enter location: ")

    new_class = ClassSession(name, day, start_time, end_time, location)
    schedule.append(new_class)
    print(f"\n✅ Class '{name}' added to schedule!\n")


def view_schedule():
    if not schedule:
        print("\n📭 Your schedule is empty.\n")
    else:
        print("\n📅 Your Class Schedule:\n")
        print("=" * 60)
        print(f"{'Class Name':<15} | {'Day':<9} | Time       | Location")
        print("=" * 60)
        for sch in schedule:
            print(sch)
        print("=" * 60)


def save_schedule(filename="schedule.json"):
    with open(filename, "w") as f:
        json.dump([cls.to_dict() for cls in schedule], f, indent=4)
    print("\n💾 Schedule saved successfully!\n")


def load_schedule(filename="schedule.json"):
    global schedule
    try:
        with open(filename, "r") as f:
            data = json.load(f)
            schedule = [ClassSession.from_dict(item) for item in data]
        print("\n📂 Schedule loaded successfully!\n")
    except FileNotFoundError:
        print("\n⚠️ No saved schedule found.\n")


def main_menu():
    load_schedule()  # Automatically try to load on start
    while True:
        print("\n===== 🗂️ CLASS SCHEDULE MENU =====")
        print("1️⃣  Add Class")
        print("2️⃣  View Schedule")
        print("3️⃣  Save Schedule")
        print("4️⃣  Exit")
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            add_class()
        elif choice == '2':
            view_schedule()
        elif choice == '3':
            save_schedule()
        elif choice == '4':
            save_schedule()  # Auto-save on exit
            print("\n👋 Goodbye! Your schedule has been saved.")
            break
        else:
            print("\n❌ Invalid choice. Please enter 1, 2, 3, or 4.")

main_menu()



        