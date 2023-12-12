from .cardMini import CardMini


async def setup(bot):
    await bot.add_cog(CardMini(bot))
