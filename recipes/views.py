# foodwaste/recipes/views.py
from django.shortcuts import render,redirect
from django.http import JsonResponse
import openai
from django.contrib import messages
from .forms import RecipeForm,PerishableItemForm
from .models import Recipe,PerishableItem

def generate_recipe(request):
    openai.api_key= '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'
    if request.method == 'POST':
        form = RecipeForm(request.POST)

        if form.is_valid():
            user_ingredients = form.cleaned_data['ingredients']
            dietary_preferences = form.cleaned_data['dietary_preferences']

            # Call OpenAI GPT-3 to generate a recipe based on the user's input
            prompt = f"Generate a recipe using the ingredients: {user_ingredients}, with dietary preferences: {dietary_preferences}."
            response = openai.Completion.create(
                engine="gpt-3.5-turbo-instruct",
                prompt=prompt,
                max_tokens=300
            )

            # Extract the generated recipe from the OpenAI response
            generated_recipe = response['choices'][0]['text']

            # Save the generated recipe to the database
            Recipe.objects.create(
                title=f"Generated Recipe - {user_ingredients}",
                ingredients=user_ingredients,
                instructions=generated_recipe
            )

            # Return the generated recipe as a JSON response
            return render(request, 'recipes/generate_recipe.html', {'form': form,'generated_recipe':generated_recipe})

    else:
        form = RecipeForm()

    return render(request, 'recipes/generate_recipe.html', {'form': form})

from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import PerishableItemForm
from .models import PerishableItem
from twilio.rest import Client

def send_whatsapp_message(body, to):
    account_sid = ''
    auth_token = ''
    twilio_phone_number = 'whatsapp:+14155238886'

    client = Client(account_sid, auth_token)
    message = client.messages.create(from_=twilio_phone_number, body=body, to=to)
    return message.sid

# Import necessary modules

from .utils import get_expiration_days_from_gpt_and_save
# Your existing view
def track_expiration(request):
    if request.method == 'POST':
        form = PerishableItemForm(request.POST)

        if form.is_valid():
            item_name = form.cleaned_data['name']
            a,b=get_expiration_days_from_gpt_and_save(item_name)
            print(a,b)
            # Save the perishable item to the database
            PerishableItem.objects.create(name=b, estimated_expiration_days=a)
            
            messages.success(request, f'Successfully added {item_name} to perishable items.')
            return redirect('track_expiration')

    else:
        form = PerishableItemForm()

    perishable_items = PerishableItem.objects.all()
    print(perishable_items)

    # Construct the message with the perishable items
    message_template = """
        🌽🥦🍅 Perishable Items Reminder 🍎🥑🍞

        Hello! Here's a reminder for your upcoming perishable items:
        """

    # Add the items dynamically
    for item in perishable_items:
        message_template += f"- {item.name}\n"

    # Add the static part of the message
    message_template += """
    Remember to check the expiration dates and use them before they expire! 🕰️

    Note: We will send you a reminder for expired items.

    Thank you! 🙌
    """

    # Send the message via WhatsApp
    # send_whatsapp_message(message_template, 'whatsapp:+919724309274')

    return render(request, 'recipes/track_expiration.html', {'form': form, 'perishable_items': perishable_items})



from django.shortcuts import render, redirect, get_object_or_404
from .models import PerishableItem

def delete_perishable_item(request, item_id):
   
    perishable_item = get_object_or_404(PerishableItem, pk=item_id)

   
    perishable_item.delete()

    
    return redirect('track_expiration')
