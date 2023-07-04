'''
Chat Bot
-------------------------------------------------------------
1) pip install ChatterBot chatterbot-corpus spacy
2) python3 -m spacy download en_core_web_sm
   Or... choose the language you prefer
3) Navigate to your Python3 directory
4) Modify Lib/site-packages/chatterbot/tagging.py
  to properly load 'en_core_web_sm'
'''


from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


def create_chat_bot():
   chatbot = ChatBot('Chattering Bot')
   trainer = ChatterBotCorpusTrainer(chatbot)
   trainer.train('chatterbot.corpus.english')

   while True:
       try:
           bot_input = chatbot.get_response(input())
           print(bot_input)

       except (KeyboardInterrupt, EOFError, SystemExit):
           break


if __name__ == '__main__':
   create_chat_bot()

# Replace this:
self.nlp = spacy.load(self.language.ISO_639_1.lower())

# With this:
if self.language.ISO_639_1.lower() == 'en':
   self.nlp = spacy.load('en_core_web_sm')
else:
   self.nlp = spacy.load(self.language.ISO_639_1.lower())