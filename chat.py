from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

class Chat_T:
    chatbot: None

    def __init__(self):
        self.chatbot = ChatBot("ChatBot")
    # Training with Personal Ques & Ans
        conversation = [
            "Is the weather good today?",
            "The weather is very nice",
            "What color is the grass?",
            "Green",
            "What is your name?",
            "It is very nice to meet you",
            "it is nice to meet you",
            "when do you go to bed",
            "midnight",
            "when do you wake up",
            "in the morning"
        ]
        trainer = ListTrainer(self.chatbot)
        trainer.train(conversation)

    def chat(self, t1):
        response = self.chatbot.get_response(t1)
        return response