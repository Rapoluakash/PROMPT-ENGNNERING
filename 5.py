#5. Generating Multiple Prompts Dynamically 



def generate_prompts_from_data(data_list):
    prompts = []
    for item in data_list:
        prompt = f"Explain {item} in simple terms."
        prompts.append(prompt)
    return prompts

data_list = ["quantum computing", "machine learning", "climate change"]
prompts = generate_prompts_from_data(data_list)  # Corrected variable name

for prompt in prompts:  # Corrected loop variable
    print(prompt)
