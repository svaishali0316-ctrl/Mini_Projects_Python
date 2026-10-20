# Project 2: TO-Do-List

print("=" * 30)
print("        TO DO LIST     ")
print("=" * 30)

tasks = []

while True:
    task=input("Enter a task: ")
    if task.lower() == "done":
        break
    tasks.append(task)

print("Your to-do list: ")
for i, task in enumerate(tasks, 1):
    print(f"{i}. {task}")
