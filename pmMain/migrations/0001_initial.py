# Generated by Django 2.1.2 on 2020-05-29 20:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Earnings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='default', max_length=100)),
                ('date', models.DateField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('comment', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Expenses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='default', max_length=100)),
                ('date', models.DateField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('comment', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Prop_Name',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prop_name', models.CharField(max_length=100, unique=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='properties', to='pmMain.Owner')),
            ],
        ),
        migrations.CreateModel(
            name='Reserve',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='default', max_length=100)),
                ('date', models.DateField()),
                ('direction', models.CharField(choices=[('IN', 'IN'), ('OUT', 'OUT')], default='IN', max_length=3)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('comment', models.CharField(max_length=100)),
                ('prop_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pmMain.Prop_Name')),
            ],
        ),
        migrations.CreateModel(
            name='Room_Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_no', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100, unique=True)),
                ('phone_no', models.CharField(max_length=16, unique=True)),
                ('rent', models.IntegerField()),
                ('key_deposit', models.IntegerField()),
                ('last_month', models.IntegerField()),
                ('active_room', models.BooleanField(default=True)),
                ('prop_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pmMain.Prop_Name')),
            ],
        ),
        migrations.CreateModel(
            name='Room_Transactions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='default', max_length=100)),
                ('date', models.DateField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('comment', models.CharField(max_length=100)),
                ('prop_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reserves', to='pmMain.Prop_Name')),
                ('room_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pmMain.Room_Info')),
            ],
        ),
        migrations.AddField(
            model_name='expenses',
            name='prop_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='expenses', to='pmMain.Prop_Name'),
        ),
        migrations.AddField(
            model_name='expenses',
            name='room_no',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='expenses', to='pmMain.Room_Info'),
        ),
        migrations.AddField(
            model_name='earnings',
            name='prop_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='earnings', to='pmMain.Prop_Name'),
        ),
        migrations.AddField(
            model_name='earnings',
            name='room_no',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='earnings', to='pmMain.Room_Info'),
        ),
    ]
