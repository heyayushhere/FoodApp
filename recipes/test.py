

import openai
openai.api_key= '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'
def get_expiration_days_from_gpt(item_name):
    prompt = f"Estimate the expiration days for {item_name}."
    response = openai.Completion.create(
        engine="text-davinci-002",  # Use the appropriate engine
        prompt=prompt,
        max_tokens=50,  # Adjust based on your needs
        n=1,  # Number of completions
        stop=None,  # Optional: Specify a stopping condition
    )
    return response.choices[0].text.strip()
a=get_expiration_days_from_gpt("milk")
print(a)