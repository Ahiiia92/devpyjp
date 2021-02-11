from pathlib import Path

from django.apps import AppConfig


class PollsConfig(AppConfig):
    name = 'polls'
    MODEL_PATH = Path("semantic_search_quora_hnswlib")