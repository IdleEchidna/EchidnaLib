import string
import random
import discord
from discord.ext import commands

class Fun(commands.Cog):

    def __init__(self,bot):
        self.bot = bot
        self.count = 0

    @commands.command()
    async def ask(self,ctx):

        answers = [
            'As I see it, yes.',
            'Ask again later.',
            'Better not tell you now.',
            'Cannot predict now.',
            'Concentrate and ask again.',
            'Don’t count on it.',
            'It is certain.',
            'It is decidedly so.',
            'Most likely.',
            'My reply is no.',
            'My sources say no.',
            'Outlook not so good.',
            'Outlook good.',
            'Reply hazy, try again.',
            'Signs point to yes.',
            'Very doubtful.',
            'Without a doubt.',
            'Yes.',
            'Yes – definitely.',
            'You may rely on it.'
        ]
        response = random.choice(answers)
        await ctx.send(response)

    @commands.command()
    async def countup(self,ctx):
        self.count += 1
        await ctx.send(f'{self.count}!')

    @commands.command()
    async def coin_flip(self,ctx):
        sides = ['heads','tails']
        result=random.choice(sides)
        response=f"It's {result}!"
        await ctx.send(response)

    @commands.command()
    async def whowouldwin(self,ctx,arg1,arg2):
        choices=[arg1,arg2]
        winner=random.choice(choices)
        lines=[
            f'Hmm... it was close, but I think {winner} would win.',
            f'Well of course {winner} would win.',
            f"It's way too close to know.",
            f"I'm insulted you would even ask, {winner} is the clear winner."
        ]
        result=random.choice(lines)
        await ctx.send(result)

def setup(bot):
    bot.add_cog(Fun(bot))