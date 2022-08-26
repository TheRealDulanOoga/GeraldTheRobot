from discord_components import ComponentsBot

from music_cog import music_cog
from help_cog import help_cog

bot = ComponentsBot(command_prefix='!')

bot.remove_command('help')

bot.add_cog(music_cog(bot))
bot.add_cog(help_cog(bot))

with open('token.txt', 'r') as file:
    token = file.readlines()[0]
bot.run(token)
