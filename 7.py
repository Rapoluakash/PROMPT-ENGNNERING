
#7. Using Prompt Templates with f-Strings

def generate_flexible_prompt(action,subject,tone):
    prompt=f"write a {tone} {action} about {subject}."
    return prompt 
    
action="story"
subject="thr first human on mars"
tone="adventures"
prompt=generate_flexible_prompt(action,subject,tone)
print("Generated Prompt:",prompt)