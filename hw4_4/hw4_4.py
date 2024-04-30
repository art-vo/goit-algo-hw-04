def main():
    contacts = {}                                                # словник для зберігання контактів {ім'я: номер телефону}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ").strip().lower()  # отримання введення від користувача та перетворення його у нижній регістр
        command, *args = parse_input(user_input)                 # розбиття введеного рядка на команду та аргументи

        if command == "exit" or command == "close":              # перевірка чи користувач ввів команду "exit" або "close"
            print("Good bye!")  
            break                                                # вихід з циклу
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))                   # виклик функції для додавання контакту
        elif command == "change":
            print(change_contact(args, contacts))                # виклик функції для зміни номера телефону контакту
        elif command == "phone":
            print(show_phone(args, contacts))                    # виклик функції для виведення номера телефону контакту
        elif command == "all":
            print(show_all(contacts))                            # виклик функції для виведення всіх контактів
        else:
            print("Invalid command.")

def parse_input(user_input):
    cmd, *args = user_input.split()                              # розділення введеного рядка на команду та аргументи
    cmd = cmd.strip().lower()                                    # видалення зайвих пробілів та перетворення команди у нижній регістр
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args                                           # розділення аргументів на ім'я та номер телефону
    contacts[name] = phone                                       # додавання контакту до словника
    return "Contact added."

def change_contact(args, contacts):
    name, new_phone = args                                       # розділення аргументів на ім'я та новий номер телефону
    if name in contacts:                                         # перевірка чи ім'я існує в словнику
        contacts[name] = new_phone                               # зміна номера телефону для зазначеного контакту
        return "Contact updated." 
    else:
        return "Contact not found."
    
def show_phone(args, contacts):
    name = args[0]                                                # отримання імені з аргументів
    if name in contacts:                                          # перевірка чи ім'я існує в словнику
        return f"Phone number for {name}: {contacts[name]}"       # виведення номера телефону для зазначеного контакту
    else:
        return "Contact not found."                               # повідомлення про невдалу спробу знайти контакт, якщо ім'я не знайдено

def show_all(contacts):
    if contacts:                                                  # перевірка чи словник не пустий
        all_contacts = "\n".join(f"{name}: {phone}" for name, phone in contacts.items())  # створення рядка з усіма контактами
        return all_contacts 
    else:
        return "No contacts saved."  
    
if __name__ == "__main__":
    main()
