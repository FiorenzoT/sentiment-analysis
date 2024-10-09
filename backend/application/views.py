import json

from django.http import JsonResponse
from django.shortcuts import render
from textblob import TextBlob
from .models import SentimentAnalysis


def sentiment_analysis(request):
    """
    Handles the sentiment analysis for POST requests. It receives the input text,
    performs sentiment analysis, saves the result to the database, and returns the analysis
    results in a JSON response.

    If the request is not POST, it renders the default sentiment analysis page.

    Args:
        request: The HTTP request object.

    Returns:
        If POST, a JSON response containing the analyzed text, sentiment label, and polarity.
        If not POST, renders the 'index.html' page for sentiment input.
    """

    if request.method == 'POST':
        input = request.POST.get('text')

        # Perform sentiment analysis using TextBlob
        blob = TextBlob(input)
        sentiment_polarity = blob.sentiment.polarity

        if sentiment_polarity > 0:
            sentiment = 'Positive'
        elif sentiment_polarity < 0:
            sentiment = 'Negative'
        else:
            sentiment = 'Neutral'

        # Save the analyzed input, sentiment, and polarity to the database
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
    """
    Handles displaying the history of previous sentiment analysis results.
    Retrieves all saved sentiment analysis records from the database, ordered by
    the most recent entry first, and passes them to the 'history.html' template for rendering.

    Args:
        request: The HTTP request object.

    Returns:
        Renders the 'history.html' template with the list of past analyses.
    """

    analyses = SentimentAnalysis.objects.all().order_by('-created_at')

    return render(request, 'application/history.html', {'analyses': analyses})