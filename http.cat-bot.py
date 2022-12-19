import discord
import re
import os
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

response_codes = [100,101,102,103,200,201,202,203,204,206,207,300,301,302,303,304,305,307,308,400,401,402,403,404,405,406,407,408,409,410,411,412,413,414,415,416,417,418,420,421,422,423,424,425,426,429,431,444,450,451,497,498,499,500,501,502,503,504,506,507,508,509,510,511,521,522,523,525,599]


def extract_number(string):
    # Use a regex to find any sequence of digits in the string
    match = re.search(r'\d+', string)
    if match:
        # Convert the matched string to an integer
        try:
            return int(match.group())
        except ValueError:
            # If the value is not a valid integer, return None
            return 404
    else:
        # If no match was found, return None
        return 404

def check_code(number):
    return number in response_codes


@client.event
async def on_ready():
    print(f'Logged in...')


@client.event
async def on_message(message):
    # If the message is from the bot, ignore it
    if message.author == client.user:
        return

    # If the message starts with "http."
    if message.content.startswith('http.'):
            # Attempt to extract the response code from the message
            message_code = extract_number(message.content)
            if check_code(message_code):
                await message.channel.send(f'https://http.cat/{message_code}.jpg')
            else:
                await message.channel.send(f'https://http.cat/404.jpg')

client.run(os.getenv('TOKEN'))