from django.contrib import messages
from django.shortcuts import render, redirect

from subscriptions.models import Subscription, Payment, SubPlan


# Create your views here.

def payment_taking(request):
    if request.method == "POST":
        selected_package = request.POST.get("package")
        if selected_package:
            match selected_package:
                case "min":
                    days_to_update = SubPlan.MINIMUM
                case "mid":
                    days_to_update = SubPlan.MIDDLE
                case _:
                    days_to_update = SubPlan.MAXIMUM
            subscription = Subscription.objects.get(user=request.user)
            payment = Payment(subscriptions=subscription, payment_plan=days_to_update)
            subscription.sub_update(days_to_update.value)
            subscription.save()
            payment.save()
            return redirect('authentication:user_details')
        messages.error(request, 'Choose an option')
        return render(request, 'payment.html')
    return render(request, 'payment.html')
