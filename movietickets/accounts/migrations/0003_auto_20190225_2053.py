# Generated by Django 2.1.4 on 2019-02-25 15:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20190225_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book1',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
