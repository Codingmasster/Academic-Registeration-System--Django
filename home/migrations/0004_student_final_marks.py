# Generated by Django 5.0.2 on 2024-03-12 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_product_delete_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='final_marks',
            field=models.IntegerField(default=0),
        ),
    ]
