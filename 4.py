
#create prompt using templates

def create_summary_prompt(text):
    prompt_templet="Summarize the following text:{text}"

    return prompt_templet.format(text=text)


input_text="AI is repidly chang the way work,communicate ,solve the problems."
summary_prompt=create_summary_prompt(input_text)
print("Generate Summary Prompt:",summary_prompt)
