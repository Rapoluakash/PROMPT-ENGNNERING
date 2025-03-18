topics=["artificial intelligence","space exploration","ancinent histotry"]
tones=["serious","humorous"]

prompts=[]
for topic in topics:
    for tone in tones:
        prompt =f"write a {tone} story about {topic}."
        prompts.append(prompt)



for prompt in prompts:
    print(prompt)




