from __future__ import unicode_literals
import os
from django.db import models

# Create class for smart quotes
class smart_quote(models.Model):
    class Meta:
        verbose_name = "Smart Quote"

    # quote
    quote = models.CharField(
        max_length = 1000,
        verbose_name = "Quote"
    )

    # Return the name of the model
    def __unicode__(self):
        return self.quote

# Create class for news item
class news_item(models.Model):
    class Meta:
        verbose_name = "News Item"

    # title of news item
    title = models.CharField(
        max_length = 350,
        verbose_name = "Title"
    )

    # date of news item
    date = models.DateField(
        verbose_name = "Date"
    )

    # URL for news item
    URL = models.CharField(
        max_length = 350,
        verbose_name = "URL"
    )

    # Return the name of the model
    def __unicode__(self):
        return self.title

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
        #get_latest_by = "pub_title"

    # Publication Title
    title = models.CharField(
        max_length = 350,
        unique = True,
        verbose_name = "Publication Title"
    )

    # Publication Container
    container = models.TextField(
        verbose_name = "Citation"
    )

    # Publication Index
    idx = models.IntegerField(
        unique = True,
        verbose_name = "Index Number"
    )

    # Return the name of the model
    def __unicode__(self):
        return self.title + ' - ' + str(self.idx)

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
