import json

from django.http import JsonResponse
from django.shortcuts import render
from textblob import TextBlob


def sentiment_analysis(request):

    if request.method == 'POST':
        input = request.POST.get('text')

        if input is None:
            return JsonResponse({'error': 'No text provided'}, status=400)


        # Analyze the input
        blob = TextBlob(input)
        sentiment_polarity = blob.sentiment.polarity

        if sentiment_polarity > 0:
            sentiment = 'Positive'
        elif sentiment_polarity < 0:
            sentiment = 'Negative'
        else:
            sentiment = 'Neutral'
    
        return JsonResponse({
            'text': input,
            'sentiment': sentiment,
            'popolarity': sentiment_polarity
        })
    
    return render(request, 'application/index.html')