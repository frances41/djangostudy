# Generated by Django 2.2.3 on 2019-07-28 04:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='content',
            field=models.TextField(null=True),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='app.Board')),
            ],
        ),
    ]