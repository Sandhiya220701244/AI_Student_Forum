

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0008_auto_20180731_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='answer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.Answer'),
        ),
    ]
