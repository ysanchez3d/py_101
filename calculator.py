import json

with open('calculator_messages.json', 'r') as file:
    data = json.load(file)

def prompt(message):
    print(f"==> {message}")

def invalid_number(number_str):
    try:
        int(number_str)
    except ValueError:
        return True

    return False

LANGUAGE = 'es'

def perform_calculation():
    prompt("What's the first number?")
    number1 = input()

    while invalid_number(number1):
        prompt("Hmm... that doesn't look like a valid number.")
        number1 = input()

    prompt("What's the second number?")
    number2 = input()

    while invalid_number(number2):
        prompt(messages("invalid", LANGUAGE))
        number2 = input()

    prompt(messages("operation", LANGUAGE))
    operation = input()

    while operation not in ["1", "2", "3", "4"]:
        prompt(messages("pick_operation", LANGUAGE))
        operation = input()

    match operation:
        case "1":
            output = int(number1) + int(number2)
        case "2":
            output = int(number1) - int(number2)
        case "3":
            output = int(number1) * int(number2)
        case "4":
            output = int(number1) / int(number2)

    prompt(f"The result is {output}")

    prompt(messages("new_calculation", LANGUAGE))
    answer = input()

    if answer == 'yes':
        perform_calculation()


def messages(message, lang='en'):
    return data[lang][message]

prompt(messages("welcome", LANGUAGE))
perform_calculation()