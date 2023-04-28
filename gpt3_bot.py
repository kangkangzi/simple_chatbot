# Import OpenAI API
import openai

# Load OpenAI API key
with open("openai.key", "r") as file:
    openai.api_key = file.read().strip()

# Define function to ask questions
def question(sentence):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": sentence}
        ],
        temperature=0,
        max_tokens=1024,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    return response['choices'][0]['message']['content']

# Define function to print the answer
def answer(sentence):
    print("\033[36m>Answer: \033[0m", question(sentence))
    print("-------------------------")

# Define main function
def main():
    print("Welcome to the GPT-3 bot!")
    print("-------------------------")

    # Get the question number from terminal
    q_num = input("Question number: ")
    q_num = int(q_num)

    # Check if the question number is valid
    if q_num > 25:
        print("Too many questions!")
        exit()

    # Loop q_num times
    for i in range(int(q_num)):
        # Get the question from terminal
        print("-------------------------")
        q = input("\033[35m>Question: \033[0m")

        # Ask the question and print the answer
        answer(q)

    # Exit the program
    print("Goodbye!")
    exit()

# Execute main function
if __name__ == "__main__":
    main()