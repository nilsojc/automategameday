import os
import json
import urllib.request
import boto3
from datetime import datetime, timedelta, timezone

def format_game_data(game):
    # Extract relevant information from the game
    status = game.get("Status", "Unknown")
    away_team_name = game.get("AwayTeamName", "Unknown")
    home_team_name = game.get("HomeTeamName", "Unknown")
    away_team_formation = game.get("AwayTeamFormation", "Unknown")
    home_team_formation = game.get("HomeTeamFormation", "Unknown")
    final_score = f"{game.get('AwayTeamScore', 'N/A')}-{game.get('HomeTeamScore', 'N/A')}"
    start_time = game.get("DateTime", "Unknown")
    
    if status == "Final":
        return (
            f"Game Status: {status}\n"
            f"{away_team_name} vs {home_team_name}\n"
            f"Final Score: {final_score}\n"
            f"Start Time: {start_time}\n"
            f"Away Team Formation: {away_team_formation}\n"
            f"Home Team Formation: {home_team_formation}\n"
        )
    elif status == "InProgress":
        last_play = game.get("LastPlay", "N/A")
        return (
            f"Game Status: {status}\n"
            f"{away_team_name} vs {home_team_name}\n"
            f"Current Score: {final_score}\n"
            f"Last Play: {last_play}\n"
            f"Away Team Formation: {away_team_formation}\n"
            f"Home Team Formation: {home_team_formation}\n"
        )
    elif status == "Scheduled":
        return (
            f"Game Status: {status}\n"
            f"{away_team_name} vs {home_team_name}\n"
            f"Start Time: {start_time}\n"
            f"Away Team Formation: {away_team_formation}\n"
            f"Home Team Formation: {home_team_formation}\n"
        )
    else:
        return (
            f"Game Status: {status}\n"
            f"{away_team_name} vs {home_team_name}\n"
            f"Details are unavailable at the moment.\n"
        )

def lambda_handler(event, context):
    # Get environment variables
    api_key = os.getenv("ESP_API_KEY")
    sns_topic_arn = os.getenv("SNS_TOPIC_ARN")
    sns_client = boto3.client("sns")
    
    # Set the date to 12-21-2024
    date = "2024-12-21"  # Explicit date
    
    # Define the competition (e.g., "La Liga")
    competition = "ESP"  # Change this to the desired competition (e.g., "PremierLeague")

    print(f"Fetching games for competition: {competition} on date: {date}")
    
    # Fetch data from the API with competition and date variables
    api_url = f"https://api.sportsdata.io/v4/soccer/scores/json/GamesByDateFinal/{competition}/{date}?key={api_key}"
    print(f"API URL: {api_url}")
     
    try:
        with urllib.request.urlopen(api_url) as response:
            data = json.loads(response.read().decode())
            print(json.dumps(data, indent=4))  # Debugging: log the raw data
    except Exception as e:
        print(f"Error fetching data from API: {e}")
        return {"statusCode": 500, "body": f"Error fetching data: {e}"}
    
    # Check if the response has the expected structure
    if not isinstance(data, list):  # If the data isn't a list (i.e., no games found or incorrect format)
        print("API response is not a list or games data is missing.")
        return {"statusCode": 400, "body": "Invalid data received from the API."}
    
    # Include all games (final, in-progress, and scheduled)
    messages = [format_game_data(game) for game in data]
    final_message = "\n---\n".join(messages) if messages else "No games available for today."
    
    # Publish to SNS
    try:
        sns_client.publish(
            TopicArn=sns_topic_arn,
            Message=final_message,
            Subject="Game Updates"
        )
        print("Message published to SNS successfully.")
    except Exception as e:
        print(f"Error publishing to SNS: {e}")
        return {"statusCode": 500, "body": f"Error publishing to SNS: {e}"}
    
    return {"statusCode": 200, "body": "Data processed and sent to SNS"}
