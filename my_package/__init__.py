from typing import Literal

import transformers


__version__ = '0.1.0'


Label = Literal['POSITIVE', 'NEGATIVE']


class SentimentAnalyzer:
    def __init__(self) -> None:
        self.pipeline = transformers.pipeline('sentiment-analysis')

    def predict(self, text: str) -> Label:
        res = self.pipeline(text)
        return res[0]['label']  # type: ignore
