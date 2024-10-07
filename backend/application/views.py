import json

from django.http import JsonResponse
from django.shortcuts import render
from textblob import TextBlob


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
    
        return render(request, 'application/result.html', {
            'sentiment': sentiment,
            'popolarity': sentiment_polarity,
            'text': input
        })
    
    return render(request, 'application/index.html')