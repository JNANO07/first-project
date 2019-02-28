import pickle
from time import sleep


ACTION_ADD_CONTACT = 1
ACTION_REMOVE_CONTACT = 2
ACTION_FIND_CONTACT = 3
ACTION_EXPORT_CONTACT = 4
ACTION_EXIT = 5

MENU_OPTIONS = [ACTION_ADD_CONTACT, ACTION_REMOVE_CONTACT, ACTION_FIND_CONTACT, ACTION_EXPORT_CONTACT, ACTION_EXIT]

SAVE_FILE_NAME = "contacts.save"


def ask_until_options_expeted(options):
    selected_option = " "

    while not selected_option.isdigit() or(selected_option.isdigit() and int(selected_option) not in options):
        selected_option = input("choose one:")
        return int(selected_option)


def show_menu():
    print("1 - add a contact.")
    print("2 - remove a contact.")
    print("3 - find a contact.")
    print("4 - export a contact")
    print("5 - exit")
    return ask_until_options_expeted(MENU_OPTIONS)


def add_contact(contacts):
    print("\n add a contact.")
    contact={
        "name": input("name:"),
        "phone": input("phone:"),
        "email": input("Email:")
    }
    contacts.append(contact)
    print("{} is add as contact.\n".format(contact["name"]))
    sleep(2)


def find_contact(contacts):

    found_contacts = []
    contact_counter = 0
    contact_indexes = []
    yes_no_quest = "Y"

    while yes_no_quest == "Y":

        search_term = input("enter the name of the contact to search:")

        for contact in contacts:
            if contact["name"].find(search_term) >= 0:
                found_contacts.append(contact)
                print("{} - {}".format(contact_counter, contact["name"]))
                contact_indexes.append(contact_counter)
                contact_counter += 1

                contact_index = 0

        if len(contact_indexes) > 1:
            contact_index = ask_until_options_expeted(contact_indexes)
            yes_no_quest = "N"
        elif len(contact_indexes) == 0:
            print("no found contacts\n")
            yes_no_quest=input("Do yo want to try again?:(Y/N)")
            if yes_no_quest == "N":
                return

    print("\nContact {}.\n".format(found_contacts[contact_index]["name"]))
    print("Name: {name}.\nPhone: {phone}.\nEmail: {email}.\n".format(**found_contacts[contact_index]))
    sleep(2)


def load_contacts():
    try:
        return pickle.load(open(SAVE_FILE_NAME, "rb"))
    except FileNotFoundError:
        return []


def save_contacts(contacts):
    with open(SAVE_FILE_NAME, "wb") as save_file:
        pickle.dump(contacts, save_file)
    print("contacts save.")


def export_contacts():
    pass


def remove_contact(contacts):

    search_term = input("enter the name of the contact to search:")

    found_contacts = []
    contact_counter = 0
    contact_indexes = []

    for contact in contacts:
        if contact["name"].find(search_term) >= 0:
            found_contacts.append(contact)
            print("{} - {}".format(contact_counter, contact["name"]))
            contact_indexes.append(contact_counter)
            contact_counter += 1

            contact_index = 0

    if len(contact_indexes) > 1:
       contact_index = ask_until_options_expeted(contact_indexes)
    elif len(contact_indexes) == 0:
        print("no found contacts\n")
        return

    del (contacts[contact_index])
    print("Contact delete.\n")
    sleep(2)


def main():

    contacts = load_contacts()
    print(contacts)
    action = show_menu()

    while action != ACTION_EXIT:
        if action == ACTION_ADD_CONTACT:
            add_contact(contacts)
        elif action == ACTION_REMOVE_CONTACT:
            remove_contact(contacts)
        elif action == ACTION_FIND_CONTACT:
            find_contact(contacts)
        elif action == ACTION_EXPORT_CONTACT:
            export_contacts()


        action = show_menu()
    save_contacts(contacts)
    print("god bye")


if __name__ == "__main__":
    main()
