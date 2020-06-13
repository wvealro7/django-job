# Generated by Django 3.0.7 on 2020-06-13 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0008_auto_20200613_2017'),
    ]

    operations = [
        migrations.CreateModel(
            name='Applay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('website', models.URLField()),
                ('cv', models.FileField(upload_to='apply')),
                ('cover_letter', models.TextField()),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='apply_job', to='jobs.Job')),
            ],
        ),
    ]