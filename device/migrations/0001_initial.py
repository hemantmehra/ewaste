# Generated by Django 2.1.3 on 2018-11-18 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_type', models.CharField(choices=[('DW', 'Dishwasher'), ('TV', 'TV'), ('LP', 'Laptop'), ('RF', 'Refrigerator'), ('MS', 'Mouse'), ('KB', 'Keyboard'), ('HD', 'Hair Dryer'), ('PD', 'iPod'), ('MW', 'Microwave'), ('MP', 'Microphone'), ('RC', 'Remote Control')], max_length=2)),
                ('price', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Element',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Co', 'Copper'), ('Si', 'Silver'), ('Pl', 'Platinum'), ('Go', 'Gold'), ('Pa', 'Palladium'), ('Ta', 'Tantalum'), ('Wh', 'Whetstone'), ('Ti', 'Tin'), ('Zi', 'Zinc'), ('St', 'Steel'), ('Bi', 'Bismuth'), ('Ir', 'Iron'), ('An', 'Antimony'), ('Ni', 'Nickel'), ('Al', 'Aluminium'), ('Co', 'Cobalt'), ('Ox', 'Oxygen'), ('Ca', 'Carbon'), ('Si', 'Silicon'), ('In', 'Indium'), ('Ga', 'Gallium'), ('Ne', 'Neodymium'), ('Me', 'Mercury'), ('Ca', 'Cadmium'), ('Su', 'Sulphur'), ('Br', 'Brominated Flame Retardants'), ('Pe', 'Perfluorooctanoic acid'), ('Be', 'Beryllium Oxide'), ('Po', 'Polyvinyl Chloride'), ('He', 'Hexavalent Chromium'), ('Le', 'Lead'), ('Am', 'Americium')], max_length=2)),
                ('effect', models.CharField(max_length=1000)),
            ],
        ),
        migrations.AddField(
            model_name='device',
            name='elements',
            field=models.ManyToManyField(to='device.Element'),
        ),
    ]
