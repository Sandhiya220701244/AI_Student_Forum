

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0002_auto_20180730_1354'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='closed',
        ),
    ]
