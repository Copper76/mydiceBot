import asyncio
import discord
import random
from discord.ext import commands

bot = commands.Bot(command_prefix="!")


@bot.command()
async def rollshort(ctx, *dice):
    channel = ctx.channel
    if len(dice) == 0:
        randomValue = random.randint(1, 20)
        await channel.send("1d20:" + str(randomValue))
        if randomValue == 1:
            await channel.send("You got a natural 1, impressive")
        elif randomValue == 20:
            await channel.send("OMG NATURAL 20")
    else:
        total = ""
        totalDice = []
        summation = 0
        for i in range(len(dice)):
            num = dice[i].split('d')[0]
            if num == "":
                num = 1
            else:
                try:
                    num = int(num)
                except:
                    await channel.send("Error with the dice")
                    return
            try:
                d = int(dice[i].split('d')[1])
                if d != 4 and d != 6 and d != 8 and d != 10 and d != 12 and d != 20 and d != 100:
                    await channel.send("Error with the dice")
                    return
                for i2 in range(num):
                    totalDice.append(random.randint(1, d))
                total += dice[i] + " "
            except:
                await channel.send("Error with the dice")
                return
        total += ":"
        for i in range(len(totalDice)):
            summation += totalDice[i]
        total += str(summation)
        await channel.send(total)
        if len(totalDice) == 1 and d == 20:
            if totalDice[0] == 1:
                await channel.send("You got a natural 1, impressive")
            elif totalDice[0] == 20:
                await channel.send("OMG NATURAL 20")


@bot.command()
async def roll(ctx, *dice):
    channel = ctx.channel
    if len(dice) == 0:
        randomValue = random.randint(1, 20)
        await channel.send("1d20:" + str(randomValue))
        if randomValue == 1:
            await channel.send("You got a natural 1, impressive")
        elif randomValue == 20:
            await channel.send("OMG NATURAL 20")
    else:
        total = ""
        totalDice = []
        summation = 0
        for i in range(len(dice)):
            num = dice[i].split('d')[0]
            if num == "":
                num = 1
            else:
                try:
                    num = int(num)
                except:
                    await channel.send("Error with the dice")
                    return
            try:
                d = int(dice[i].split('d')[1])
                if d != 4 and d != 6 and d != 8 and d != 10 and d != 12 and d != 20 and d != 100:
                    await channel.send("Error with the dice")
                    return
                for i2 in range(num):
                    totalDice.append(random.randint(1, d))
                total += dice[i] + " "
            except:
                await channel.send("Error with the dice")
                return
        total += ":"
        for i in range(len(totalDice)):
            total += str(totalDice[i])
            if (i < len(totalDice) - 1):
                total += '+'
            else:
                total += '='
            summation += totalDice[i]
        total += str(summation)
        await channel.send(total)
        if len(totalDice) == 1 and d == 20:
            if totalDice[0] == 1:
                await channel.send("You got a natural 1, impressive")
            elif totalDice[0] == 20:
                await channel.send("OMG NATURAL 20")


@bot.command()
async def dm(ctx, user: discord.User, content):
    await user.send(content)


@bot.command()
async def embed(ctx):
    embed: discord.Embed = discord.Embed(title="hi", description="yareyare")
    embed.set_footer(text="hello")
    await ctx.channel.send(embed=embed)


@bot.command()
async def make_announcement(ctx: commands.Context):
    """
        Create a new announcement in a server targeting specific roles
    :param ctx:
    :return:
    """

    while True:
        await ctx.send("Now please enter the message that you want to send")
        message = await bot.wait_for("message")
        if not message:
            await ctx.send(
                "Okay, didn't receive a message. Cancelling command.")
            return
        else:
            if len(message.content) <= 2000:
                content = message.content
            else:
                await ctx.send(
                    "The message is too long, please keep the message within 2000 characters")
                return
        embed: discord.Embed = discord.Embed(title=f"This announcement is from {ctx.guild.name}",
                                             description=content)  # , colour=KoalaColours.KOALA_GREEN
        embed.set_thumbnail(url=ctx.guild.icon_url)
        await ctx.channel.send(embed=embed)
        await ctx.send("Are you happy with the message you are sending? Please respond with Y/N")
        reply = await bot.wait_for("message")
        if not reply or reply.content == 'Y':
            break
    while True:
        await ctx.send(
            "Please add the roles that you want to tag separated by comma,or enter Y when you are done")
        roles = await bot.wait_for("message")
        receiver = []
        role_list = []
        if not roles:
            await ctx.send("There doesn't seem to be any input, cancelling the command due to inactivity")
            return
        elif roles.content == 'Y':
            if not receiver:
                receiver = ctx.guild.members
                roles.content = "everyone"
                role_list.append(ctx.guild.id)
            break
        else:
            for role in roles.content.split():
                role_list.append(role[3:-1])
            for member in ctx.guild.members:
                for role in member.roles:
                    if role.id in role_list:
                        receiver.append(member)
                        break
        await ctx.send(
            f"You will send to {roles.content} and there are {str(len(receiver))} receivers")

    for user in receiver:
        await user.send(embed=embed)
    await ctx.send("The announcement was made successfully")


@bot.command()
async def allroles(ctx):
    await ctx.send("OK do it")
    all_roles = ctx.guild.roles
    await ctx.send(all_roles)
    await ctx.send(ctx.guild.id)


bot.run("Nzg1MjczMzUzNzQwNjE1NzM0.X81czQ.idHIpwPFbCraY3CLRes1d0KKlmA")
