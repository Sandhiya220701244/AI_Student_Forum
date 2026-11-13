

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0003_remove_question_closed'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='points',
            field=models.IntegerField(default=0),
        ),
    ]
