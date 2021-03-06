# Generated by Django 2.2b1 on 2019-02-14 18:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('creatorz', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.TextField()),
                ('lastname', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Playback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.CharField(choices=[('START', 'Customer starts playing'), ('STOP', 'Customer stops playing')], max_length=100)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='playbacks', to='creatorz.Album')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='playbacks', to='creatorz.Customer')),
            ],
        ),
    ]
