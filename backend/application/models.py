from django.db import models


class SentimentAnalysis(models.Model):
    input_text = models.TextField()
    sentiment = models.CharField(max_length=20)
    polarity = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.input_text[:50]} - {self.sentiment} ({self.polarity})'