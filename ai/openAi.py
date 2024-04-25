from openai import OpenAI
 

api_key = 'sk-proj-aJhHaoKKZGEK1ElfV8MxT3BlbkFJVSHuyVqJy9RlIXb6TgXB'

client = OpenAI(api_key=api_key)

# Define the chat completion request
completion = client.chat.completions.create(model="gpt-3.5-turbo",
messages=[
    {"role": "system", "content": "You are a club matcher, skilled in reading a short bibliography and selecting the best clubs for that individual."},
    {"role": "user", "content": "I love to play chess and race cars what clubs would you recommend?"},
])

# Extract and print the completed response message
print(completion.choices[0].message.content)