import discord
from discord import app_commands
from discord.ext import commands
from environments import *
from buttons import *
from discord.app_commands import Choice


class SlashCommands(commands.Cog):

    def __init__(
            self,
            bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(
        name="name",
        description="Please enter your name only.")
    async def name(
            self,
            interaction: discord.Interaction,
            name: str) -> None:
        if interaction.channel.id == command_channel_id:
            with open(
                    "members.json",
                    "r") as doc:
                members = json.load(doc)

            if str(interaction.user.id) not in members:
                channel = self.bot.get_channel(channel1)
                await interaction.response.send_message(
                    f"Successful.")
                await channel.send(
                    f"You can not use this command.")
                await channel.send(
                    f"Please use !!dm to our bot {interaction.user.mention}.")

            else:

                language = members[str(interaction.user.id)]["language"]

                if "name" in members[str(interaction.user.id)]:
                    channel = self.bot.get_channel(channel1)

                    await interaction.response.send_message(
                        f"Successful.")
                    await channel.send(
                        f"Your name is already in our database {interaction.user.mention}.")

                else:
                    try:

                        with open(
                                f"members.json",
                                "r") as doc:

                            users = json.load(doc)

                        users[str(interaction.user.id)]["name"] = name

                        with open(
                                f"members.json",
                                "w") as doc:

                            json.dump(users, doc)

                        channel = self.bot.get_channel(channel1)

                        await interaction.response.send_message(
                            f"Successful.")
                        await channel.send(
                            f"{texter(language=language, index='6_1')} {interaction.user.mention}")

                    except Exception as e:
                        await interaction.response.send_message(
                            f"Successful.")

                        print(e)
                        channel = self.bot.get_channel(channel1)

                        await channel.send(
                            f"{interaction.user.mention}, \nError: {e}")

        else:
            await interaction.response.send_message(
                f"Successful.")
            await interaction.channel.send(
                f"Please use commands at right channel: <#1012250908840693801>", delete_after=5)
            await interaction.message.delete()

    @app_commands.command(
        name="dm",
        description="Open private dms and use this command for communicate.")
    async def dm(
            self,
            interaction: discord.Interaction):

        if interaction.channel.id == command_channel_id:
            member = interaction.user

            with open(
                    f"members.json",
                    "r") as doc:

                members = json.load(doc)

            if str(member.id) in members:
                channel = self.bot.get_channel(channel1)

                await interaction.response.send_message(
                    f"Successful.")
                await channel.send(
                    f"You can not use this command.")
                await channel.send(
                    f"Your id is already in our database. {member.mention}")

            else:
                try:

                    await interaction.response.send_message(
                        f"Successful.")
                    await interaction.followup.send(
                        f"Please check your dm {member.mention}")

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
                        f"{text}",
                        view=await language_buttons())

                except Exception as e:

                    await interaction.response.send_message(
                        f"Successful.")

                    print(e)
                    channel = self.bot.get_channel(channel1)

                    await channel.send(f"{interaction.user.mention}, \n{texter('gb', '99')}")

        else:

            await interaction.response.send_message(
                f"Successful.")
            await interaction.channel.send(
                f"Please use commands at right channel: <#1012250908840693801>", delete_after=5)
            await interaction.channel.message.delete()

    @app_commands.command(
        name="surname",
        description="Please enter your surname only.")
    async def surname(
            self,
            interaction: discord.Interaction,
            surname: str) -> None:

        if interaction.channel.id == command_channel_id:
            member = interaction.user

            with open(
                    f"members.json",
                    "r") as doc:

                members = json.load(doc)

            if str(member.id) not in members:
                channel = self.bot.get_channel(channel1)

                await interaction.response.send_message(
                    f"Successful.")
                await channel.send(
                    f"You can not use this command.")
                await channel.send(
                    f"Please use !!dm to our bot {member.mention}.")

            else:

                if "surname" in members[str(member.id)]:
                    channel = self.bot.get_channel(channel1)

                    await interaction.response.send_message(
                        f"Successful.")
                    await channel.send(
                        f"Your surname is already in our database {member.mention}")

                else:
                    try:

                        with open(
                                f"members.json",
                                "r") as doc:

                            users = json.load(doc)
                        users[str(member.id)]["surname"] = surname

                        with open(
                                f"members.json",
                                "w") as doc:
                            json.dump(users, doc)

                        channel = self.bot.get_channel(channel1)

                        await interaction.response.send_message(
                            f"Successful.")
                        await channel.send(
                            f"{texter(users[str(member.id)]['language'], index='7_1')} {member.mention}")
                        await member.edit(
                            nick=f"{users[str(member.id)]['name']} {surname}")

                    except Exception as e:
                        channel = self.bot.get_channel(channel1)

                        await interaction.response.send_message(
                            f"Successful.")
                        await channel.send(
                            f"{member.mention}, \nError: {e}")

        else:

            await interaction.response.send_message(
                f"Successful.")
            await interaction.channel.send(
                f"Please use commands at right channel: <#1012250908840693801>", delete_after=5)
            await interaction.message.delete()

    @app_commands.command(
        name="change_language",
        description="Changing the language of a user. !Only for moderators!")
    @app_commands.describe(
        user="User to change language",
        language="New language")
    @app_commands.choices(
        language=[
            Choice(name="Tr", value="tr"),
            Choice(name="Gb", value="gb"),
            Choice(name="Cp", value="cp"),
            Choice(name="De", value="de"),
            Choice(name="Es", value="es")])
    async def change_language(
            self,
            interaction: discord.Interaction,
            user: discord.Member,
            language: str) -> None:

        if interaction.user.guild_permissions.manage_messages:

            with open(
                    f"members.json",
                    "r") as doc:
                members = json.load(doc)

            name = f"Language | {members[str(user.id)]['language'].upper()}"
            old_role = discord.utils.get(interaction.guild.roles, name=name)
            del members[str(user.id)]["language"]
            members[str(user.id)]["language"] = language

            with open(
                    f"members.json",
                    "w") as doc:
                json.dump(members, doc)

            channel = self.bot.get_channel(channel1)
            name = f"Language | {language.upper()}"
            role = discord.utils.get(interaction.guild.roles, name=name)
            member = interaction.guild.get_member(user.id)

            await member.remove_roles(old_role)
            await member.add_roles(role)
            await interaction.response.send_message(
                "Successful")
            await channel.send(
                f"New language for {user.mention} is {language}.")

        else:

            await interaction.response.send_message(
                "Failed")
            channel = self.bot.get_channel(channel1)

            await channel.send(
                f"An error occurred {interaction.user.mention}: *INSUFFICIENT AUTHORITY*")

    @app_commands.command(
        name="help",
        description="Shows a embed about commands which you can use.")
    @app_commands.describe(
        command="Choose a command for more explanation")
    @app_commands.choices(
        command=[
            Choice(name="Dm", value="dm"),
            Choice(name="Name", value="name"),
            Choice(name="Surname", value="surname"),
            Choice(name="Change Language", value="change_language")])
    async def help(
            self,
            interaction: discord.Interaction,
            command: str = None) -> None:

        try:

            if command is None:
                embed = discord.Embed(
                    title="*COMMANDS*",
                    color=discord.Color.blurple())
                embed.add_field(
                    name="/help",
                    value="Shows this embed.",
                    inline=False)
                embed.add_field(
                    name="/dm",
                    value="For members which can't get any dms",
                    inline=False)
                embed.add_field(
                    name="/name",
                    value="For using while signing up",
                    inline=False)
                embed.add_field(
                    name="/surname",
                    value="For using while signing up",
                    inline=False)
                embed.add_field(
                    name="/change_language",
                    value="!For admins only!",
                    inline=False)
                embed.set_footer(
                    text="For more, please use help command with options.",
                    icon_url=self.bot.user.avatar)

                await interaction.response.send_message(
                    f"Successful.")

                channel = self.bot.get_channel(channel1)

                await channel.send(
                    f"{interaction.user.mention}",
                    embed=embed)

            else:

                if command == "dm":
                    embed = discord.Embed(
                        title="*DETAILS FOR 'DM' COMMAND*",
                        color=discord.Color.green())
                    embed.add_field(
                        name="DESCRIPTION",
                        value="""//For members which couldn't get any dms from our bot.
            Don't forget allow dms from server members option.
            Please allow the permission.
            For more help: https://support.discord.com/hc/en-us/articles/217916488-Blocking-Privacy-Settings-""")
                    embed.set_footer(
                        text="If you have any questions pleas contact with moderators.",
                        icon_url=self.bot.user.avatar)

                    await interaction.response.send_message(
                        f"Successful.")

                    channel = self.bot.get_channel(channel1)

                    await channel.send(
                        f"{interaction.user.mention}",
                        embed=embed)

                elif command == "name":
                    embed = discord.Embed(
                        title="*DETAILS FOR 'NAME' COMMAND*",
                        color=discord.Color.green())
                    embed.add_field(
                        name="DESCRIPTION",
                        value="""//Use this command while signing up.
            Please follow the directions which is on your dm
            Usage: !!name {your name}""")
                    embed.set_footer(
                        text="If you have any questions pleas contact with moderators.",
                        icon_url=self.bot.user.avatar)

                    await interaction.response.send_message(
                        f"Successful.")

                    channel = self.bot.get_channel(channel1)

                    await channel.send(
                        f"{interaction.user.mention}",
                        embed=embed)

                elif command == "surname":
                    embed = discord.Embed(
                        title="*DETAILS FOR 'SURNAME' COMMAND*",
                        color=discord.Color.green())
                    embed.add_field(
                        name="DESCRIPTION",
                        value="""//Use this command while signing up.
                Please follow the directions which is on your dm
                Usage: !!name {your surname}""")
                    embed.set_footer(
                        text="If you have any questions pleas contact with moderators.",
                        icon_url=self.bot.user.avatar)

                    await interaction.response.send_message(
                        f"Successful.")

                    channel = self.bot.get_channel(channel1)

                    await channel.send(
                        f"{interaction.user.mention}",
                        embed=embed)

                elif command == "change_language":
                    embed = discord.Embed(
                        title="*DETAILS FOR 'CHANGE LANGUAGE' COMMAND*",
                        color=discord.Color.green())
                    embed.add_field(
                        name="DESCRIPTION",
                        value="""//Only for admins.
            Usage: !!change_language {user} {language}
            !language should be in that form: tr, gb, cp, de, es.""")
                    embed.set_footer(
                        text="If you have any questions pleas contact with moderators.",
                        icon_url=self.bot.user.avatar)

                    await interaction.response.send_message(
                        f"Successful.")

                    channel = self.bot.get_channel(channel1)

                    await channel.send(
                        f"{interaction.user.mention}", embed=embed)

        except Exception as e:

            await interaction.response.send_message(
                f"Failed event.")

            channel = self.bot.get_channel(channel1)

            await channel.send(
                f"An error occurred {interaction.user.mention}, error message:")
            print(e)
            await channel.send(
                f"{e}")


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(SlashCommands(bot), guilds=[discord.Object(id=1009896590128984064)])
