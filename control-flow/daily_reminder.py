task = input("Enter your task:").lower()
priority = input("Priority (high/medium/low):").lower()
time_bound = input("Is it time-bound? (yes/no):").lower()

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a {priority} priority task but not time-bound. Try to complete it as soon as possible.")

    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a {priority} priority task and time-bound. Make sure to complete it on time.")
        else:
            print(f"Reminder: '{task}' is a {priority} priority task and not time-bound. Complete it when possible.")
        
    case "low":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a {priority} priority task but time-bound. Try to finish it soon.")
        else:
            print(f"Reminder: '{task}' is a {priority} priority task. Consider doing it when you have free time.")
        

    case _:
        print("Invalid priority (expected: high, medium, or low).")


