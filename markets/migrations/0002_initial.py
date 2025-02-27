# Generated by Django 5.1.6 on 2025-02-27 14:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("markets", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="작성자",
            ),
        ),
        migrations.AddField(
            model_name="market",
            name="tags",
            field=models.ManyToManyField(
                blank=True,
                max_length=50,
                to="markets.hashtag",
                verbose_name="해시태그 목록",
            ),
        ),
        migrations.AddField(
            model_name="market",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="markets",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="comment",
            name="market",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="markets.market",
                verbose_name="가게명",
            ),
        ),
        migrations.AddField(
            model_name="marketimage",
            name="post",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="markets.market",
                verbose_name="이미지",
            ),
        ),
        migrations.AddField(
            model_name="festival",
            name="region",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="markets.region",
            ),
        ),
    ]
