"""
    Вимоги до завдання:
    Програма повинна мати функцію main(), яка управляє основним циклом обробки команд.
Реалізуйте функцію parse_input(), яка розбиратиме введений користувачем рядок на команду та її аргументи. 
Команди та аргументи мають бути розпізнані незалежно від регістру введення.
Ваша програма повинна очікувати на введення команд користувачем та обробляти їх за допомогою відповідних функцій. 
В разі введення команди "exit" або "close", програма повинна завершувати виконання.
Напишіть функції обробники для різних команд, такі як add_contact(), change_contact(), show_phone() тощо.
Використовуйте словник Python для зберігання імен і номерів телефонів. Ім'я буде ключем, а номер телефону – значенням.
Ваша програма має вміти ідентифікувати та повідомляти про неправильно введені команди.
    Критерії оцінювання:
Бот повинен перебувати в нескінченному циклі, чекаючи команди користувача.
Бот завершує свою роботу, якщо зустрічає слова: "close" або "exit".
Бот не чутливий до регістру введених команд.
Бот приймає команди:
"hello", та відповідає у консоль повідомленням "How can I help you?"
"add username phone". За цією командою бот зберігає у пам'яті, наприклад у словнику, новий контакт. 
Користувач вводить ім'я username та номер телефону phone, обов'язково через пробіл.
"change username phone". За цією командою бот зберігає в пам'яті новий номер телефону phone для контакту username, що вже існує в записнику.
"phone username" За цією командою бот виводить у консоль номер телефону для зазначеного контакту username.
"all". За цією командою бот виводить всі збереженні контакти з номерами телефонів у консоль.
"close", "exit" за будь-якою з цих команд бот завершує свою роботу після того, як виведе у консоль повідомлення "Good bye!" та завершить своє виконання.
Логіка команд реалізована в окремих функціях і ці функції приймають на вхід один або декілька рядків та повертають рядок.
Вся логіка взаємодії з користувачем реалізована у функції main, всі print та input відбуваються тільки там.
"""

def main():
    contacts = {}                                                # dictionary to store contacts {name: phone number}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ").strip().lower()  # receiving input from the user and converting it to lowercase
        command, *args = parse_input(user_input)                 # splitting the input string into command and arguments

        if command == "exit" or command == "close":              # checking whether the user entered the "exit" or "close" command
            print("Good bye!")  
            break                                                # loop exit
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))                   # function call to add a contact
        elif command == "change":
            print(change_contact(args, contacts))                # call the function to change the phone number of the contact
        elif command == "phone":
            print(show_phone(args, contacts))                    # function call to output the contact's phone number
        elif command == "all":
            print(show_all(contacts))                            # function call to display all contacts
        else:
            print("Invalid command.")

def parse_input(user_input):
    cmd, *args = user_input.split()                              # splitting the input line into command and arguments
    cmd = cmd.strip().lower()                                    # removing extra spaces and converting the command to lower case
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args                                           # splitting arguments into name and phone number
    contacts[name] = phone                                       # adding a contact to the dictionary
    return "Contact added."

def change_contact(args, contacts):
    name, new_phone = args                                       # splitting arguments into name and new phone number
    if name in contacts:                                         # checking if the name exists in the dictionary
        contacts[name] = new_phone                               # changing the phone number for the specified contact
        return "Contact updated." 
    else:
        return "Contact not found."
    
def show_phone(args, contacts):
    name = args[0]                                                # getting name from arguments
    if name in contacts:                                          # checking if the name exists in the dictionary
        return f"Phone number for {name}: {contacts[name]}"       #outputting the phone number for the specified contact
    else:
        return "Contact not found."                               # message about an unsuccessful attempt to find a contact if the name is not found

def show_all(contacts):
    if contacts:                                                  # checking if the dictionary is not empty
        all_contacts = "\n".join(f"{name}: {phone}" for name, phone in contacts.items())  # creating a row with all contacts
        return all_contacts 
    else:
        return "No contacts saved."  
    
if __name__ == "__main__":
    main()
