from openai import OpenAI
import requests
from dotenv import load_dotenv
import os
import sys

clubs = []  # Initialize an empty list to store the clubs

# Define the URL of the API endpoint
api_url = 'https://club.theodorepreaus.xyz/api/clubs'
api_key = os.getenv("OPENAI_API_KEY")

def fetch_clubs():
    """Fetches club details from the API and returns a list of clubs."""
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            clubs_data = response.json()
            return [{ 'name': club.get('Activity Name', 'Unknown Club'),
                      'description': club.get('Description', 'No description available') }
                    for club in clubs_data]
        else:
            print(f'HTTP error! Status: {response.status_code}')
            return []
    except Exception as e:
        print('Error fetching clubs:', e)
        return []

def validate_response(response, clubs):
    """Validates that the response only contains club names from the list."""
    valid_names = {club['name'] for club in clubs}
    # Split response into words and check if each word is part of valid club names
    return ' '.join([word for word in response.split() if word in valid_names])

def main(user_input):
    if not user_input:
        print("No user input provided.")
        sys.exit(1)

    clubs = fetch_clubs()
    prompt = "Please select a club from the following list based on user interest. Refer to clubs only by their names without altering them: " + ", ".join([club['name'] for club in clubs])
    
    client = OpenAI(api_key=api_key)
    try:
        completion = client.chat_completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": user_input}
            ],
            temperature=0.1  # Reduce randomness
        )
        suggestion = completion.choices[0].message['content']
        valid_suggestion = validate_response(suggestion, clubs)
        print(valid_suggestion or "No valid club name found in the response.")
    except Exception as e:
        print('Error during AI completion:', e)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python openAi.py '<input_data>'")
        sys.exit(1)
    main(sys.argv[1])
