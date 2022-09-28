import discord
from discord.ext import commands
import json
from environments import *
from buttons import *


class Commands(commands.Cog):

    def __init__(
            self,
            bot):
        self.bot = bot

    @commands.command()
    async def dm(
            self,
            ctx):
        """//For members which couldn't get any dms from our bot.
        Don't forget allow dms from server members option.
        Please allow the permission.
        For more help: https://support.discord.com/hc/en-us/articles/217916488-Blocking-Privacy-Settings-"""

        if ctx.channel.id == command_channel_id:
            member = ctx.author

            with open(
                    f"members.json",
                    "r") as doc:

                members = json.load(doc)

            if str(member.id) in members:
                channel = self.bot.get_channel(channel1)

                await channel.send(
                    f"You can not use this command.")
                await channel.send(
                    f"Your id is already in our database. {member.mention}")

            else:
                try:
                    text_tr = f"{texter('tr', '1')}\n{texter('tr', '2')}\n{texter('tr', '3')}"
                    text_gb = f"{texter('gb', '1')}\n{texter('gb', '2')}\n{texter('gb', '3')}"
                    text_cp = f"{texter('cp', '1')}\n{texter('cp', '2')}\n{texter('cp', '3')}"
                    text_es = f"{texter('es', '1')}\n{texter('es', '2')}\n{texter('es', '3')}"
                    text_de = f"{texter('de', '1')}\n{texter('de', '2')}\n{texter('de', '3')}"

                    await member.send(
                        text_tr)
                    await member.send(
                        text_gb)
                    await member.send(
                        text_cp)
                    await member.send(
                        text_de)
                    await member.send(
                        text_es)

                    text = """\n\n\n**--------------------------------------------------------------------------------------**
                        PLEASE SELECT YOUR LANGUAGE"""

                    await member.send(
                        f"{text}", view=await language_buttons())

                except Exception as e:

                    channel = self.bot.get_channel(channel1)
                    await channel.send(f"An error occurred {ctx.author.mention}, \n{e}")

        else:
            await ctx.send(
                f"Please use commands at right channel: <#1012250908840693801>",
                delete_after=5)
            await ctx.message.delete()

    @commands.command()
    async def name(
            self,
            ctx,
            name: str):
        """//Use this command while signing up.
        Please follow the directions which is on your dm
        Usage: !!name {your name}"""

        if ctx.channel.id == command_channel_id:
            member = ctx.author

            with open(
                    f"members.json",
                    "r") as doc:
                members = json.load(doc)

            if str(member.id) not in members:
                channel = self.bot.get_channel(channel1)

                await channel.send(
                    f"You can not use this command.")
                await channel.send(
                    f"Please use !!dm to our bot {member.mention}.")

            else:
                language = members[str(ctx.author.id)]["language"]

                if "name" in members[str(member.id)]:
                    channel = self.bot.get_channel(channel1)

                    await channel.send(
                        f"Your name is already in our database {member.mention}.")

                else:
                    try:

                        with open(
                                f"members.json",
                                "r") as doc:
                            users = json.load(doc)

                        users[str(ctx.author.id)]["name"] = name

                        with open(
                                f"members.json",
                                "w") as doc:
                            json.dump(users, doc)

                        channel = self.bot.get_channel(channel1)

                        await channel.send(
                            f"{texter(language=language, index='6_1')} {ctx.author.mention}")

                    except Exception as e:
                        channel = self.bot.get_channel(channel1)
                        await channel.send(f"{ctx.author.mention}, \nError: {e}")

        else:
            await ctx.send(
                f"Please use commands at right channel: <#1012250908840693801>",
                delete_after=5)
            await ctx.message.delete()

    @commands.command()
    async def surname(
            self,
            ctx,
            surname: str):
        """//Use this command while signing up.
        Please follow the directions which is on your dm
        Usage: !!surname {your surname}"""

        if ctx.channel.id == command_channel_id:
            member = ctx.author

            with open(
                    f"members.json",
                    "r") as doc:
                members = json.load(doc)

            if str(member.id) not in members:
                channel = self.bot.get_channel(channel1)

                await channel.send(
                    f"You can not use this command.")
                await channel.send(
                    f"Please use !!dm to our bot {member.mention}.")

            else:

                if "surname" in members[str(member.id)]:
                    channel = self.bot.get_channel(channel1)

                    await channel.send(
                        f"Your surname is already in our database {member.mention}")

                else:
                    try:

                        with open(
                                f"members.json",
                                "r") as doc:
                            users = json.load(doc)

                        users[str(ctx.author.id)]["surname"] = surname

                        with open(
                                f"members.json",
                                "w") as doc:
                            json.dump(users, doc)

                        channel = self.bot.get_channel(channel1)

                        await channel.send(
                            f"{texter(users[str(member.id)]['language'], index='7_1')} {ctx.author.mention}")
                        await ctx.author.edit(
                            nick=f"{users[str(ctx.author.id)]['name']} {surname}")

                    except Exception as e:
                        channel = self.bot.get_channel(channel1)
                        await channel.send(
                            f"{ctx.author.mention}, \nError: {e}")

        else:
            await ctx.send(
                f"Please use commands at right channel: <#1012250908840693801>", delete_after=5)
            await ctx.message.delete()

    @commands.command()
    @commands.has_permissions(
        manage_messages=True)
    async def change_language(
            self,
            ctx,
            user: discord.Member,
            language: str):
        """//Only for admins.
        Usage: !!change_language {user} {language}
        !language should be in that form: tr, gb, cp, de, es."""
        with open(
                f"members.json",
                "r") as doc:
            members = json.load(doc)

        name = f"Language | {members[str(user.id)]['language'].upper()}"
        old_role = discord.utils.get(ctx.guild.roles, name=name)
        del members[str(user.id)]["language"]
        members[str(user.id)]["language"] = language.lower()

        with open(
                f"members.json",
                "w") as doc:
            json.dump(members, doc)

        channel = self.bot.get_channel(channel1)
        name = f"Language | {language.upper()}"
        role = discord.utils.get(ctx.guild.roles, name=name)
        member = ctx.guild.get_member(user.id)

        await member.remove_roles(old_role)
        await member.add_roles(role)
        await channel.send(
            f"New language for {user.mention} is {language}.")


async def setup(bot):
    await bot.add_cog(Commands(bot))
