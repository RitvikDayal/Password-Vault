# Generated by Django 3.1.1 on 2020-09-11 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vault', '0002_auto_20200912_0057'),
    ]

    operations = [
        migrations.AddField(
            model_name='credential',
            name='iv',
            field=models.CharField(default=b"\xc3\xef\xb5\x02s\x88\xb1\x8c\xfd\x17*k=\xb7'2", help_text='Do not alter/delete this field', max_length=200),
        ),
    ]