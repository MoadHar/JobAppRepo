# Generated by Django 4.2.3 on 2023-07-27 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscribe', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscribe',
            name='option',
            field=models.CharField(choices=[('W', 'Weekly'), ('M', 'Monthly')], default='M', max_length=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='subscribe',
            name='email',
            field=models.EmailField(max_length=100),
        ),
    ]
