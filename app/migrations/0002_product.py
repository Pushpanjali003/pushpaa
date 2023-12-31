# Generated by Django 4.2.6 on 2023-11-22 11:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pr_image', models.ImageField(upload_to='gallery')),
                ('pr_name', models.CharField(max_length=20)),
                ('pr_price', models.IntegerField(default=0)),
                ('pr_des', models.TextField()),
                ('cat_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.category')),
            ],
        ),
    ]
