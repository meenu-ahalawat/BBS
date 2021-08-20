# Generated by Django 3.1.7 on 2021-08-09 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customerdetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('avail_bal', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='transectiondetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('deb_amt', models.IntegerField()),
                ('cr_amt', models.IntegerField()),
                ('ac_bal', models.IntegerField()),
            ],
        ),
    ]
