from discord.ext import commands 
import pkg.client as client
import pkg.helpers as helper
import pkg.personagem as modulos_char
import pkg.helpers as utils

bot = client.cli

@bot.command()
async def test(ctx, args):
    await ctx.send(args)



def main():
    info = helper.carregarConfig("config.json")
    bot.run(info['token'])
    bot.add_command(test)
    
    pass

if __name__ == '__main__':
    main()


