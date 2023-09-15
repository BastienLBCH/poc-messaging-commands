# Generated by Django 4.2.4 on 2023-08-28 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instantMessages', '0005_usercreatedconversation_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraddedparticipanttoconversation',
            name='event',
            field=models.CharField(default='userAddedParticipantToConversation', max_length=100),
        ),
        migrations.AddField(
            model_name='userdeletedconversation',
            name='event',
            field=models.CharField(default='userDeletedConversation', max_length=100),
        ),
        migrations.AddField(
            model_name='userremovedparticipanttoconversation',
            name='event',
            field=models.CharField(default='userRemovedParticipantToConversation', max_length=100),
        ),
        migrations.AddField(
            model_name='usersentmessagetoconversation',
            name='event',
            field=models.CharField(default='userSentMessageToConversation', max_length=100),
        ),
    ]