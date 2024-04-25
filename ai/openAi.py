from openai import OpenAI
import requests
 

clubs = []  # Initialize an empty list to store the clubs

# Define the URL of the API endpoint
api_url = 'http://3.21.246.221/api/clubs'

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



prompt_lines = []
for club in clubs:
    prompt_lines.append(f"Club Name: {club['Club Name']}")
    prompt_lines.append(f"Club Description: {club['Club Description']}")
    prompt_lines.append("")  # Add an empty line between clubs for separation

# Join all prompt lines into a single string with newline characters
prompt = "\n".join(prompt_lines)



api_key = 'sk-proj-zpFndZSmaygmwmlmWjchT3BlbkFJtRVbDMSfmy2zoH1qGbtC'

client = OpenAI(api_key=api_key)

# Define the chat completion request
completion = client.chat.completions.create(model="gpt-3.5-turbo",
messages=[
    {"role": "system", "content": prompt},
    {"role": "user", "content": "I love to climb, social justice, and race cars what three clubs would you recommend?"},
])

# Extract and print the completed response message
print(completion.choices[0].message.content)

