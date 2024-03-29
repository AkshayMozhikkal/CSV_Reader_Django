# Generated by Django 5.0.2 on 2024-02-12 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bitcoin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('open', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('high', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('low', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('vol', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('change', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
            ],
        ),
    ]
