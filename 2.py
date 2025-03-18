def create_prompt():
    topic=input("what is topic of your stoty?")
    tone=input("Enter the tone(serious,humoros,adventuros,funny,sad):")

    prompt=f"Write a {tone} story about {topic}."
    return prompt


user_prompt=create_prompt()
print("Generated prompt:",user_prompt)
