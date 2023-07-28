# Generated by Django 4.2.3 on 2023-07-28 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('the_app', '0008_alter_location_state_alter_location_zip'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobpost',
            name='type',
            field=models.CharField(choices=[('Full Time', 'Full Time'), ('Part Time', 'Part Time')], default='Full Time', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='jobpost',
            name='description',
            field=models.TextField(),
        ),
    ]