# Generated by Django 2.0.4 on 2018-05-18 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_by', models.CharField(max_length=30)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
