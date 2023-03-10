# Generated by Django 4.1.5 on 2023-01-04 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Command",
            fields=[
                ("command", models.AutoField(primary_key=True, serialize=False)),
                ("comand_name", models.CharField(max_length=50)),
                ("score", models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name="Players",
            fields=[
                ("player", models.AutoField(primary_key=True, serialize=False)),
                ("first_name", models.CharField(max_length=30)),
                ("last_name", models.CharField(max_length=30)),
                ("contact_info", models.CharField(max_length=30)),
                ("way", models.IntegerField()),
                ("throw_count", models.IntegerField()),
                ("avarege_score", models.FloatField()),
                (
                    "comand_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="tv_view.command",
                    ),
                ),
            ],
        ),
    ]
