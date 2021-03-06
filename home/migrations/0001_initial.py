# Generated by Django 3.0.5 on 2020-05-30 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('position', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=15)),
                ('short_bio', models.CharField(max_length=200)),
                ('profile', models.ImageField(default='empty.jpg', upload_to='images/')),
            ],
        ),
    ]
