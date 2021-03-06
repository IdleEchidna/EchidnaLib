import os
from dotenv import load_dotenv

from echidnalib import bot_core

load_dotenv()

here = os.path.dirname(__file__)
cogdir = os.path.join(here,'cogs')

bot = bot_core.Bot(os.getenv('DISCORD_TOKEN'),cogdir)

bot.start()