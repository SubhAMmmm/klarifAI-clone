# Generated by Django 5.1.2 on 2024-12-04 07:54

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("chat", "0005_remove_conversation_user_remove_message_conversation_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="chathistory",
            options={
                "ordering": ["-created_at"],
                "verbose_name_plural": "Chat Histories",
            },
        ),
        migrations.RemoveField(
            model_name="chathistory",
            name="answer",
        ),
        migrations.RemoveField(
            model_name="chathistory",
            name="question",
        ),
        migrations.AddField(
            model_name="chathistory",
            name="documents",
            field=models.ManyToManyField(
                blank=True, related_name="chat_histories", to="chat.document"
            ),
        ),
        migrations.AddField(
            model_name="chathistory",
            name="follow_up_questions",
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="chathistory",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="chathistory",
            name="conversation_id",
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AlterField(
            model_name="chathistory",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="chat_histories",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.CreateModel(
            name="ChatMessage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "role",
                    models.CharField(
                        choices=[
                            ("user", "User"),
                            ("assistant", "Assistant"),
                            ("system", "System"),
                        ],
                        max_length=20,
                    ),
                ),
                ("content", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("citations", models.JSONField(blank=True, null=True)),
                (
                    "chat_history",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="messages",
                        to="chat.chathistory",
                    ),
                ),
            ],
            options={
                "ordering": ["created_at"],
            },
        ),
    ]
