# Generated by Django 2.1.3 on 2018-11-16 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20181107_1608'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='discontinued',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]