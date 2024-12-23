# Generated by Django 5.1.2 on 2024-11-29 06:41

import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("chat", "0002_remove_file_user_chathistory_document_processedindex_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="chathistory",
            name="document_context",
            field=models.ManyToManyField(
                blank=True, related_name="chat_contexts", to="chat.document"
            ),
        ),
        migrations.AddField(
            model_name="chathistory",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="chathistory",
            name="last_message_at",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="chathistory",
            name="conversation_id",
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AddIndex(
            model_name="chathistory",
            index=models.Index(
                fields=["user", "conversation_id", "last_message_at"],
                name="chat_chathi_user_id_0576dd_idx",
            ),
        ),
        migrations.AddIndex(
            model_name="chathistory",
            index=models.Index(
                fields=["is_active", "last_message_at"],
                name="chat_chathi_is_acti_14b8a2_idx",
            ),
        ),
    ]