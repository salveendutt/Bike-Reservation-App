# Generated by Django 4.1.7 on 2023-05-29 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bike_app', '0002_rename_isfix_bikeinfo_isbroken'),
    ]

    operations = [
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('user_accounts', models.ManyToManyField(related_name='workers', to='bike_app.useraccount')),
            ],
        ),
        migrations.AddField(
            model_name='useraccount',
            name='worker',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='bike_app.worker'),
        ),
    ]