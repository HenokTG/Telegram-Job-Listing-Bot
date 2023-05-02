from django.urls import path

from .views import (client_login, register_client, client_profile, client_profile_update,
                    register_applicant, apllicant_profile_update, confirm_applicant_registration)

urlpatterns = [
    path("client-login", client_login, name="client-login"),
    path("client-registration", register_client, name="client-registration"),
    path("client-profile", client_profile, name="client-registration"),
    path("client-profile-update", client_profile_update,
         name="client-registration"),
    path("applicant-registration", register_applicant, name="register-applicant"),
    path("applicant-profile-update", apllicant_profile_update,
         name="client-registration"),
    path("confirm-applicant-registration",
         confirm_applicant_registration, name="confirm-applicant"),
]
