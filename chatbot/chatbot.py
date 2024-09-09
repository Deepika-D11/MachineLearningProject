import streamlit as st
from nltk.chat.util import Chat, reflections

# Define pairs for chatbot responses
pairs = [
    [
        r"(.*)my name is (.*)",
        ["Hello %2, How are you today ?"]
    ],
    [
        r"(.*)help(.*) ",
        ["I can help you "]
    ],
    [
        r"(.*) your name ?",
        ["My name is thecleverprogrammer, but you can just call me robot and I'm a chatbot."]
    ],
    [
        r"how are you (.*) ?",
        ["I'm doing very well", "I am great!"]
    ],
    [
        r"sorry (.*)",
        ["It's alright", "It's OK, never mind that"]
    ],
    [
        r"i'm (.*) (good|well|okay|ok)",
        ["Nice to hear that", "Alright, great!"]
    ],
    [
        r"(hi|hey|hello|hola|holla)(.*)",
        ["Hello", "Hey there"]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse"]
    ],
    [
        r"(.*)created(.*)",
        ["Noor Saeed created me using Python's NLTK library", "Top secret ;)"]
    ],
    [
        r"(.*) (location|city) ?",
        ['Dera Ismail Khan, KPK']
    ],
    [
        r"(.*)raining in (.*)",
        ["No rain in the past 4 days here in %2", "In %2 there is a 50% chance of rain"]
    ],
    [
        r"how (.*) health (.*)",
        ["Health is very important, but I am a computer, so I don't need to worry about my health."]
    ],
    [
        r"(.*)(sports|game|sport)(.*)",
        ["I'm a very big fan of Cricket."]
    ],
    [
        r"who (.*) (Cricketer|Batsman)?",
        ["Babir Azam"]
    ],
    [
        r"quit",
        ["Bye for now. See you soon :)", "It was nice talking to you. See you soon :)"]
    ],
    [
        r"(.*)",
        ["That is nice to hear"]
    ]
]

# Custom reflections (optional)
my_dummy_reflections = {
    "go": "gone",
    "hello": "hey there"
}

# Initialize the chatbot
chatbot = Chat(pairs, reflections)


# Streamlit app
def main():
    st.title("Chatbot Application")
    st.write(
        "Hi, I'm DeepuDeshmukh, and I like to chat. Please type lowercase English language to start a conversation. Type 'quit' to leave.")

    # Chatbot interaction
    user_input = st.text_input("You: ", "")

    if st.button("Send"):
        if user_input.lower() == "quit":
            st.write("Chatbot: Bye for now. See you soon :)")
        else:
            response = chatbot.respond(user_input)
            st.write(f"Chatbot: {response}")


# Run the app
if __name__ == "__main__":
    main()
