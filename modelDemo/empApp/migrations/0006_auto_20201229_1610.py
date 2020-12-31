# Generated by Django 3.1.4 on 2020-12-29 10:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empApp', '0005_auto_20201229_1455'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=20)),
                ('lastName', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='project',
            name='programmers',
            field=models.ManyToManyField(to='empApp.Programmer'),
        ),
        migrations.CreateModel(
            name='License',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=10)),
                ('validFrom', models.DateField()),
                ('validTo', models.DateField()),
                ('person', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='empApp.person')),
            ],
        ),
    ]
