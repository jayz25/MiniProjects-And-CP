# Generated by Django 3.1.7 on 2021-04-09 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('content', models.TextField(blank=True)),
                ('completed', models.BooleanField(default=False)),
                ('created', models.DateField(default='2021-04-09')),
                ('due_date', models.DateField(default='2021-04-09')),
            ],
        ),
    ]
