# grocery/views.py
from django.shortcuts import render, redirect
from .forms import PerishableItemForm
from datetime import datetime, timedelta
from twilio.rest import Client

def send_whatsapp_message(body, to):
    account_sid = 'AC7a99f94d0cbed0961682b3ccd15fcad6'
    auth_token = 'c486768e02f7a48c78d5746f6bc96695'
    twilio_phone_number = 'whatsapp:+14155238886'

    client = Client(account_sid, auth_token)
    message = client.messages.create(from_=twilio_phone_number, body=body, to=to)
    return message.sid

def add_to_grocery_list(request):
    if request.method == 'POST':
        form = PerishableItemForm(request.POST)
        if form.is_valid():
            expiration_date = form.cleaned_data['expiration_date']
            # Process the form data as needed
            send_whatsapp_message(f"Item added: {form.cleaned_data['name']}, Expiry Date: {expiration_date}", 'whatsapp:+919724309274')
            return redirect('grocery_list')
    else:
        form = PerishableItemForm()

    return render(request, 'grocery/add_item.html', {'form': form})
