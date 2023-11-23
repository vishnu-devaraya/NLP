from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('MyBot')
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train('chatterbot.corpus.english')

def chat_with_bot():
    print("Bot: Hello! How can I assist you today?")

# Greet the user before starting the conversation
chat_with_bot()

while True:
    user_input = input("You: ")

    if user_input.lower() == 'exit':
        print('Bot: Goodbye!')
        break

    response = chatbot.get_response(user_input)
    print("Bot:", response)
