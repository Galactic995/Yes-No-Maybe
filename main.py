#Yes-No-Maybe
#This program allows the user to ask yes-no-maybe questions and receive a random response. The user can exit the program by typing "quit" or "exit". The program also checks if the input is a question by looking for a "?" character.

import random # Import the random module to generate random responses

def yes_no_maybe(): # Function to return a random response of "Yes", "No", or "Maybe"
    responses = ["Yes", "No", "Maybe"]
    return random.choice(responses)

def question(): # Function to prompt the user for a question and provide a response
    while True:
        question = input('Ask a yes-no-maybe question(type "quit" or "exit" to quite program): ')
        
        if question.lower() in ["quit", "exit"]: # Check if the user wants to quit the program
            print("Goodbye!")
            break
        
        if "?" not in question: # Check if the input is a question by looking for a "?" character
            print('That is not a question, use "?" to ask a question.')
            continue

        answer = yes_no_maybe() # Get a random response from the yes_no_maybe function
        print(f"The answer to your question is: {answer}")

def main(): # Main function to run the program
    print("Welcome to Yes-No-Maybe!")
    question()

if __name__ == "__main__": # Run the main function if this script is executed
    main()

    