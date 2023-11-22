# Generated by Django 4.2.7 on 2023-11-21 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('task_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('task_name', models.CharField(max_length=255)),
                ('next_task_id', models.EmailField(max_length=254)),
                ('previous_task_id', models.CharField(max_length=255)),
            ],
        ),
    ]