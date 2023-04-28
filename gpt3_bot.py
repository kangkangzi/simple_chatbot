# Import OpenAI API
import openai

# Load OpenAI API key
with open("openai.key", "r") as file:
    openai.api_key = file.read().strip()

# Define function to ask questions
def question(sentence):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=sentence,
        temperature=0,
        max_tokens=60,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    return response["choices"][0]["text"]

# Define function to print the answer
def answer(sentence):
    print("Answer:", question(sentence))

# Define main function
def main():
    print("Welcome to the GPT-3 bot!")

    # Get the question number from terminal
    q_num = input("Question number: ")

    # Check if the question number is valid
    if q_num > 25:
        print("Too many questions!")
        exit()

    # Loop q_num times
    for i in range(int(q_num)):
        # Get the question from terminal
        q = input("Question: ")

        # Ask the question and print the answer
        answer(q)

    # Exit the program
    print("Goodbye!")
    exit()

# Execute main function
if __name__ == "__main__":
    main()