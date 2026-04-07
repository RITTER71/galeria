# Generated manually: add orientacion to match model

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fotos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='foto',
            name='orientacion',
            field=models.CharField(default='', editable=False, max_length=10),
            preserve_default=False,
        ),
    ]
