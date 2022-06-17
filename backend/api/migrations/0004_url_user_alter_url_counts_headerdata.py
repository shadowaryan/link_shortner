# Generated by Django 4.0.2 on 2022-06-11 10:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_url_counts'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='api.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='url',
            name='counts',
            field=models.IntegerField(),
        ),
        migrations.CreateModel(
            name='HeaderData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('header_data', models.CharField(max_length=2048)),
                ('url', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.url')),
            ],
        ),
    ]