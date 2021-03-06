import os
import string
import random
import discord
from discord.ext import commands

class Hangman(commands.Cog):

    def __init__(self,bot):
        self.bot = bot
        self.active_games = {}

    @commands.command()
    async def hmstart(self,ctx, *args):
        if ctx.guild.id in self.active_games:
            await ctx.send('Game is already running! use the "hmstop" command to quit the game.')
        else:
            if len(args) < 0:
                await ctx.message.delete()
            else:
                g = self.start_game(ctx,self.get_word())
                print(f'State: {g.get_state()}')
                await ctx.send(g.get_state())
                #single player, select random phrase
                pass

    @commands.command()
    async def hmstop(self, ctx):
        if ctx.guild.id in self.active_games:
            g = self.active_games[ctx.guild.id]
            await ctx.send(f'Stopped active game! The phrase was {g.word}')
            self.end_game(ctx)
        else:
            await ctx.send('No active game found! Start a game with the "hmstart" command.')

    @commands.command()
    async def hmword(self,ctx,word):
        if ctx.guild.id in self.active_games:
            g = self.active_games[ctx.guild.id]
            if(len(word) != len(g.word)):
                await ctx.send(f'Incorrect guess length, check your guess again!')
            else:
                if word == g.word:
                    await ctx.send(f'Congratulations! The phrase was {g.word}. You guessed it in {len(g.guesses)+len(g.wrong_guesses)} with {g.lives} lives left!')
                    self.end_game(ctx)
                else:
                    await ctx.send(f'Game over! Your guess was wrong, the phrase was {g.word}')
                    self.end_game(ctx)

    @commands.command()
    async def hm(self,ctx,arg1):
        if len(arg1) != 1:
            await ctx.send('Please only guess one letter!')
            return
        else:
            if ctx.guild.id in self.active_games:
                g = self.active_games[ctx.guild.id]
                if not g.guess(arg1):
                    await ctx.send(f'{arg1} is already guessed, try again!')
                else:
                    await ctx.send(g.get_state())
                    await self.check_winner(ctx,g)
                return
            else:
                await ctx.send('No active game found. Use the "hmstart" command to start a game!')
                return

    async def check_winner(self, ctx, game):
        if game.lives == 0:
            await ctx.send(f'Game over! You ran out of lives, the phrase was {game.word}')
            self.end_game(ctx)
        elif '-' not in game.revealed:
            await ctx.send(f'Congratulations! The phrase was {game.word}. You guessed it in {len(game.guesses)+len(game.wrong_guesses)} with {game.lives} lives left!')
            self.end_game(ctx)
        return 

    def end_game(self, ctx):
        self.active_games.pop(ctx.guild.id, None)

    def get_word(self):
        path = os.path.dirname(__file__)
        word_file = os.path.join(path, 'hangman/hangmanphrases.txt')
        words = open(word_file).read().splitlines()
        word = random.choice(words)
        return word

    def start_game(self, ctx, word):
        tempGame = Game(word, ctx.guild.id)
        self.active_games[ctx.guild.id] = tempGame
        print(f'Starting hangman game on {ctx.guild.id} with phrase {word}')
        return tempGame


class Game():

    def __init__(self, word, guild):
        self.word = word
        self.revealed = ""
        self.guild = 0
        self.guesses = []
        self.wrong_guesses = []
        self.lives = 5

    def get_state(self):
        temp = ""
        for letter in self.word:
            if letter != ' ' and letter not in self.guesses:
                temp += '- '
            elif letter == ' ':
                temp += '   '
            else:
                temp += letter
        self.revealed = temp

        return f'{self.revealed} LIVES:{self.lives}'

    def guess(self,guess):
        if guess in self.word and guess not in self.guesses:
            self.guesses.append(guess)
            return True
        elif guess in self.guesses or guess in self.wrong_guesses:
            return False
        elif guess not in self.word:
            self.wrong_guesses.append(guess)
            self.lives -=1
            return True




def setup(bot):
    bot.add_cog(Hangman(bot))