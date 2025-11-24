# -------------------------------------------
# Exercise 1: Assessment Preparation
# -------------------------------------------
# This exercise will help you prepare for Assessment 3: Python Program.
# If you can complete this exercise, you will be ready to tackle any of
# the six assessment briefs (Emergency Calls, Lost Property, Student Progress,
# Event Registration, Library Books, or Expense Tracker).
#
# We'll build a simple "Task Manager" together, practising all the skills
# you need for your assessment.
#
# **If you are working alone:** Complete each task in order and commit
# your work after each task.
#
# **If working in groups:** Follow the swap instructions after each task.
#
# Remember the key concepts we'll use:
# - Lists: Store multiple items
# - Dictionaries: Store related information together with keys
# - Loops: Repeat actions (while, for)
# - Conditionals: Make decisions (if, elif, else)
# - Validation: Check user input is correct
#
# IMPORTANT: Don't delete any code from previous tasks!
# Each task builds on the one before it.
# -------------------------------------------


# -------------------------------------------
# Task 1: Setting Up Data Storage
# -------------------------------------------
# For your assessment, you'll need to store multiple records.
# We use a LIST to store many items, and DICTIONARIES to store details
# about each individual item.
#
# TODO:
# 1. Create an empty list called 'tasks'
#    This will store all our task records
#
#    EXAMPLE:
#    tasks = []
#
# 2. Print the tasks list to see what it looks like (it should be empty)
#
# Write your code below:




# -------------------------------------------
# SWAP COMPUTERS (Don't swap computers if working alone)
# -------------------------------------------
# Use Git to:
# 1. Stage your changes: git add .
# 2. Commit with message: git commit -m "Completed Task 1"
# 3. Push to repository: git push origin main
# The next learner must pull before continuing: git pull origin main
# -------------------------------------------


# -------------------------------------------
# Task 2: Creating a Welcome Message
# -------------------------------------------
# Every program needs a clear welcome message.
# This helps users understand what the system does.
#
# TODO:
# 1. Print a line of equals signs: "======================================="
# 2. Print "TASK MANAGER SYSTEM"
# 3. Print "Keep track of your daily tasks"
# 4. Print another line of equals signs
# 5. Print a blank line using print()
#
# Write your code below:




# -------------------------------------------
# SWAP COMPUTERS (Don't swap computers if working alone)
# -------------------------------------------
# Use Git to:
# 1. Stage your changes: git add .
# 2. Commit with message: git commit -m "Completed Task 2"
# 3. Push to repository: git push origin main
# The next learner must pull before continuing: git pull origin main
# -------------------------------------------


# -------------------------------------------
# Task 3: Creating the First Menu
# -------------------------------------------
# Your program needs a menu so users can choose what to do.
# We'll start with just displaying the menu once.
#
# TODO:
# 1. Print these menu options:
#    "1. Add task"
#    "2. View all tasks"
#    "3. Exit"
#
# 2. Print a blank line
#
# 3. Ask the user to choose an option and store it in a variable called 'choice'
#    Use: choice = input("Select an option: ")
#
# 4. Print a blank line
#
# 5. Print what they chose: print(f"You selected: {choice}")
#
# Write your code below:




# -------------------------------------------
# SWAP COMPUTERS (Don't swap computers if working alone)
# -------------------------------------------
# Use Git to:
# 1. Stage your changes: git add .
# 2. Commit with message: git commit -m "Completed Task 3"
# 3. Push to repository: git push origin main
# The next learner must pull before continuing: git pull origin main
# -------------------------------------------


# -------------------------------------------
# Task 4: Making the Menu Loop
# -------------------------------------------
# The menu should keep appearing until the user chooses to exit.
# We use a WHILE loop for this.
#
# TODO:
# 1. Find your menu code from Task 3
#
# 2. BEFORE the menu code, set choice to "0" so the loop can start:
#    choice = "0"
#
# 3. Replace the menu code with a while loop:
#    while choice != "3":
#        # Put ALL your menu code from Task 3 inside here
#        # Remember to indent everything inside the loop!
#
# 4. Delete the line that prints what they selected (we don't need it anymore)
#
# 5. Test it - the menu should repeat until you type "3"
#
# Write your code (modify your Task 3 code):




# -------------------------------------------
# SWAP COMPUTERS (Don't swap computers if working alone)
# -------------------------------------------
# Use Git to:
# 1. Stage your changes: git add .
# 2. Commit with message: git commit -m "Completed Task 4"
# 3. Push to repository: git push origin main
# The next learner must pull before continuing: git pull origin main
# -------------------------------------------


