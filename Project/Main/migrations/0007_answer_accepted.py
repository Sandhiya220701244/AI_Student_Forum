

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0006_answer_vote'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='accepted',
            field=models.IntegerField(default=0),
        ),
    ]
