import csv
import requests
from redbot.core import commands, data_manager
import random

class cardMini(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def open2(self, ctx):
        db_file = data_manager.cog_data_path(self) / "cards.csv"

        with open(db_file, "r") as csv_file:
            cards_data = list(csv.DictReader(csv_file))

        season2_cards = [card for card in cards_data if card["Season"] == "2"]

        if season2_cards and random.random() < 0.9:
            random_card = random.choice(season2_cards)
        else:
            random_card = random.choice(cards_data)

        card_info = f"Username: {random_card['Username']}\n" \
                    f"Mention: {random_card['Mention']}\n" \
                    f"ID: {random_card['ID']}\n" \
                    f"Ranking: {random_card['Ranking']}\n" \
                    f"Rarity: {random_card['Rarity']}\n" \
                    f"Season: {random_card['Season']}\n" \
                    f"GobsCount: {random_card['GobsCount']}\n" \
                    f"MV: {random_card['MV']}"

        await ctx.send(f"Random Card:\n{card_info}")

    @commands.command()
    async def import_cards(self, ctx):
        url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRSS2pmupriEkgsieDU1LnDc0En1TjULcY7cjS_9qCgOdgSwKeIp7NFvhdfgfGp0swVzn4bNsPfcRqs/pub?gid=0&single=true&output=csv"

        response = requests.get(url)
        if response.status_code == 200:
            csv_content = response.content.decode("utf-8").splitlines()

            cards_data = list(csv.DictReader(csv_content))
            db_file = data_manager.cog_data_path(self) / "cards.csv"

            if db_file.exists():
                with open(db_file, "a", newline="") as csv_file:
                    fieldnames = cards_data[0].keys()
                    data_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                    data_writer.writerows(cards_data)
            else:
                with open(db_file, "w", newline="") as csv_file:
                    fieldnames = cards_data[0].keys()
                    data_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                    data_writer.writeheader()
                    data_writer.writerows(cards_data)

            await ctx.send("Database created/updated successfully.")
        else:
            await ctx.send("Failed to fetch CSV data from the URL.")

def setup(bot):
    cog = CardCog(bot)
    bot.add_cog(cog)
