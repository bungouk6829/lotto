# Generated by Django 3.1.4 on 2020-12-22 01:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20201222_0111'),
    ]

    operations = [
        migrations.AddField(
            model_name='information',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='information',
            name='call_attr',
            field=models.CharField(blank=True, choices=[('call', '상담전화했음'), ('bad', '진상고객'), ('wrong', '잘못된DB'), ('customer', '계약함')], max_length=80, null=True, verbose_name='상태'),
        ),
    ]
