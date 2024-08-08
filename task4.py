def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter a valid command."
        except ValueError:
            return "Enter the argument for the command."
        except IndexError:
            return "Give me both name and phone number."

    return inner


contacts = {}


@input_error
def add_contact(args):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args):
    name, new_phone_number = args

    if name in contacts:
        contacts[name] = new_phone_number
        return f"Contact {name} updated."
    else:
        return f"Contact {name} not found."


@input_error
def show_phone(args):
    name = args[0]
    return contacts.get(name, "Contact not found.")


@input_error
def show_all():
    if not contacts:
        return "No contacts available."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())


@input_error
def delete_contact(args):
    name = args[0]
    if name in contacts:
        del contacts[name]
        return "Contact deleted."
    return "Contact not found."


def parse_input(user_input):
    cmd, *args = user_input.split(' ')
    cmd = cmd.strip().lower()

    return cmd, *args


def main():
    print("Welcome to Assistant Bot!")
    print("Available commands:")
    print("- hello")
    print("- add [name] [phone_number]")
    print("- change [name] [new_phone_number]")
    print("- phone [name]")
    print("- all (to show all contacts)")
    print("- exit (or close to exit)")

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args))
        elif command == "change":
            print(change_contact(args))
        elif command == "phone":
            print(show_phone(args))
        elif command == "all":
            print(show_all())
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
