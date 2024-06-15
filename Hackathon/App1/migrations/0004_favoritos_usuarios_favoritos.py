# Generated by Django 5.0.6 on 2024-06-15 10:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0003_remove_usuarios_contraseña'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favoritos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App1.curso')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favoritos_relacionados', to='App1.usuarios')),
            ],
            options={
                'verbose_name': 'Favorito',
                'verbose_name_plural': 'Favoritos',
                'db_table': 'Favoritos',
                'unique_together': {('usuario', 'curso')},
            },
        ),
        migrations.AddField(
            model_name='usuarios',
            name='favoritos',
            field=models.ManyToManyField(related_name='usuarios_favoritos', through='App1.Favoritos', to='App1.curso'),
        ),
    ]
