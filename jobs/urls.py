from django.urls import path

from .views import (job_listings_by_client, create_job_listing, job_application_tracker,
                    process_job_application_request, process_accepted_application, JobListingBotView)

urlpatterns = [
    # DjangoREST - TgBot API endpoints
    path('tg-bot-job-listing',
         JobListingBotView.as_view(), name='bot-listings'),
    path('tg-bot-apply-for-job',
         process_job_application_request, name='apply-for-job'),
    path('tg-bot-accept-application',
         process_accepted_application, name='accept-application'),
    # Django View Routes
    path("listings", job_listings_by_client, name="job-listings"),
    path("post-job", create_job_listing, name="post-jobs"),
    path("submitted-applications", job_application_tracker, name="job-applications"),
]
