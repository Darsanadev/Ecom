# Generated by Django 4.2.4 on 2024-02-01 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontnd', '0002_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=100, null=True)),
                ('productname', models.CharField(blank=True, max_length=100, null=True)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('totalprice', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
