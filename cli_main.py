import json
import os

def load_data():
    if os.path.exists("notes.json"):
        try:
            with open("notes.json", "r") as file:
                if os.stat("notes.json").st_size == 0:
                    return []
                return json.load(file)
        except json.JSONDecodeError:
            return []
    else:
        return []
    
notes = load_data()

def save_data(notes):
    with open("notes.json", "w") as file:
        json.dump(notes, file, indent=4)

def generate_id(notes):
    if not notes:
        return 1
    else:
        max_id = max(note["id"] for note in notes)
        return max_id + 1


def create_note(notes):
    title = input("Enter the title: ").strip()
    content = input("Enter the content: ").strip()

    # Validation
    if not title:
        print("Title cannot be empty!")
        return

    if not content:
        print("Content cannot be empty!")
        return

    # Generate ID
    new_id = generate_id(notes)

    # Create note
    note = {
        "id": new_id,
        "title": title,
        "content": content
    }

    # Add to list
    notes.append(note)

    # Save to file
    save_data(notes)

    print("Note created successfully!")

def view_notes(notes):
    if not notes:
        print("No notes available.")
        return

    print("\n--- Notes List ---")
    for note in notes:
        print(f"ID: {note['id']} | Title: {note['title']}")

def read_note(notes):
    if not notes:
        print("No notes available.")
        return

    try:
        note_id = int(input("Enter note ID: "))
    except ValueError:
        print("Invalid ID! Please enter a number.")
        return

    for note in notes:
        if note["id"] == note_id:
            print("\n--- Note Details ---")
            print(f"Title: {note['title']}")
            print(f"Content: {note['content']}")
            return

    print("Note not found!")

def edit_note(notes):
    if not notes:
        print("No notes available.")
        return

    try:
        note_id = int(input("Enter note ID to edit: "))
    except ValueError:
        print("Invalid ID!")
        return

    for note in notes:
        if note["id"] == note_id:
            new_title = input("Enter new title: ").strip()
            new_content = input("Enter new content: ").strip()

            if new_title:
                note["title"] = new_title
            if new_content:
                note["content"] = new_content

            save_data(notes)
            print("Note updated successfully!")
            return

    print("Note not found!")

def delete_note(notes):
    if not notes:
        print("No notes available.")
        return

    try:
        note_id = int(input("Enter note ID to delete: "))
    except ValueError:
        print("Invalid ID!")
        return

    for i, note in enumerate(notes):
        if note["id"] == note_id:
            confirm = input("Are you sure you want to delete? (y/n): ").lower()

            if confirm == "y":
                notes.pop(i)
                save_data(notes)
                print("Note deleted successfully!")
            else:
                print("Deletion cancelled.")
            return

    print("Note not found!")


def show_menu():
    print("\n--- Note Taking App ---")
    print("1. Create Note")
    print("2. View Notes")
    print("3. Read Note")
    print("4. Edit Note")
    print("5. Delete Note")
    print("6. Exit")


def main():
    notes = load_data()

    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            create_note(notes)

        elif choice == "2":
            view_notes(notes)

        elif choice == "3":
            read_note(notes)

        elif choice == "4":
            edit_note(notes)

        elif choice == "5":
            delete_note(notes)

        elif choice == "6":
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()



    

