from __future__ import unicode_literals
import os, datetime
from django.db import models

# Create class for lab member
class lab_member(models.Model):
    class Meta:
        verbose_name = "Lab Member"

    # last name of lab member
    first_name = models.CharField(
        max_length = 70,
        verbose_name = "First Name"
    )

    # last name of lab member
    last_name = models.CharField(
        max_length = 70,
        verbose_name = "Last Name"
    )

    # Email of lab member
    email = models.CharField(
        max_length = 254,
        null = True,
        blank = True,
        verbose_name = "Email"
    )

    # Phone number of lab member
    phone = models.CharField(
        max_length = 13,
        null = True,
        blank = True,
        verbose_name = "Phone"
    )

    # Index for title of lab member
    title = models.CharField(
        max_length = 70,
        null = True,
        blank = True,
        verbose_name = "Title"
    )

    # Field for member blurb
    blurb = models.TextField(
        verbose_name = "Blurb"
    )

    # Define if member is alumni
    alumni = models.BooleanField(
        verbose_name = "Lab Alumni"
    )

    # Photo of lab member
    photo = models.ImageField(
        upload_to='portraits/',
        null = True,
        blank = True,
        verbose_name = "Photo"
    )

    # Return the name of the model
    def __unicode__(self):
        return self.last_name + ', ' + self.first_name

# Create class for publication
class publication(models.Model):
    class Meta:
        verbose_name = "Publication"

    # Publication Title
    title = models.CharField(
        max_length = 350,
        unique = True,
        verbose_name = "Publication Title"
    )

    # Publication Container
    container = models.TextField(
        default = datetime.date.today,
        verbose_name = "Citation"
    )

    # Publication Date
    date = models.DateField(
        verbose_name = "Date Published"
    )

	# Paper Upload
    paper = models.FileField(
        upload_to = "papers/",
        null = True,
        blank = True,
        verbose_name = "Paper"
    )

    # Return the name of the model
    def __unicode__(self):
        return self.title

# Create class for publication links
class publication_link(models.Model):
    class Meta:
        verbose_name = "Publication Link"

    # Create foreign key to publication class
    publication = models.ForeignKey(
        publication,
        on_delete = models.CASCADE,
        verbose_name = "Publication Link"
    )

    # Publication Title
    link = models.CharField(
        max_length = 350,
        unique = True,
        verbose_name = "Link"
    )

    # Return the name of the model
    def __unicode__(self):
        return self.link

# Create class for job listing
class job_listing(models.Model):
    class Meta:
        verbose_name = "Job Listing"

    # Create Title for Job listing
    title = models.CharField(
        max_length = 350,
        verbose_name = "Title"
    )

    # Create Job post date
    post_date = models.DateField(
        auto_now_add = True,
        verbose_name = "Posting Date"
    )

    # Create Job ID
    jobid = models.IntegerField(
        verbose_name = "Job ID#"
    )
    
    # Create Job URL
    joburl = models.CharField(
        max_length = 1000,
        verbose_name = "Job URL",
        null = True,
        blank = True
    )

    # Create Job Description
    description = models.TextField(
        blank = True,
        null = True,
        verbose_name = "Description"
    )

    def __unicode__(self):
        return self.title + " - " + str(self.jobid)

# Create class for current study listing
class current_study(models.Model):
    class Meta:
        verbose_name = "Current Study"

    # Create title for Study
    title = models.CharField(
        max_length = 350,
        verbose_name = "Title"
    )

    # Create study description
    description = models.TextField(
        blank = True,
        null = True,
        verbose_name = "Description"
    )

    # create link to study form
    link = models.CharField(
        max_length = 1000,
        null = True,
        verbose_name = "Link"
    )

    # flier attachement
    flier = models.FileField(
        upload_to='attachments/',
        null = True,
        blank = True,
        verbose_name = "Flier"
    )

    def __unicode__(self):
        return self.title

# Create class for media listing
class media_listing(models.Model):
    class Meta:
        verbose_name = "Media Listing"

    # Create title for media listing
    title = models.CharField(
        max_length = 350,
        verbose_name = "Title"
    )

    # Create description for media listing
    description = models.TextField(
        blank = True,
        null = True,
        verbose_name = "Description"
    )

    # Create link to media listing
    link = models.CharField(
        max_length = 1000,
        null = True,
        verbose_name = "Link"
    )

    # Image for media listing
    image = models.ImageField(
        upload_to='media_listing_images/',
        null = True,
        blank = True,
        verbose_name = "Image"
    )

    # Publication Date
    date = models.DateField(
        verbose_name = "Date Published"
    )

    def __unicode__(self):
        return self.title

# Create class for data listing
class data_listing(models.Model):
    class Meta:
        verbose_name = "Data Listing"

    # Create title for data listing
    title = models.CharField(
        max_length = 350,
        verbose_name = "Title"
    )

    # Create description for data listing
    description = models.TextField(
        blank = True,
        null = True,
        verbose_name = "Description"
    )

    # create link to data listing
    link = models.CharField(
        max_length = 1000,
        null = True,
        verbose_name = "Link"
    )

    # image for data_listing
    image = models.ImageField(
        upload_to='data_listing_images/',
        null = True,
        blank = True,
        verbose_name = "Image"
    )

    def __unicode__(self):
        return self.title

# Create class for software listing
class software_listing(models.Model):
    class Meta:
        verbose_name = "Software Listing"

    # Create title for software listing
    title = models.CharField(
        max_length = 350,
        verbose_name = "Title"
    )

    # Create description for software listing
    description = models.TextField(
        blank = True,
        null = True,
        verbose_name = "Description"
    )

    # create link to software listing
    link = models.CharField(
        max_length = 1000,
        null = True,
        verbose_name = "Link"
    )

    # image for software listing
    image = models.ImageField(
        upload_to='software_listing_images/',
        null = True,
        blank = True,
        verbose_name = "Image"
    )

    def __unicode__(self):
        return self.title
