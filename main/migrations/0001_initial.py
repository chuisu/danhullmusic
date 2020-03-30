# Generated by Django 3.0.4 on 2020-03-30 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(help_text='This is the About section that appears on the front page. Populate it with your bio or a short blurb about yourself and the site.')),
            ],
        ),
        migrations.CreateModel(
            name='BackgroundImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(help_text="This image will appear as the main image behind the site's front page", upload_to='static/uploads/backgroundimagemodel/')),
            ],
        ),
        migrations.CreateModel(
            name='CalendarEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('date', models.DateTimeField()),
                ('body', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('phone', models.CharField(max_length=256)),
                ('email', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='EmailFormEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('email', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Title your piece of media. This will appear next to the media as a label.', max_length=200)),
                ('file', models.FileField(upload_to='static/uploads/mediamodel/')),
            ],
        ),
        migrations.CreateModel(
            name='NewsletterEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('date', models.DateTimeField()),
                ('body', models.TextField()),
            ],
        ),
    ]