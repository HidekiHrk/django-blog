from django.db import migrations

def add_slug(apps, schema_editor):
    Post = apps.get_model('website', 'Post')
    for post in Post.objects.all():
        post.save()

class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_slug),
    ]
