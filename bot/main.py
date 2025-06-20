import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import random

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    await bot.load_extension('commands.nom_de_ton_module')
    print(f"Connecté en tant que {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

@bot.command()
async def blague(ctx):
    blagues = [
        "Pourquoi les canards ont-ils autant de plumes ? Pour couvrir leur derrière !",
        "Quel est le comble pour un électricien ? De ne pas être au courant.",
        "Pourquoi les poissons détestent l’ordinateur ? À cause d’Internet."
    ]
    await ctx.send(random.choice(blagues))

@bot.command()
async def eightball(ctx, *, question):
    reponses = [
        "Oui, bien sûr !",
        "Non, jamais.",
        "Peut-être…",
        "Je ne sais pas.",
        "Demande plus tard."
    ]
    await ctx.send(f"🎱 {random.choice(reponses)}")

@bot.command()
async def pileouface(ctx):
    resultat = random.choice(["Pile", "Face"])
    await ctx.send(f"🪙 {resultat} !")

@bot.command()
async def avatar(ctx, user: discord.Member = None):
    user = user or ctx.author
    await ctx.send(user.display_avatar.url)

@bot.command()
async def serveur(ctx):
    guild = ctx.guild
    embed = discord.Embed(
        title=f"Infos du serveur {guild.name}",
        color=discord.Color.blue()
    )
    embed.add_field(name="Membres", value=guild.member_count)
    embed.add_field(name="Propriétaire", value=guild.owner)
    embed.add_field(name="Créé le", value=guild.created_at.strftime("%d/%m/%Y"))
    await ctx.send(embed=embed)

@bot.command()
async def userinfo(ctx, user: discord.Member = None):
    user = user or ctx.author
    embed = discord.Embed(
        title=f"Infos sur {user.display_name}",
        color=user.color
    )
    embed.add_field(name="ID", value=user.id)
    embed.add_field(name="Créé le", value=user.created_at.strftime("%d/%m/%Y"))
    embed.add_field(name="A rejoint le", value=user.joined_at.strftime("%d/%m/%Y"))
    embed.set_thumbnail(url=user.display_avatar.url)
    await ctx.send(embed=embed)

@bot.command()
async def dice(ctx, faces: int = 6):
    result = random.randint(1, faces)
    await ctx.send(f"🎲 Tu as lancé un dé à {faces} faces et obtenu : **{result}**")

# Load commands from the commands package
for filename in os.listdir('./bot/commands'):
    if filename.endswith('.py'):
        bot.load_extension(f'commands.{filename[:-3]}')

# Run the bot
if __name__ == "__main__":
    bot.run(TOKEN)