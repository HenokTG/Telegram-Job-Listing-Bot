from django.http import HttpResponse


def client_login(request):
    return HttpResponse("Hello, Please Log in. ")


def register_client(request):
    return HttpResponse("Hello, Please Fill the following fields and register. ")


def client_profile(request):
    return HttpResponse("This is Client Profile")


def client_profile_update(request):
    return HttpResponse("Lets update your profile")


def register_applicant(request):
    return HttpResponse("Hello, Applicant. Please Fill the following fields and register as applicant.")


def apllicant_profile_update(request):
    return HttpResponse("Oh, Do you came to update your profile? Go ahead fill the required.")


def confirm_applicant_registration(request):
    return HttpResponse("Hello, new bee. Welcome to Jobs Bot. Thank You for Registering")
