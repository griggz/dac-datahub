# Generated by Django 3.1.4 on 2020-12-24 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('job_title', models.CharField(blank=True, max_length=300, null=True)),
                ('organization', models.CharField(blank=True, max_length=300, null=True)),
                ('work_phone', models.IntegerField(blank=True, max_length=300, null=True)),
                ('web_site', models.CharField(blank=True, max_length=1000, null=True)),
                ('number_of_staff', models.IntegerField(blank=True, null=True)),
                ('industry', models.CharField(blank=True, max_length=300, null=True)),
                ('solution_option', models.CharField(blank=True, max_length=300, null=True)),
                ('contact_date', models.DateTimeField(auto_now_add=True)),
                ('method_of_referral', models.CharField(blank=True, max_length=300, null=True)),
                ('contact_source', models.CharField(blank=True, max_length=100, null=True)),
                ('additional_details', models.TextField(default='')),
            ],
        ),
    ]
