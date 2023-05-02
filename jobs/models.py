import uuid

from django.db import models

from django.conf import settings
from django.utils import timezone


from bot_users.models import ClientProfile, ApplicantProfile


# Create or retrieve a default client placeholder on delete
def get_default_client():
    return ClientProfile.objects.get_or_create(client_name="deleted", email="unknown@deleted.com", phone=0)[0].id


# Create or retrieve a default applicant placeholder on delete6
def get_default_applicant():
    return ApplicantProfile.objects.get_or_create(applicant_name="deleted", email="unknown@deleted.com", phone=0)[0].id


class JobListings(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    post_time = models.DateTimeField(default=timezone.now)
    job_tile = models.CharField(max_length=144, null=True, blank=True)
    qualification = models.CharField(max_length=144, null=True, blank=True)
    focus_areas = models.CharField(max_length=144, null=True, blank=True)
    job_description = models.TextField(null=True, blank=True)
    no_open_positions = models.IntegerField(null=True, blank=True)
    no_of_applicants = models.IntegerField(null=True, blank=True)
    max_no_of_applicant = models.IntegerField(null=True, blank=True)
    last_submission_date = models.DateTimeField(null=True, blank=True)
    is_open = models.BooleanField(default=True)

    posting_client = models.ForeignKey(settings.AUTH_USER_MODEL,
                                       on_delete=models.SET_DEFAULT,
                                       default=get_default_client
                                       )

    class Meta:
        ordering = ('-post_time',)

    def __str__(self):
        return f'{self.job_tile} job post by {self.posting_client.client_name}'

# Create or retrieve a default job listing placeholder on delete


def get_default_job_listing():
    return JobListings.objects.get_or_create(job_tile="deleted job listing")[0].id


class JobApplicationTracker(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    applied_at = models.DateTimeField(default=timezone.now)
    job_title = models.CharField(max_length=144, null=True, blank=True)
    job_listing = models.ForeignKey(JobListings,
                                    on_delete=models.SET_DEFAULT,
                                    default=get_default_job_listing
                                    )
    applied_by = models.ForeignKey(ApplicantProfile,
                                   on_delete=models.SET_DEFAULT,
                                   default=get_default_applicant
                                   )
    applied_to = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   on_delete=models.SET_DEFAULT,
                                   default=get_default_client
                                   )
    status = models.CharField(max_length=144, null=True, blank=True)

    invited_for_interview = models.BooleanField(default=False)

    class Meta:
        ordering = ('-applied_at',)

    def __str__(self):
        return f'{self.job_title} job applied by {self.applied_by.applicant_name} to {self.applied_to.client_name}'
