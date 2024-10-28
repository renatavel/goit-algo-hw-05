def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IndexError:
            return "Please provide the correct number of arguments: name nad phone."
        except ValueError:
            return "Provide me the correct information, please."
        except KeyError:
            return "Contact not found."
    return inner

@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    return cmd.strip().lower(), args

@input_error
def add_contact(args, contacts):
    name, phone = args  
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    name, new_phone = args  
    if name not in contacts:
        raise KeyError  
    contacts[name] = new_phone
    return "Contact updated."

@input_error
def show_phone(args, contacts):
    user_name = args[0]  
    return contacts[user_name] 

@input_error
def show_all(contacts):
    if not contacts:
        return "No contacts found."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())

@input_error
def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ").strip().lower()
        command, args = parse_input(user_input)

        match command:
            case "close" | "exit":
                print("Good bye!")
                break
            case "hello":
                print("How can I help you?")
            case "add":
                print(add_contact(args, contacts))
            case "change":
                print(change_contact(args, contacts))
            case "phone":
                print(show_phone(args, contacts))
            case "all":
                print(show_all(contacts))
            case _:
                print("Invalid command.")

if __name__ == "__main__":
    main()

