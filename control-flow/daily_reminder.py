task = input("Enter your task:").lower()
priority = input("Priority (high/medium/low):").lower()
bound = input("Is it time-bound? (yes/no):").lower()

match priority:
    case "high":
        if bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print("Reminder: This task is high priority but not time-bound. Try to complete it as soon as possible.")
        

    case "medium":
        if bound == "yes":
            print("Reminder: This task is medium priority and time-bound. Make sure to complete it on time.")
        else:
            print("Reminder: This task is medium priority and not time-bound. Complete it when possible.")
        
    case "low":
        if bound == "yes":
            print("Reminder: This task is low priority but time-bound. Try to finish it soon.")
        else:
            print(f"Reminder: '{task}' is a low priority task. Consider doing it when you have free time.")
        

    case _:
        print("Invalid priority (expected: high, medium, or low).")