import stripe

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from basket.basket import Basket


@login_required
def BasketView(request):

    basket = Basket(request)
    total = str(basket.get_total_price())
    total = total.replace('.', '')
    total = int(total)

    stripe.api_key = 'sk_test_51IZc1lIufSawS3O8UOQIii1mCyuMgDzcZT2azj1M7balJsTqyYhNWPAm7CpwG2sr28yeR9eoKIIQL8qg369Dveou00z992GmB3'
    intent = stripe.PaymentIntent.create(
        amount=total,
        currency='gbp',
        metadata={'userid': request.user.id}
    )

    return render(request, 'payment/home.html', {'client_secret': intent.client_secret})
