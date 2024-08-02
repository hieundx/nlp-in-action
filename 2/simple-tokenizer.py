text = "Trust me, though, the words were on their way, and when they arrived, Liesel would hold them in her hands like the clouds, and she would wring them out, like the rain"

words = text.split()
print(words[:5])

# Very simple tokenizer

comma_token = [token for token in words if ',' in token][0]
print('token with comma:', comma_token)
