from django.shortcuts import render
from django.contrib import messages

from .forms import OrderForm

# Create your views here.
def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There is nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form' : order_form,
        'stripe_public_key' : 'pk_test_51RT7XNQYzCqRJuvweCHetwqwxO9ToTlngh5RrX13kKNBZ1SB5sAQJUbS0maG0kJ8Vz4ulwt9yRPSP0toiDROyGJI00JhlE8an0',
        'client_secret' : 'test client secret',
    }
    return render(request, template, context)
