# Generated by Django 5.1.2 on 2024-10-19 18:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_example_is_active_1_example_is_active_2_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='setting',
            old_name='offer',
            new_name='offers',
        ),
    ]
