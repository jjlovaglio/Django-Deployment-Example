# Generated by Django 3.1.1 on 2020-09-08 00:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0003_auto_20200908_0003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accessrecord',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='first_app.webpage'),
        ),
    ]