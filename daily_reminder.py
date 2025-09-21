task = input("Please, give me a description about your task? ").lower()
priority = input("Is your task (High, Medium or Low priority)? ").lower()
bound = input("Is your task time-bound (yes or no)? ").lower()

match priority:
    case "high":
        if bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        elif bound == "no":
            print("Reminder: This task is high priority but not time-bound. Try to complete it as soon as possible.")
        else:
            print("Invalid input for time-bound (expected 'yes' or 'no').")

    case "medium":
        if bound == "yes":
            print("Reminder: This task is medium priority and time-bound. Make sure to complete it on time.")
        elif bound == "no":
            print("Reminder: This task is medium priority and not time-bound. Complete it when possible.")
        else:
            print("Invalid input for time-bound (expected 'yes' or 'no').")

    case "low":
        if bound == "yes":
            print("Reminder: This task is low priority but time-bound. Try to finish it soon.")
        elif bound == "no":
            print(f"Reminder: '{task}' is a low priority task. Consider doing it when you have free time.")
        else:
            print("Invalid input for time-bound (expected 'yes' or 'no').")

    case _:
        print("Invalid priority (expected: high, medium, or low).")