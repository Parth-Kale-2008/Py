import tiktoken

enc = tiktoken.get_encoding("cl100k_base")

for text in ["hello world", "नमस्ते दुनिया", "hallowelt"]:
    print(f"{len(enc.encode(text))} tokens | {text}")