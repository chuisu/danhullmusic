from django.db import models

class About(models.Model):
    title = 'About'
    body = models.TextField(help_text = "This is the About section that appears on the front page. Populate it with your bio or a short blurb about yourself and the site.")

class CalendarEvent(models.Model):
    title = models.CharField(max_length=256)
    date = models.DateTimeField() 
    body = models.TextField()

class NewsletterEntry(models.Model):
    title = models.CharField(max_length=256)
    date = models.DateTimeField()
    body = models.TextField()

class Media(models.Model):
    title = models.CharField(max_length=200, help_text="Title your piece of media. This will appear next to the media as a label.")
    file = models.FileField(upload_to='static/uploads/mediamodel/')

class BackgroundImage(models.Model):
    title = 'Background image'
    file = models.FileField(upload_to='static/uploads/backgroundimagemodel/', help_text="This image will appear as the main image behind the site's front page")

class Contact(models.Model):
    name = models.CharField(max_length=256)
    phone = models.CharField(max_length=256)
    email = models.CharField(max_length=256)

class EmailFormEntry(models.Model):
    name = models.CharField(max_length=256)
    email = models.CharField(max_length=256)
