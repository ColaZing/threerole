# Generated by Django 4.0.4 on 2023-03-18 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookshop', '0005_alter_order_ordertime'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name': '水果表', 'verbose_name_plural': '水果表'},
        ),
        migrations.AlterModelOptions(
            name='bookcategory',
            options={'verbose_name': '水果分类表', 'verbose_name_plural': '水果分类表'},
        ),
        migrations.AlterModelOptions(
            name='collection',
            options={'verbose_name': '水果收藏表', 'verbose_name_plural': '水果收藏表'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': '水果评论表', 'verbose_name_plural': '水果评论表'},
        ),
        migrations.AddField(
            model_name='user',
            name='idcard',
            field=models.CharField(default=0, max_length=18, verbose_name='身份证'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(max_length=32, verbose_name='水果名'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='book',
            field=models.CharField(max_length=32, verbose_name='水果名'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='book',
            field=models.CharField(max_length=32, verbose_name='水果名'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='book',
            field=models.CharField(max_length=32, verbose_name='水果名'),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='book',
            field=models.CharField(max_length=32, verbose_name='水果名'),
        ),
        migrations.AlterField(
            model_name='couponcode',
            name='book',
            field=models.CharField(max_length=32, verbose_name='水果名'),
        ),
        migrations.AlterField(
            model_name='order',
            name='book',
            field=models.CharField(max_length=32, verbose_name='水果名'),
        ),
    ]
