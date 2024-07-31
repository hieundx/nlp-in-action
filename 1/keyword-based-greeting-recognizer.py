# Keyword-based greeting recognizer
greetings = "Hi Hello Greets Hey Howdy".split()
user_statement = input("Enter your statement: ")
user_tokens = user_statement.split()
if any(greeting in user_tokens for greeting in greetings):
    bot_reply = 'Thermonuclear war is a strange game.'
    bot_reply += ' The only winning move is not to play.'
else:
    bot_reply = 'Would you like a cup of tea?'
    
print(bot_reply)