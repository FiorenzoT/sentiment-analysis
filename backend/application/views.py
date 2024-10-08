import json

from django.http import JsonResponse
from django.shortcuts import render
from textblob import TextBlob
from .models import SentimentAnalysis


def sentiment_analysis(request):

    if request.method == 'POST':
        input = request.POST.get('text')

        # Analyze the input
        blob = TextBlob(input)
        sentiment_polarity = blob.sentiment.polarity

        if sentiment_polarity > 0:
            sentiment = 'Positive'
        elif sentiment_polarity < 0:
            sentiment = 'Negative'
        else:
            sentiment = 'Neutral'

        SentimentAnalysis.objects.create(
            input_text=input,
            sentiment=sentiment,
            polarity=sentiment_polarity
        )
    
        return JsonResponse({
            'text': input,
            'sentiment': sentiment,
            'polarity': sentiment_polarity
        })
    
    return render(request, 'application/index.html')


def sentiment_history(request):

    analyses = SentimentAnalysis.objects.all().order_by('-created_at')  # Sort by most recent

    return render(request, 'application/history.html', {'analyses': analyses})