# Generated by Django 2.1.4 on 2019-02-25 15:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie', models.CharField(default='', max_length=250)),
                ('show_number', models.CharField(default='', max_length=250)),
                ('row', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H')], max_length=3)),
                ('column', models.CharField(choices=[('s1', 's1'), ('s2', 's2'), ('s3', 's3'), ('s4', 's4'), ('s5', 's5'), ('s6', 's6'), ('s7', 's7'), ('s8', 's8'), ('s9', 's9'), ('s10', 's10')], max_length=4)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie', models.CharField(default='', max_length=150)),
                ('language', models.CharField(default='', max_length=250)),
                ('sno', models.IntegerField(default=0)),
                ('image', models.ImageField(blank=True, upload_to='movie_image')),
                ('videofile', models.FileField(null=True, upload_to='videos/', verbose_name='')),
            ],
        ),
        migrations.CreateModel(
            name='Theatre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=250)),
                ('city', models.CharField(default='', max_length=250)),
                ('seats', models.IntegerField(default=0)),
                ('first', models.CharField(default='', max_length=250)),
                ('second', models.CharField(default='', max_length=250)),
                ('third', models.CharField(default='', max_length=250)),
                ('available', models.IntegerField(default=0)),
                ('booked', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(default='', max_length=100)),
                ('city', models.CharField(default='', max_length=100)),
                ('phone', models.IntegerField(default=0)),
                ('website', models.URLField(default='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='book1',
            name='theatre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Theatre'),
        ),
    ]
