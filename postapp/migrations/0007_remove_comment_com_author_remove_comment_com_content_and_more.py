# Generated by Django 4.2.1 on 2023-06-04 10:11

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('postapp', '0006_user_comment_block'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='com_author',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='com_content',
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='postapp.user'),
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_content',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='edited',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
