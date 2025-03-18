#6. Advanced Prompt Engineering

def create_stepwise_prompt(context):
    step1_prompt = f"Summarize this text: {context}"
    ai_summary = "This is a summary of the context."
    step2_prompt = f"Based on the summary: {ai_summary}, answer the following question: What are the key points?"
    return step1_prompt, step2_prompt

context = "Artificial intelligence became a pivotal technology in the 21st century..."
step1, step2 = create_stepwise_prompt(context)  # Fixed variable name

print("Step 1 Prompt:", step1)
print("Step 2 Prompt:", step2)  # Corrected variable name
