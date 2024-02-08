# Generated by Django 4.2.7 on 2024-01-31 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rovers', '0008_rename_rover_id_using_rover_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='using',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='rover',
            name='equipment',
            field=models.TextField(help_text='Через запятую с большой буквы', null=True),
        ),
    ]