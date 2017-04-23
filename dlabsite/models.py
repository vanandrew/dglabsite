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

    blurb = models.TextField(
        verbose_name = "Blurb"
    )

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

# Create class for research
class research(models.Model):
    class Meta:
        verbose_name = "Research"
        verbose_name_plural = "Research"

    # Title of Research
    title = models.CharField(
        max_length = 350,
        unique = True,
        verbose_name = "Title"
    )

    # Description of Research
    description = models.TextField(
        verbose_name = "Description"
    )

    # Return the name of the model
    def __unicode__(self):
        return self.title

class research_image(models.Model):
    class Meta:
        verbose_name = "Research Image"

    # Create foreign key to research class
    research = models.ForeignKey(
        research,
        on_delete=models.CASCADE
    )

    # Image Caption
    caption = models.CharField(
        max_length = 350,
        blank = True,
        verbose_name = "Caption"
    )

    # Research Photos
    image = models.ImageField(
        upload_to='research_images/',
        null = True,
        blank = True,
        verbose_name = "Image"
    )

    # Return the name of the model
    def __unicode__(self):
        return self.image

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
    date = models. DateField(
        verbose_name = "Date Published"
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
        on_delete=models.CASCADE,
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
