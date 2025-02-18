# Generated by Django 5.1.6 on 2025-02-18 13:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='createdAt',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='updatedAt',
            new_name='updated_at',
        ),
        migrations.AlterModelTable(
            name='user',
            table='users',
        ),
        migrations.CreateModel(
            name='WebLink',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('url', models.URLField(max_length=255)),
                ('category', models.CharField(choices=[('favorites', '개인즐겨찾기'), ('work', '업무 활용자료'), ('reference', '참고자료'), ('education', '교육 및 학습자료'), ('shared', '공유')], max_length=20)),
                ('image_url', models.URLField(blank=True, max_length=500, null=True)),
                ('shared', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_by', to='database.user')),
            ],
            options={
                'db_table': 'weblinks',
            },
        ),
    ]
