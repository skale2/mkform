# Generated by Django 2.1 on 2018-08-22 20:55

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import picklefield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Boolean',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('value', models.NullBooleanField()),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BooleanDef',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('desc', models.TextField()),
                ('required', models.BooleanField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BooleanValidator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('message', models.CharField(default='Internal Error: This validator is abstract', max_length=255)),
                ('must_be', models.BooleanField()),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Checkbox',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CheckboxDef',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('desc', models.TextField()),
                ('required', models.BooleanField()),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CheckboxGridDef',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('desc', models.TextField()),
                ('required', models.BooleanField()),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('checkboxes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.Checkbox')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Date',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('value', models.DateField()),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DateDef',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('desc', models.TextField()),
                ('required', models.BooleanField()),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DateTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('value', models.DateTimeField()),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DateTimeDef',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('desc', models.TextField()),
                ('required', models.BooleanField()),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('value', models.FileField(upload_to='')),
                ('mimetype', models.CharField(choices=[('text/plain', 'Plain Text'), ('text/html', 'HTML'), ('text/css', 'CSS'), ('text/javascript', 'Javascript'), ('image/gif', 'GIF'), ('image/png', 'PNG'), ('image/png', 'PNG'), ('image/jpeg', 'JPEG'), ('image/bmp', 'BMP'), ('image/webp', 'WEBP'), ('audio/midi', 'MIDI'), ('audio/mpeg', 'MPEG'), ('audio/webm', 'WEBM'), ('audio/ogg', 'OGG'), ('audio/wav', 'WAV'), ('video/webm', 'WEBM'), ('video/ogg', 'OGG'), ('application/octet-stream', 'Octet Stream'), ('application/pkcs12', 'PKCS12'), ('application/vnd.mspowerpoint', 'MS Powerpoint'), ('application/xhtml+xml', 'XHTML XML'), ('application/xml', 'XML'), ('application/pdf', 'PDF'), ('multipart/form-data', 'Form Data')], max_length=30)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FileDef',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('desc', models.TextField()),
                ('required', models.BooleanField()),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('desc', models.TextField()),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LongAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('value', models.TextField()),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LongAnwserDef',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('desc', models.TextField()),
                ('required', models.BooleanField()),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MultipleChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MultipleChoiceDef',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('desc', models.TextField()),
                ('required', models.BooleanField()),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MultipleChoiceGridDef',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('desc', models.TextField()),
                ('required', models.BooleanField()),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Number',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('value', models.IntegerField()),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='NumberDef',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('desc', models.TextField()),
                ('required', models.BooleanField()),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RegexValidator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('message', models.CharField(default='Internal Error: This validator is abstract', max_length=255)),
                ('regex', models.CharField(max_length=255)),
                ('contains', models.BooleanField(default=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.Form')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('index', models.SmallIntegerField()),
                ('desc', models.TextField()),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.Form')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ShortAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('value', models.CharField(max_length=255)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ShortAnwserDef',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('desc', models.TextField()),
                ('required', models.BooleanField()),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('regex_validator', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='forms.RegexValidator')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.Section')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SizeValidator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('message', models.CharField(default='Internal Error: This validator is abstract', max_length=255)),
                ('max_size', models.IntegerField(default=9223372036854775807)),
                ('min_size', models.IntegerField(default=-9223372036854775807)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('value', models.TimeField()),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TimeDef',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('desc', models.TextField()),
                ('required', models.BooleanField()),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.Section')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ChoiceDef',
            fields=[
                ('booleandef_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='forms.BooleanDef')),
            ],
            options={
                'abstract': False,
            },
            bases=('forms.booleandef',),
        ),
        migrations.CreateModel(
            name='DateTimeValidator',
            fields=[
                ('sizevalidator_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='forms.SizeValidator')),
                ('max_datetime', models.DateTimeField(default=datetime.datetime(9999, 12, 31, 23, 59, 59, 999999))),
                ('min_datetime', models.DateTimeField(default=datetime.datetime(1, 1, 1, 0, 0))),
            ],
            options={
                'abstract': False,
            },
            bases=('forms.sizevalidator',),
        ),
        migrations.CreateModel(
            name='DateValidator',
            fields=[
                ('sizevalidator_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='forms.SizeValidator')),
                ('max_date', models.DateField(default=datetime.date(9999, 12, 31))),
                ('min_date', models.DateField(default=datetime.date(1, 1, 1))),
            ],
            options={
                'abstract': False,
            },
            bases=('forms.sizevalidator',),
        ),
        migrations.CreateModel(
            name='FileValidator',
            fields=[
                ('sizevalidator_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='forms.SizeValidator')),
                ('accepted_types', picklefield.fields.PickledObjectField(editable=False)),
                ('max_bytes', models.BigIntegerField(default=10000000.0)),
                ('min_bytes', models.BigIntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
            bases=('forms.sizevalidator',),
        ),
        migrations.CreateModel(
            name='TimeValidator',
            fields=[
                ('sizevalidator_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='forms.SizeValidator')),
                ('max_time', models.TimeField(default=datetime.time(23, 59, 59, 999999))),
                ('min_time', models.TimeField(default=datetime.time(0, 0))),
            ],
            options={
                'abstract': False,
            },
            bases=('forms.sizevalidator',),
        ),
        migrations.AddField(
            model_name='time',
            name='definition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.TimeDef'),
        ),
        migrations.AddField(
            model_name='time',
            name='response',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.Response'),
        ),
        migrations.AddField(
            model_name='time',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.Section'),
        ),
        migrations.AddField(
            model_name='sizevalidator',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='shortanwserdef',
            name='size_validator',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='forms.SizeValidator'),
        ),
        migrations.AddField(
            model_name='shortanswer',
            name='definition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.ShortAnwserDef'),
        ),
        migrations.AddField(
            model_name='shortanswer',
            name='response',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.Response'),
        ),
        migrations.AddField(
            model_name='shortanswer',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.Section'),
        ),
        migrations.AddField(
            model_name='numberdef',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.Section'),
        ),
        migrations.AddField(
            model_name='numberdef',
            name='size_validator',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='forms.SizeValidator'),
        ),
        migrations.AddField(
            model_name='number',
            name='definition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.NumberDef'),
        ),
        migrations.AddField(
            model_name='number',
            name='response',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.Response'),
        ),
        migrations.AddField(
            model_name='number',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.Section'),
        ),
        migrations.AddField(
            model_name='multiplechoicegriddef',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.Section'),
        ),
        migrations.AddField(
            model_name='multiplechoicedef',
            name='grid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='multiple_choices', to='forms.MultipleChoiceGridDef'),
        ),
        migrations.AddField(
            model_name='multiplechoicedef',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.Section'),
        ),
        migrations.AddField(
            model_name='multiplechoice',
            name='definition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.MultipleChoiceDef'),
        ),
        migrations.AddField(
            model_name='multiplechoice',
            name='response',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.Response'),
        ),
        migrations.AddField(
            model_name='multiplechoice',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.Section'),
        ),
        migrations.AddField(
            model_name='longanwserdef',
            name='regex_validator',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='forms.RegexValidator'),
        ),
        migrations.AddField(
            model_name='longanwserdef',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.Section'),
        ),
        migrations.AddField(
            model_name='longanwserdef',
            name='size_validator',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='forms.SizeValidator'),
        ),
        migrations.AddField(
            model_name='longanswer',
            name='definition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.LongAnwserDef'),
        ),
        migrations.AddField(
            model_name='longanswer',
            name='response',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.Response'),
        ),
        migrations.AddField(
            model_name='longanswer',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.Section'),
        ),
        migrations.AddField(
            model_name='filedef',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.Section'),
        ),
        migrations.AddField(
            model_name='file',
            name='definition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.FileDef'),
        ),
        migrations.AddField(
            model_name='file',
            name='response',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.Response'),
        ),
        migrations.AddField(
            model_name='file',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.Section'),
        ),
        migrations.AddField(
            model_name='datetimedef',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.Section'),
        ),
        migrations.AddField(
            model_name='datetime',
            name='definition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.DateTimeDef'),
        ),
        migrations.AddField(
            model_name='datetime',
            name='response',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.Response'),
        ),
        migrations.AddField(
            model_name='datetime',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.Section'),
        ),
        migrations.AddField(
            model_name='datedef',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.Section'),
        ),
        migrations.AddField(
            model_name='date',
            name='definition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.DateDef'),
        ),
        migrations.AddField(
            model_name='date',
            name='response',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.Response'),
        ),
        migrations.AddField(
            model_name='date',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.Section'),
        ),
        migrations.AddField(
            model_name='choice',
            name='multiple_choices',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.MultipleChoice'),
        ),
        migrations.AddField(
            model_name='choice',
            name='response',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.Response'),
        ),
        migrations.AddField(
            model_name='choice',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.Section'),
        ),
        migrations.AddField(
            model_name='choice',
            name='value',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.Boolean'),
        ),
        migrations.AddField(
            model_name='checkboxgriddef',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.Section'),
        ),
        migrations.AddField(
            model_name='checkboxdef',
            name='grid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='checkboxes', to='forms.CheckboxGridDef'),
        ),
        migrations.AddField(
            model_name='checkboxdef',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.Section'),
        ),
        migrations.AddField(
            model_name='checkbox',
            name='definition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.CheckboxDef'),
        ),
        migrations.AddField(
            model_name='checkbox',
            name='response',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.Response'),
        ),
        migrations.AddField(
            model_name='checkbox',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.Section'),
        ),
        migrations.AddField(
            model_name='booleandef',
            name='boolean_validator',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='forms.BooleanValidator'),
        ),
        migrations.AddField(
            model_name='booleandef',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='booleandef',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.Section'),
        ),
        migrations.AddField(
            model_name='boolean',
            name='definition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.BooleanDef'),
        ),
        migrations.AddField(
            model_name='boolean',
            name='response',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.Response'),
        ),
        migrations.AddField(
            model_name='boolean',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.Section'),
        ),
        migrations.AddField(
            model_name='timedef',
            name='time_validator',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='forms.TimeValidator'),
        ),
        migrations.AddField(
            model_name='filedef',
            name='file_validator',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='forms.FileValidator'),
        ),
        migrations.AddField(
            model_name='datetimedef',
            name='datetime_validator',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='forms.DateTimeValidator'),
        ),
        migrations.AddField(
            model_name='datedef',
            name='date_validator',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='forms.DateValidator'),
        ),
        migrations.AddField(
            model_name='choicedef',
            name='checkbox',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='forms.CheckboxDef'),
        ),
        migrations.AddField(
            model_name='choicedef',
            name='multiple_choice',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='forms.MultipleChoiceDef'),
        ),
        migrations.AddField(
            model_name='choice',
            name='definition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.ChoiceDef'),
        ),
    ]
