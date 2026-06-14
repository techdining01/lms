from .base import BaseAIProvider


class OpenAIProvider(BaseAIProvider):
    def generate(self, prompt: str): ...
