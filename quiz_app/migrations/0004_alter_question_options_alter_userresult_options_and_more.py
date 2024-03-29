# Generated by Django 4.1.7 on 2023-04-01 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_app', '0003_alter_userresult_percent_alter_userresult_score'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': 'سوال', 'verbose_name_plural': 'سوال ها'},
        ),
        migrations.AlterModelOptions(
            name='userresult',
            options={'verbose_name': 'نتیجه', 'verbose_name_plural': 'نتایج'},
        ),
        migrations.AlterField(
            model_name='question',
            name='answer',
            field=models.CharField(choices=[('option1', 'option1'), ('option2', 'option2'), ('option3', 'option3'), ('option4', 'option4')], help_text='گزینه درست را انتخاب کنید', max_length=10, verbose_name='پاسخ'),
        ),
        migrations.AlterField(
            model_name='question',
            name='option1',
            field=models.CharField(max_length=50, verbose_name='گزینه اول'),
        ),
        migrations.AlterField(
            model_name='question',
            name='option2',
            field=models.CharField(max_length=50, verbose_name='گزینه دوم'),
        ),
        migrations.AlterField(
            model_name='question',
            name='option3',
            field=models.CharField(max_length=50, verbose_name='گزینه سوم'),
        ),
        migrations.AlterField(
            model_name='question',
            name='option4',
            field=models.CharField(max_length=50, verbose_name='گزینه چهارم'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question',
            field=models.CharField(max_length=50, unique=True, verbose_name='سوال'),
        ),
        migrations.AlterField(
            model_name='question',
            name='status',
            field=models.BooleanField(default=False, help_text='وضعیت انتشار سوال', verbose_name='وضعیت'),
        ),
        migrations.AlterField(
            model_name='userresult',
            name='correct',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='تعداد سوالات درست'),
        ),
        migrations.AlterField(
            model_name='userresult',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد '),
        ),
        migrations.AlterField(
            model_name='userresult',
            name='fullname',
            field=models.CharField(max_length=20, verbose_name='نام و نام خانوادگی'),
        ),
        migrations.AlterField(
            model_name='userresult',
            name='percent',
            field=models.FloatField(max_length=5, verbose_name='درصد'),
        ),
        migrations.AlterField(
            model_name='userresult',
            name='score',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='امتیاز'),
        ),
        migrations.AlterField(
            model_name='userresult',
            name='totall',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='کل سوالات'),
        ),
        migrations.AlterField(
            model_name='userresult',
            name='wrong',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='تعداد سوالات غلط'),
        ),
    ]
