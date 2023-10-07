

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
       migrations.CreateModel(
            name='Randevu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tarih', models.CharField(max_length=50)),
                ('numara', models.CharField(max_length=10)),
                ('isim', models.CharField(max_length=50)),
                ('soyisim', models.CharField(max_length=50)),
            ],
       ),
    ]
