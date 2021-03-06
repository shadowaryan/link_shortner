# Generated by Django 4.0.2 on 2022-06-18 21:00

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Redirect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('header_data', models.CharField(max_length=2048)),
                ('ip_address', models.CharField(max_length=32)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='url',
            name='counts',
        ),
        migrations.AddField(
            model_name='url',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='url',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.DeleteModel(
            name='HeaderData',
        ),
        migrations.AddField(
            model_name='redirect',
            name='url',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.url'),
        ),
    ]
