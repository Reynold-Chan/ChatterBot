from chatterbot import chatbot 
from chatterbot.trainers import ListTrainer

chatbot = Chatbot('GamingChatBot')
Training = ListTrainer(chatbot)
trainer.train(['How is your day today','What am I doing','Who are you'])

response = chatbot.get_response('my name is Reynold')
print(response)