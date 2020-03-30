from django.db import models

class About(models.Model):
    title = 'About'
    body = models.TextField(help_text = "This is the About section that appears on the front page. Populate it with your bio or a short blurb about yourself and the site."

class Calendar_event(models.Model):
    title = models.CharField(max_length=256)
    date = models.DateTimeField() 
    body = models.TextField()

class Newsletter_entry(models.Model):
    title = models.CharField(max_length=256)
    date = models.DateTimeField()
    body = models.TextField()

class Media(models.Model):
    title = models.CharField(max_length=200, help_text="Title your piece of media. This will appear next to the media as a label.")
    image = models.ImageField(upload_to='static/media')

class Background_image(models.Model):
    title = 'Background image'
    image = models.ImageField(upload_to='static/media', help_text="This image will appear as the main image behind the site's front page")

class Contact(models.Model):
    name = models.CharField(max_length=256)
    phone = models.CharField(max_length=256)
    email = models.CharField(max_length=256)

class Email_form_entry(models.Model):
    name = models.CharField(max_length=256)
    email = models.CharField(max_length=256)
