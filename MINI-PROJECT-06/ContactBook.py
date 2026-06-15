# Search contact by name or number
def search(contacts):
    """Search contact using name or number."""

    if not contacts:
        return "No contacts available"

    search_option = input("Do you want to search by 'number' or 'name': ").lower()

    # Search by name
    if search_option == "name":
        search_by_name = input("Enter the name that you want to search: ").lower()

        if search_by_name in contacts:
            return f"This is the number: {contacts[search_by_name]}"

        return f"you have nobody with the name {search_by_name} in your contacts"

    # Search by number
    elif search_option == "number":
        search_by_number = input("Enter the number: ")

        for key, value in contacts.items():
            if search_by_number == value:
                return f"This is the name of the number: {key}"

        return f"you have nobody with the number {search_by_number} in your contacts"

    return "We only search through number or name"


# Update contact number
def to_update(contacts):
    """Update contact number."""

    if not contacts:
        return "No contacts available"

    update_contact = input("Enter the name that you want to update: ").lower()

    if update_contact in contacts:

        number_for_update = input("Enter the number to update: ")

        if number_for_update in contacts.values():
            return "already exists!"

        contacts[update_contact] = number_for_update
        return "update was successful"

    return "You don't have anyone with that name in your contacts"


# Delete contact
def delete(contacts):
    """Delete contact from contact book."""

    if not contacts:
        return "No contacts available"

    to_delete = input("Enter name to delete: ").lower()

    if to_delete in contacts:
        contacts.pop(to_delete)
        return f"{to_delete} deleted successfully"

    return "you don't have anyone with that name"


contact_book = {}
is_running = True

while is_running:

    try:
        # Show menu
        choose = int(input("1.Add\n2.Search\n3.Update\n4.Delete\n5.Display all\n6.Exit\nWhat do you want: "))

    except ValueError:
        print("you need to choose only integers")
        continue

    # Add contact
    if choose == 1:

        to_add = True

        while to_add:

            name = input("Enter name to add: ").lower()

            if name in contact_book:
                print("you already have number with that name")

            else:
                number = input("Enter the number: ")

                if number in contact_book.values():
                    print("You already have the number!")

                else:
                    contact_book[name] = number

            # Ask to add another contact
            add_another = input("Do you want to add another contact? Type 'y' or 'n': ").lower()

            while add_another not in ["y", "n"]:
                add_another = input("Choose only between y or n: ").lower()

            if add_another == "n":
                to_add = False

    # Search contact
    elif choose == 2:
        print(search(contact_book))

    # Update contact
    elif choose == 3:
        print(to_update(contact_book))

    # Delete contact
    elif choose == 4:
        print(delete(contact_book))

    # Display contacts
    elif choose == 5:

        if not contact_book:
            print("No contacts yet")

        else:
            for key, value in contact_book.items():
                print(f"{key} : {value}")

    # Exit program
    elif choose == 6:
        is_running = False

    else:
        print("you need to choose between 1-6")