# Generated by Django 3.2.1 on 2023-04-28 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookshop', '0006_alter_book_options_alter_bookcategory_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='banner',
            options={'verbose_name': '轮播图管理', 'verbose_name_plural': '轮播图管理'},
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name': '药品管理', 'verbose_name_plural': '药品管理'},
        ),
        migrations.AlterModelOptions(
            name='bookcategory',
            options={'verbose_name': '水果分类', 'verbose_name_plural': '水果分类'},
        ),
        migrations.AlterModelOptions(
            name='cart',
            options={'verbose_name': '购物车管理', 'verbose_name_plural': '购物车管理'},
        ),
        migrations.AlterModelOptions(
            name='collection',
            options={'verbose_name': '水果收藏表', 'verbose_name_plural': '水果收藏表'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': '水果评论', 'verbose_name_plural': '水果评论'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': '订单管理', 'verbose_name_plural': '订单管理'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': '用户管理', 'verbose_name_plural': '用户管理'},
        ),
        migrations.RemoveField(
            model_name='book',
            name='publish',
        ),
        migrations.RemoveField(
            model_name='user',
            name='idcard',
        ),
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(default=1, max_length=128, verbose_name='收货地址'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(default=1, max_length=11, verbose_name='手机号'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(default=1, max_length=32, verbose_name='角色'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=32, verbose_name='产地'),
        ),
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(max_length=32, verbose_name='水果名'),
        ),
        migrations.AlterField(
            model_name='book',
            name='publish_date',
            field=models.DateField(verbose_name='生产日期'),
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
    ]