import discord
from discord.ext import commands
from decouple import config
from movie import get_description, get_movie

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.command(name='desc')
async def _desc(ctx,movie_name):
    desc = get_description(movie_name)
    await ctx.channel.send(desc)

@bot.command(name='info')
async def _info(ctx,*,movie_name):
    movie = get_movie(movie_name)
    embed_message = discord.Embed(title=movie["Title"],description=movie["Plot"])
    embed_message.set_image(url=movie["Poster"]) 
    embed_message.add_field(name="IMdB",value=movie["imdbRating"])
    await ctx.channel.send(embed=embed_message)

bot.run(config('BOT_KEY'))
