# Generated by Django 2.1 on 2018-08-23 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0002_auto_20180823_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booleandef',
            name='desc',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='booleandef',
            name='required',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='checkboxdef',
            name='desc',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='checkboxdef',
            name='required',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='checkboxgriddef',
            name='desc',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='checkboxgriddef',
            name='required',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='datedef',
            name='desc',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='datedef',
            name='required',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='datetimedef',
            name='desc',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='datetimedef',
            name='required',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='filedef',
            name='desc',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='filedef',
            name='required',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='form',
            name='desc',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='longanswerdef',
            name='desc',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='longanswerdef',
            name='required',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='multiplechoicedef',
            name='desc',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='multiplechoicedef',
            name='required',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='multiplechoicegriddef',
            name='desc',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='multiplechoicegriddef',
            name='required',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='numberdef',
            name='desc',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='numberdef',
            name='required',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='section',
            name='desc',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='shortanswerdef',
            name='desc',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='shortanswerdef',
            name='required',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='timedef',
            name='desc',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='timedef',
            name='required',
            field=models.BooleanField(default=False),
        ),
    ]
