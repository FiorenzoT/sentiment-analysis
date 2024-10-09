# Sentiment Analysis Web Application

## Overview

This project is a sentiment analysis web application built using Django and a sentiment analysis backend. The application allows users to input text, which is then analyzed for sentiment (positive, negative, neutral) and polarity (a numerical value indicating sentiment strength).

## Features

- **Sentiment Analysis:** Analyze text and get a sentiment score (positive, negative, neutral) and polarity.
- **AJAX Integration:** Submits text and displays results without reloading the page.
- **Database Integration:** Saves user input and analysis results to a database, with a page to view the sentiment analysis history.
- **Docker:** Easily containerized for consistent deployment in isolated environments.
  
## Installation and Setup

1. **Prerequisites**:
    - Docker and Docker Compose installed on your system.

2. **Clone the repository**:
    ``
    git clone https://github.com/FiorenzoT/sentiment-analysis.git
    ``
    ``
    cd sentiment-analysis
    ``

3. **Build and run the Docker containers**:
    ``
    docker-compose up --build
    ``

5. **Access the web app by navigating to**: [http://localhost:8081](http://localhost:8081)

## Usage

- Navigate to the application in your browser.
- Enter a sentence or paragraph into the text box and click "Analyze" to get sentiment results.
- View the analysis of the latest input or view the history on the history page.

## Endpoints

- `/`: Home page with text input for sentiment analysis.
- `/history`: View previous sentiment analysis results.

## Future Enhancements
 - **Migrate the Database to Amazon RDS**: Instead of storing the data in a local file, the database could be moved to Amazon RDS, which is a managed service that takes care of backups, scaling, and maintenance. This would make the app more reliable and scalable.

 - **Deploy on AWS EC2**: The application could be deployed on Amazon EC2, which offers more flexibility and control over the environment. Using EC2 with Docker containers would allow the app to scale more easily and handle higher traffic.

 - **Automate with CI/CD Pipelines**: To streamline updates, we could set up a CI/CD pipeline using AWS tools. This would automate the process of testing and deploying new code changes, making the release process faster and reducing the risk of manual errors.
