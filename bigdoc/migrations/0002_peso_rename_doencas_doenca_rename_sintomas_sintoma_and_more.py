# Generated by Django 4.0.3 on 2022-04-07 19:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bigdoc', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Peso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.PositiveSmallIntegerField(choices=[(1, 'Muito Raro'), (2, 'Raro'), (3, 'Pouco Comum'), (4, 'Comum'), (5, 'Muito Comum')])),
            ],
        ),
        migrations.RenameModel(
            old_name='Doencas',
            new_name='Doenca',
        ),
        migrations.RenameModel(
            old_name='Sintomas',
            new_name='Sintoma',
        ),
        migrations.DeleteModel(
            name='Pesos',
        ),
        migrations.AddField(
            model_name='peso',
            name='doenca',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bigdoc.doenca'),
        ),
        migrations.AddField(
            model_name='peso',
            name='sintoma',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bigdoc.sintoma'),
        ),
    ]