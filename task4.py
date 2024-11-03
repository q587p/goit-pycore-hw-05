def input_error(func):
    """Декоратор для обробки помилок введення користувача."""
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter the argument for the command."
        except KeyError:
            return "Contact not found."
    return inner

def main():
    contacts = {}
    print("Привіт! Я ваш асистент. Введіть 'hello' для початку.")

    while True:
        user_input = input("\nEnter a command: ").strip()
        command, *args = parse_input(user_input)

        if command in ["exit", "close"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

@input_error
def add_contact(args, contacts):
    """Додає контакт до словника."""
    if len(args) != 2:
        raise ValueError("Missing arguments")
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    """Змінює номер телефону для вказаного контакту."""
    if len(args) != 2:
        raise ValueError("Missing arguments")
    name, new_phone = args
    if name not in contacts:
        raise KeyError("Contact not found")
    contacts[name] = new_phone
    return "Contact updated."

@input_error
def show_phone(args, contacts):
    """Показує номер телефону для вказаного контакту."""
    if len(args) != 1:
        raise ValueError("Missing arguments")
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        raise KeyError("Contact not found")

@input_error
def show_all(contacts):
    """Показує всі контакти."""
    if not contacts:
        return "No contacts found."
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

def parse_input(user_input):
    """Розбирає введений рядок на команду та аргументи."""
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

if __name__ == "__main__":
    main()