from django.contrib import admin

from .models import JobListings, JobApplicationTracker

admin.site.register(JobListings)
admin.site.register(JobApplicationTracker)
