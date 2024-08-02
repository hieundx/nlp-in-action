import re

# Regex pattern for word tokenization
pattern = r"(?<!\w)['']?[a-zA-Z]+(?:[''](?:s|ll|ve|re|m|t))?"

# Example text
text = "Trust me, though, the words were on their way, and when they arrived, Liesel would hold them in her hands like the clouds, and she'd wring them out, like the rain."

# Tokenize the text
for token in re.findall(pattern, text):
    print(token)