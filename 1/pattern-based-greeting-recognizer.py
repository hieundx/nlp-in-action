import re

# Fuzzy regex that matches mispellings of "hello", "hey", "hi", "howdy", "greetings"
r = re.compile(r'(?i)^(h[aei]+(y|llo)?|h[aeou]w?d+y|gre+t?s?)', re.IGNORECASE)

user_statement = input("Enter your statement: ")
user_tokens = user_statement.split()
if any(r.match(token) for token in user_tokens):
    bot_reply = 'Thermonuclear war is a strange game.'
    bot_reply += ' The only winning move is not to play.'
else:
    bot_reply = 'Would you like a cup of tea?'
    
print(bot_reply)