# -------------------------------------------
# Task 5: Validating Menu Input
# -------------------------------------------
# We need to check that users enter valid menu options.
# If they don't, we should show an error and ask again.
#
# TODO:
# 1. Find where you get the user's choice (the input line)
#
# 2. AFTER getting the choice, but BEFORE the end of the while loop, add:
#
#    while choice != "1" and choice != "2" and choice != "3":
#        print("ERROR: Invalid choice")
#        print()
#        print("1. Add task")
#        print("2. View all tasks")
#        print("3. Exit")
#        print()
#        choice = input("Select an option: ")
#        print()
#
# 3. Test it by entering invalid options like "5" or "hello"
#
# Write your code (add to your while loop from Task 4):




# -------------------------------------------
# SWAP COMPUTERS (Don't swap computers if working alone)
# -------------------------------------------
# Use Git to:
# 1. Stage your changes: git add .
# 2. Commit with message: git commit -m "Completed Task 5"
# 3. Push to repository: git push origin main
# The next learner must pull before continuing: git pull origin main
# -------------------------------------------


# -------------------------------------------
# Task 6: Adding Option 1 - Get Input
# -------------------------------------------
# Now let's make option 1 actually work!
# When the user chooses "1", we'll collect information.
#
# TODO:
# 1. After your validation loop (but still inside the main while loop), add:
#
#    if choice == "1":
#        task_name = input("Enter task name: ")
#        priority = input("Enter priority (High/Medium/Low): ")
#        print()
#        print("Task added successfully")
#        print()
#
# 2. Test option 1 - it should ask for input and confirm
#
# Write your code (add to your while loop):




# -------------------------------------------
# SWAP COMPUTERS (Don't swap computers if working alone)
# -------------------------------------------
# Use Git to:
# 1. Stage your changes: git add .
# 2. Commit with message: git commit -m "Completed Task 6"
# 3. Push to repository: git push origin main
# The next learner must pull before continuing: git pull origin main
# -------------------------------------------


# -------------------------------------------
# Task 7: Validating Task Input
# -------------------------------------------
# We should validate the input when adding tasks.
# Make sure fields aren't left blank.
#
# TODO:
# 1. Find your if choice == "1": section
#
# 2. AFTER getting task_name, add validation:
#    while task_name == "":
#        print("ERROR: Task name cannot be blank")
#        task_name = input("Enter task name: ")
#
# 3. AFTER getting priority, add validation:
#    while priority == "":
#        print("ERROR: Priority cannot be blank")
#        priority = input("Enter priority (High/Medium/Low): ")
#
# 4. Test by pressing Enter without typing anything
#
# Write your code (add to your choice == "1" section):




# -------------------------------------------
# SWAP COMPUTERS (Don't swap computers if working alone)
# -------------------------------------------
# Use Git to:
# 1. Stage your changes: git add .
# 2. Commit with message: git commit -m "Completed Task 7"
# 3. Push to repository: git push origin main
# The next learner must pull before continuing: git pull origin main
# -------------------------------------------


# -------------------------------------------
# Task 8: Storing Tasks in the List
# -------------------------------------------
# Now let's actually save the task to our list!
# We'll create a dictionary and add it to the tasks list.
#
# TODO:
# 1. Find your if choice == "1": section
#
# 2. AFTER the validation, but BEFORE printing "Task added successfully", add:
#
#    task = {
#        "name": task_name,
#        "priority": priority,
#        "status": "Not started"
#    }
#    tasks.append(task)
#
# 3. Test by adding a few tasks
#
# Write your code (add to your choice == "1" section):




# -------------------------------------------
# SWAP COMPUTERS (Don't swap computers if working alone)
# -------------------------------------------
# Use Git to:
# 1. Stage your changes: git add .
# 2. Commit with message: git commit -m "Completed Task 8"
# 3. Push to repository: git push origin main
# The next learner must pull before continuing: git pull origin main
# -------------------------------------------


# -------------------------------------------
# Task 9: Adding Option 2 - View All Tasks
# -------------------------------------------
# Let's make option 2 work - viewing all tasks.
# We need to loop through the list and display each task.
#
# TODO:
# 1. After your if choice == "1": section (still inside main while loop), add:
#
#    elif choice == "2":
#        if len(tasks) == 0:
#            print("No tasks recorded yet")
#            print()
#        else:
#            print("All tasks:")
#            print()
#            for task in tasks:
#                print(f"Name: {task['name']}")
#                print(f"Priority: {task['priority']}")
#                print(f"Status: {task['status']}")
#                print("---------------------------------------")
#            print()
#
# 2. Test by adding some tasks, then viewing them
#
# Write your code (add after your choice == "1" section):




# -------------------------------------------
# SWAP COMPUTERS (Don't swap computers if working alone)
# -------------------------------------------
# Use Git to:
# 1. Stage your changes: git add .
# 2. Commit with message: git commit -m "Completed Task 9"
# 3. Push to repository: git push origin main
# The next learner must pull before continuing: git pull origin main
# -------------------------------------------


