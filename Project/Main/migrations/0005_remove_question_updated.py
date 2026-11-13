

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0004_profile_points'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='updated',
        ),
    ]
