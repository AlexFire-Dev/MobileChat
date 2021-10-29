# Generated by Django 3.2.8 on 2021-10-29 21:02

import apps.base.services
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('oauth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('private', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Guild',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('created', models.DateField(auto_now_add=True)),
                ('poster', models.ImageField(blank=True, null=True, upload_to=apps.base.services.get_path_upload_poster, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg']), apps.base.services.validate_size_image])),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='guilds', to='oauth.authuser')),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
                ('banned', models.BooleanField(default=False)),
                ('guild', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='members', to='chat.guild')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='memberships', to='oauth.authuser')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users_messages', to='chat.member')),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='channels_messages', to='chat.channel')),
            ],
        ),
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=30, unique=True)),
                ('guild', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invitation_links', to='chat.guild')),
            ],
        ),
        migrations.AddField(
            model_name='channel',
            name='guild',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='channels', to='chat.guild'),
        ),
    ]