# -------------------------------------------
# Task 10: Adding Option 3 - Exit
# -------------------------------------------
# When users choose option 3, we should thank them.
# The while loop will stop automatically.
#
# TODO:
# 1. After your elif choice == "2": section (still inside main while loop), add:
#
#    elif choice == "3":
#        print("Thank you for using the Task Manager")
#        print("Goodbye")
#
# 2. Test the complete program:
#    - Add a few tasks
#    - View them
#    - Exit
#    - Try invalid menu options
#    - Try blank task names
#
# Write your code (add after your choice == "2" section):




# -------------------------------------------
# SWAP COMPUTERS (Don't swap computers if working alone)
# -------------------------------------------
# Use Git to:
# 1. Stage your changes: git add .
# 2. Commit with message: git commit -m "Completed Task 10"
# 3. Push to repository: git push origin main
# The next learner must pull before continuing: git pull origin main
# -------------------------------------------


# -------------------------------------------
# CONGRATULATIONS!
# -------------------------------------------
# You've just built a complete menu-driven program with:
# ✓ Data storage (list of dictionaries)
# ✓ Welcome message
# ✓ Looping menu
# ✓ Input validation
# ✓ Adding records
# ✓ Viewing records
# ✓ Exit handling
#
# This is EXACTLY what you need for Assessment 3!
# The structure is the same for all six assessment briefs.
# You just need to change:
# - The welcome message
# - What information you collect
# - What you display
#
# -------------------------------------------
# EXTENSION ACTIVITIES
# -------------------------------------------

# Extension 1: Search Feature
# -------------------------------------------
# Add a fourth menu option to search for tasks by name.
#
# TODO:
# 1. Find everywhere you have the menu (including in validation)
#
# 2. Update ALL menus to show:
#    "1. Add task"
#    "2. View all tasks"
#    "3. Search for task"
#    "4. Exit"
#
# 3. Change your main while loop to: while choice != "4":
#
# 4. Update your validation to check for "1", "2", "3", or "4"
#
# 5. After your elif choice == "2": section, add:
#
#    elif choice == "3":
#        if len(tasks) == 0:
#            print("No tasks to search")
#            print()
#        else:
#            search_name = input("Enter task name to search for: ")
#            found = False
#            for task in tasks:
#                if task["name"] == search_name:
#                    print()
#                    print("Task found:")
#                    print(f"Name: {task['name']}")
#                    print(f"Priority: {task['priority']}")
#                    print(f"Status: {task['status']}")
#                    print()
#                    found = True
#            if found == False:
#                print()
#                print("No matching tasks found")
#                print()
#
# 6. Change your exit section to: elif choice == "4":
#
# Write your code (modify existing code):




# -------------------------------------------
# SWAP COMPUTERS (Don't swap computers if working alone)
# -------------------------------------------
# Use Git to:
# 1. Stage your changes: git add .
# 2. Commit with message: git commit -m "Completed Extension 1"
# 3. Push to repository: git push origin main
# The next learner must pull before continuing: git pull origin main
# -------------------------------------------


# Extension 2: Summary Statistics
# -------------------------------------------
# Add an option to show how many tasks there are of each priority.
#
# TODO:
# 1. Update ALL menus to include a new option:
#    "4. View statistics"
#    And change "4. Exit" to "5. Exit"
#
# 2. Update your while loop to: while choice != "5":
#
# 3. Update validation to check for "1", "2", "3", "4", or "5"
#
# 4. After your elif choice == "3": section, add:
#
#    elif choice == "4":
#        if len(tasks) == 0:
#            print("No tasks to calculate statistics")
#            print()
#        else:
#            high_count = 0
#            medium_count = 0
#            low_count = 0
#            for task in tasks:
#                if task["priority"] == "High":
#                    high_count = high_count + 1
#                elif task["priority"] == "Medium":
#                    medium_count = medium_count + 1
#                elif task["priority"] == "Low":
#                    low_count = low_count + 1
#            print("Task Statistics:")
#            print(f"Total tasks: {len(tasks)}")
#            print(f"High priority: {high_count}")
#            print(f"Medium priority: {medium_count}")
#            print(f"Low priority: {low_count}")
#            print()
#
# 5. Update your exit to: elif choice == "5":
#
# Write your code (modify existing code):




# -------------------------------------------
# SAVE YOUR WORK
# -------------------------------------------
# Use Git to:
# 1. Stage your changes: git add .
# 2. Commit with message: git commit -m "Completed Extension 2"
# 3. Push to repository: git push origin main
# -------------------------------------------


# -------------------------------------------
# YOU'RE READY FOR ASSESSMENT 3!
# -------------------------------------------
# You now have all the skills needed to complete any of the six briefs:
# 1. Emergency Call Logger
# 2. Lost Property Tracker
# 3. Student Progress Recorder
# 4. Event Registration App
# 5. Library Book Tracker
# 6. Expense Tracker
#
# They all follow this same structure - just with different:
# - Data fields (what information you store)
# - Menu options (what the user can do)
# - Calculations (if needed, like averages or totals)
#
# Good luck with your assessment!
# -------------------------------------------
