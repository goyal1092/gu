# Generated by Django 2.2.12 on 2020-07-20 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsroom', '0013_auto_20200506_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='copyright',
            field=models.TextField(blank=True, default='<p>&copy; 2020 GroundUp. This article is licensed under a <a rel="license"   href="http://creativecommons.org/licenses/by-nd/4.0/">Creative Commons Attribution-NoDerivatives 4.0 International License</a>.</p><p>You may republish this article, so long as you credit the authors and GroundUp, and do not change the text. Please include a link back to the original article.</p>'),
        ),
    ]
