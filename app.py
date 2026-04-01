import streamlit as st
import json
import os

FILE_NAME = "notes.json"


# ------------------ DATA FUNCTIONS ------------------

def load_data():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                if os.stat(FILE_NAME).st_size == 0:
                    return []
                return json.load(file)
        except json.JSONDecodeError:
            return []
    return []


def save_data(notes):
    with open(FILE_NAME, "w") as file:
        json.dump(notes, file, indent=4)


def generate_id(notes):
    if not notes:
        return 1
    return max(note["id"] for note in notes) + 1


# ------------------ APP UI ------------------

st.title("📝 Note Taking App")

notes = load_data()

menu = st.sidebar.selectbox(
    "Menu",
    ["Create Note", "View Notes", "Read Note", "Edit Note", "Delete Note"]
)

# ------------------ CREATE ------------------

if menu == "Create Note":
    st.subheader("Create a New Note")

    title = st.text_input("Title")
    content = st.text_area("Content")

    if st.button("Save Note"):
        if not title or not content:
            st.warning("Title and Content cannot be empty!")
        else:
            note = {
                "id": generate_id(notes),
                "title": title,
                "content": content
            }
            notes.append(note)
            save_data(notes)
            st.success("Note created successfully!")

# ------------------ VIEW ------------------

elif menu == "View Notes":
    st.subheader("All Notes")

    if not notes:
        st.info("No notes available.")
    else:
        for note in notes:
            st.write(f"**ID:** {note['id']} | **Title:** {note['title']}")

# ------------------ READ ------------------

elif menu == "Read Note":
    st.subheader("Read Note")

    note_id = st.number_input("Enter Note ID", step=1)

    if st.button("Show Note"):
        for note in notes:
            if note["id"] == note_id:
                st.write(f"### {note['title']}")
                st.write(note["content"])
                break
        else:
            st.error("Note not found!")

# ------------------ EDIT ------------------

elif menu == "Edit Note":
    st.subheader("Edit Note")

    note_id = st.number_input("Enter Note ID to edit", step=1)

    for note in notes:
        if note["id"] == note_id:
            new_title = st.text_input("New Title", value=note["title"])
            new_content = st.text_area("New Content", value=note["content"])

            if st.button("Update Note"):
                note["title"] = new_title
                note["content"] = new_content
                save_data(notes)
                st.success("Note updated!")
            break
    else:
        st.info("Enter valid ID and press enter")

# ------------------ DELETE ------------------

elif menu == "Delete Note":
    st.subheader("Delete Note")

    note_id = st.number_input("Enter Note ID to delete", step=1)

    if st.button("Delete"):
        for i, note in enumerate(notes):
            if note["id"] == note_id:
                notes.pop(i)
                save_data(notes)
                st.success("Note deleted!")
                break
        else:
            st.error("Note not found!")