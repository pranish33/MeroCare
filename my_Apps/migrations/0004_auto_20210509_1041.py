# Generated by Django 3.1.3 on 2021-05-09 04:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_Apps', '0003_remove_doctor_bloodgroup'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='useremail',
            new_name='contactemail',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='username',
            new_name='contactname',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='userphonenumber',
            new_name='contactphonenumber',
        ),
    ]
