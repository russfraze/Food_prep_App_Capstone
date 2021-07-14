# Generated by Django 3.2.3 on 2021-07-14 19:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bigshop', '0002_auto_20210709_2307'),
    ]

    operations = [
        migrations.CreateModel(
            name='SavedListItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('amount', models.IntegerField()),
                ('unit', models.CharField(max_length=50)),
                ('aisle', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='saved_items', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]