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

client = OpenAI(api_key=api_key)

# Define the chat completion request
completion = client.chat.completions.create(model="gpt-3.5-turbo",
messages=[
    {"role": "system", "content": prompt},
    {"role": "user", "content": user_input_data},
])

# Extract and print the completed response message
print(completion.choices[0].message.content)

