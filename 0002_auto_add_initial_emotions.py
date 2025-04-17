from django.db import migrations

def add_emotions(apps, schema_editor):
    Emotion = apps.get_model('emotions', 'Emotion')
    default_emotions = [
        ('기쁨', '😊'),
        ('슬픔', '😢'),
        ('분노', '😡'),
        ('무기력', '😞'),
        ('불안', '😰'),
        ('평온', '🙂'),
    ]
    for name, emoji in default_emotions:
        Emotion.objects.get_or_create(name=name, defaults={'emoji': emoji})

class Migration(migrations.Migration):

    dependencies = [
        ('emotions', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_emotions),
    ]
