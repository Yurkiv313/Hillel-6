# Generated by Django 4.2.5 on 2023-10-05 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("school", "0004_alter_group_curator"),
    ]

    operations = [
        migrations.AlterField(
            model_name="group",
            name="curator",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                to="school.teacher",
                to_field="name",
            ),
        ),
        migrations.AlterField(
            model_name="teacher",
            name="name",
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
