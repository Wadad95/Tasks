import json

tasks = []

def add_task(title, description, due_date):
    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "status": "under genomförande"
    }
    tasks.append(task)
    print("Uppgiften har lagts till framgångsrikt.")

def display_tasks(show_completed=None):
    for i, task in enumerate(tasks):
        if show_completed is None or (show_completed and task["status"] == "komplett") or (not show_completed and task["status"] == "under genomförande"):
            print(f"{i + 1}. {task['title']} - {task['status']}")

def update(index, status):
    if 0 <= index < len(tasks):
        tasks[index]["status"] = status
        print("Uppgiften är uppdaterad.")
    else:
        print("Uppgiften hittades inte.")

def save_tasks(filename="tasks.json"):
    with open(filename, "w") as file:
        json.dump(tasks, file)
    print("Uppgifterna har sparats.")

def load_tasks(filename="tasks.json"):
    global tasks
    try:
        with open(filename, "r") as file:
            tasks = json.load(file)
        print("Uppgifterna har laddats upp.")
    except FileNotFoundError:
        print("Filen hittades inte.")

def main():
    load_tasks()
    while True:
        print("\n-- Lista --")
        print("1. Lägg till en ny uppgift")
        print("2. Visa alla uppgifter")
        print("3. Visa färdiga uppgifter")
        print("4. Visa ej färdiga uppgifter")
        print("5. Uppdatera status")
        print("6. Spara uppgifter")
        print("7. Stäng programmet")

        choice = input("Välj ett nummer: ")
        if choice == "1":
            title = input("Ange uppgiftens titel: ")
            description = input("Ange uppgiftens beskrivning: ")
            due_date = input("Ange datum för uppgiften (yyyy-mm-dd): ")
            add_task(title, description, due_date)

        elif choice == "2":
            display_tasks()

        elif choice == "3":
            display_tasks(show_completed=True)

        elif choice == "4":
            display_tasks(show_completed=False)

        elif choice == "5":
            try:
                index = int(input("Ange uppgiftens nummer som du vill uppdatera: ")) - 1
                status = input("Ange den nya statusen (under genomförande / komplett): ")
                update(index, status)
            except ValueError:
                print("Det nummer du angav är inte ett giltigt tal.")

        elif choice == "6":
            save_tasks()

        elif choice == "7":
            save_tasks()
            print("Programmet stängs.")
            break

        else:
            print("Vänligen välj ett giltigt nummer.")

main()
