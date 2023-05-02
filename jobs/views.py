from django.shortcuts import render
from django.http import HttpResponse, Http404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import (ListAPIView)
from rest_framework.permissions import AllowAny

from .models import JobListings, JobApplicationTracker
from bot_users.models import ClientProfile, ApplicantProfile

from .serializers import JobListingBotSerializer


# For DjangoREST - Telegram Bot Interactions


class JobListingBotView(ListAPIView):

    permission_classes = [AllowAny]
    serializer_class = JobListingBotSerializer
    queryset = JobListings.objects.all()


def process_job_application_request(request):

    return HttpResponse("Hello, I do process job applications.")


def send_application_mail(data):

    print(data)

    return None


def process_accepted_application(request):
    return HttpResponse("Hello, I do process interview acceptance report.")


def send_application_acceptance_mail(data):

    print(data)

    return None


# Django Template Views


def job_listings_by_client(request):
    return HttpResponse("List of Jobs Created by the Client")


def create_job_listing(request):
    return HttpResponse("Create Job Listing")


def job_application_tracker(request):
    return HttpResponse("Job Application Tracker")
