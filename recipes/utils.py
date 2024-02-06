import openai
import re
from datetime import datetime, timedelta
from .models import PerishableItem

openai.api_key = ''

def get_expiration_days_from_gpt_and_save(item_name):
    prompt = f"Estimate the approx expiration days for the {item_name}."
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=100  # Adjust based on your needs
    )
    print(response.choices[0].text)
    
    # Use regular expression to extract the number of days from the response
    match = re.search(r'(\d+)-?(\d*)\s*days', response.choices[0].text)
    
    if match:
        # Extracted number of days
        days = int(match.group(1))
        
        # Save the estimated expiration days in the PerishableItem model
        #perishable_item = PerishableItem.objects.create(name=item_name, estimated_expiration_days=days)
        
        return days, item_name
    else:
        # Return a default value or handle the case when no match is found
        return 4, item_name