# Generated by Django 2.0.2 on 2018-02-03 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=150)),
                ('house_number', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicus.Country')),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(blank=True, default='', max_length=25)),
                ('email', models.CharField(blank=True, default='', max_length=150)),
                ('info', models.TextField(blank=True, default='')),
                ('picture', models.ImageField(blank=True, upload_to='doctor/images')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicus.Address')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='medicus.City')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicus.Country')),
                ('district', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='medicus.District')),
            ],
        ),
        migrations.CreateModel(
            name='PostalCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postal_code', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Profession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicus.Country')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('treatment', models.IntegerField(choices=[(1, 'insufficient'), (2, 'sufficient'), (3, 'satisfactory'), (4, 'good'), (5, 'very good')])),
                ('empathy', models.IntegerField(choices=[(1, 'insufficient'), (2, 'sufficient'), (3, 'satisfactory'), (4, 'good'), (5, 'very good')])),
                ('price', models.IntegerField(choices=[(1, 'insufficient'), (2, 'sufficient'), (3, 'satisfactory'), (4, 'good'), (5, 'very good')])),
                ('waiting_time', models.IntegerField(choices=[(1, 'insufficient'), (2, 'sufficient'), (3, 'satisfactory'), (4, 'good'), (5, 'very good')])),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicus.Doctor')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='medicus.Address')),
                ('doctor', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='medicus.Doctor')),
            ],
        ),
        migrations.AddField(
            model_name='location',
            name='postal_code',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='medicus.PostalCode'),
        ),
        migrations.AddField(
            model_name='location',
            name='province',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicus.Province'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='profession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicus.Profession'),
        ),
        migrations.AddField(
            model_name='district',
            name='province',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicus.Province'),
        ),
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicus.Country'),
        ),
        migrations.AddField(
            model_name='city',
            name='district',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='medicus.District'),
        ),
        migrations.AddField(
            model_name='city',
            name='postal_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicus.PostalCode'),
        ),
        migrations.AddField(
            model_name='city',
            name='province',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicus.Province'),
        ),
        migrations.AddField(
            model_name='address',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='medicus.City'),
        ),
        migrations.AddField(
            model_name='address',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicus.Country'),
        ),
        migrations.AddField(
            model_name='address',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='medicus.Location'),
        ),
    ]
