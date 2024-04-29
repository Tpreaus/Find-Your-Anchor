from openai import OpenAI
import requests
from dotenv import load_dotenv
import os
import sys

clubs = []  # Initialize an empty list to store the clubs

# Define the URL of the API endpoint
api_url = 'https://club.theodorepreaus.xyz/api/clubs'

try:
    # Make an HTTP GET request to the API endpoint
    response = requests.get(api_url)

    # Check if the response was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        clubs_data = response.json()

        # Iterate over each club in the response
        for club in clubs_data:

            # Assuming 'club' is a dictionary containing club details
            club_name = club.get('Activity Name', '')  # Assuming 'Activity Name' is the club name
            club_description = club.get('Description', '')  # Assuming 'Description' is the club description

            # Add the club name and description to the clubs list
            clubs.append({
                'Club Name': club_name,
                'Club Description': club_description
            })
            # Now 'clubs' is a list of dictionaries, where each dictionary contains a club's name and description

    else:
        # Handle unsuccessful response
        print(f'HTTP error! Status: {response.status_code}')

except Exception as e:
    # Handle any exceptions that may occur during the request
    print('Error fetching clubs:', e)
    print('Failed to fetch clubs. Please check the error message for details.')


if len(sys.argv) < 2:
    print("Usage: python openAi.py <input_data>")
    sys.exit(1)

user_input_data = sys.argv[1]

prompt_lines = []
x = 0

prompt_lines.append("Here are the clubs you can suggest, DO NOT MAKE UP CLUBS, DO NOT CHANGE THE NAME OR DESCRIPTION OF THE CLUBS, DO NOT ADD ANYTHING ELSE, must have valid club id, please answer with the and name and descriptions ONLY no club id")

for club in clubs:
    prompt_lines.append(f"Club id: " + str(x))
    x += 1
    prompt_lines.append(f"Club Name: {club['Club Name']}")
    prompt_lines.append(f"Club Description: {club['Club Description']}")
    prompt_lines.append("")  # Add an empty line between clubs for separation

# Join all prompt lines into a single string with newline characters
prompt = "\n".join(prompt_lines)


load_dotenv()  # take environment variables from .env.

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
