# Generated by Django 3.2.8 on 2021-10-07 15:28

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailforms', '0004_add_verbose_name_plural'),
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('wagtailcore', '0062_comment_models_and_pagesubscription'),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('intro', wagtail.core.fields.RichTextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.RemoveField(
            model_name='blogpagerelatedlink',
            name='page',
        ),
        migrations.RemoveField(
            model_name='blogpage',
            name='feed_image',
        ),
        migrations.AddField(
            model_name='blogpage',
            name='intro',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='blogpage',
            name='body',
            field=wagtail.core.fields.RichTextField(blank=True),
        ),
        migrations.DeleteModel(
            name='BlogIndex',
        ),
        migrations.DeleteModel(
            name='BlogPageRelatedLink',
        ),
    ]
