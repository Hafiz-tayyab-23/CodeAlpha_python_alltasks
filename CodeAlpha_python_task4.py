# TASK 4: Basic Chatbot 
# ● Goal: Build a simple rule-based chatbot. 
# ● Scope: 
# ○ Input from user like: "hello", "how are you", "bye". 
# ○ Predefined replies like: "Hi!", "I'm fine, thanks!", "Goodbye!". 
# ● Key Concepts Used: if-elif, functions, loops, input/output.

# Function to generate chatbot replies based on user input
def chatbot_reply(user_input):
    # Normalize input to lowercase and remove extra spaces
    user_input = user_input.lower().strip()
    if user_input in ["hello", "hi"]:
        return "Hi!"
    elif user_input in ["how are you", "how are you?"]:
        return "I'm fine, thanks!"
    elif user_input in ["bye", "goodbye"]:
        return "Goodbye!"
    # Default response for unknown input
    else:
        return "Sorry, I don't understand."


# Main loop for interacting with the chatbot
print("Welcome to the Chatbot! Type 'bye' to exit.")
while True:
    user = input("You: ")
    reply = chatbot_reply(user)
    print("Bot:", reply)
    if reply == "Goodbye!":
        break
