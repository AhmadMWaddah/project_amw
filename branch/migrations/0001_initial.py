# Generated by Django 3.1.7 on 2021-04-10 07:55

import branch.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('brnch_pk', models.AutoField(primary_key=True, serialize=False, verbose_name='Branch ID')),
                ('brnch_nme', models.CharField(max_length=100, verbose_name='Branch Name')),
                ('brnch_cntry', models.CharField(max_length=100, verbose_name='Branch Country')),
                ('brnch_stt', models.CharField(max_length=100, verbose_name='Branch State')),
                ('brnch_cty', models.CharField(max_length=100, verbose_name='Branch City')),
                ('brnch_strt', models.CharField(max_length=150, verbose_name='Branch Street')),
                ('brnch_bx', models.CharField(blank=True, default=None, max_length=8, null=True, verbose_name='Branch Box Code')),
                ('brnch_phn', models.CharField(blank=True, default=None, max_length=15, null=True, unique=True, verbose_name='Branch Phone')),
                ('brnch_fx', models.CharField(blank=True, default=None, max_length=15, null=True, unique=True, verbose_name='Branch Fax')),
                ('brnch_mbl', models.CharField(blank=True, default=None, max_length=15, null=True, unique=True, verbose_name='Branch Mobile')),
                ('brnch_eml', models.EmailField(max_length=254, verbose_name='Branch Email')),
                ('brnch_www', models.URLField(max_length=150, verbose_name='Branch Website')),
                ('brnch_loc', models.CharField(max_length=600, verbose_name='Branch Location')),
                ('brnch_img', models.ImageField(blank=True, default=branch.models.default_branch_image, null=True, upload_to=branch.models.branch_image_path, verbose_name='Branch Image')),
            ],
            options={
                'verbose_name': 'Branch',
                'verbose_name_plural': 'Branches',
                'ordering': ['brnch_cntry'],
            },
        ),
    ]
