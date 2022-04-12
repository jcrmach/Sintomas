# Generated by Django 4.0.3 on 2022-04-08 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bigdoc', '0002_peso_rename_doencas_doenca_rename_sintomas_sintoma_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diagnostico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('peso', models.PositiveSmallIntegerField(choices=[(1, 'Muito Raro'), (2, 'Raro'), (3, 'Pouco Comum'), (4, 'Comum'), (5, 'Muito Comum')])),
            ],
        ),
        migrations.RemoveField(
            model_name='doenca',
            name='sintomas',
        ),
        migrations.DeleteModel(
            name='Peso',
        ),
        migrations.AddField(
            model_name='diagnostico',
            name='doenca',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pesos', to='bigdoc.doenca'),
        ),
        migrations.AddField(
            model_name='diagnostico',
            name='sintoma',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pesos', to='bigdoc.sintoma'),
        ),
    ]