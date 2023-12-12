from .cardMini import CardMini

card_mini = None  # type: CardMini


def setup(jenni):
    global card_mini
    card_mini = CardMini(jenni)


class Context:
    def __init__(self, jenni, input):
        self.jenni = jenni
        self.input = input

    @property
    def author(self):
        return self.input.user

    @property
    def guild(self):
        return self.input.message.guild

    async def send(self, msg=None, embed=None):
        if msg is not None:
            return await self.jenni.say(msg)
        if embed is not None:
            return await self.jenni.embed(embed)
        return None


async def invalid(jenni):
    await jenni.say("Invalid command")


async def ccglisttables(jenni, input):
    if not card_mini or not input.owner:
        return
    await card_mini.list_tables(Context(jenni, input))
ccglisttables.commands = ['ccglisttables']
ccglisttables.priority = 'low'
ccglisttables.thread = False
ccglisttables.rate = 0


async def ccgsetpayouttime(jenni, input):
    if not card_mini or not input.owner:
        return
    try:
        time = int(input.group(2))
        await card_mini.set_payout_time(Context(jenni, input), time)
    except:
        await invalid(jenni)
ccgsetpayouttime.commands = ['ccgsetpayoutttime']
ccgsetpayouttime.priority = 'low'
ccgsetpayouttime.thread = False
ccgsetpayouttime.rate = 0


async def ccgsetstock(jenni, input):
    if not card_mini or not input.owner:
        return
    try:
        indexes = input.group(2).split(" ")
        series = indexes.pop(0)
        count = int(indexes.pop(0))
        await card_mini.set_stock_command(Context(jenni, input), series, count)
    except:
        await invalid(jenni)
ccgsetstock.commands = ['ccgsetstock']
ccgsetstock.priority = 'low'
ccgsetstock.thread = False
ccgsetstock.rate = 0


async def ccgupdatenames(jenni, input):
    if not card_mini or not input.owner:
        return
    await card_mini.updateNames(Context(jenni, input))
ccgupdatenames.commands = ['ccgupdatenames']
ccgupdatenames.priority = 'low'
ccgupdatenames.thread = False
ccgupdatenames.rate = 0


async def ccgdvleaderboard(jenni, input):
    if not card_mini:
        return
    try:
        count = int(input.group(2))
        await card_mini.DV_leaderboard(Context(jenni, input), count)
    except:
        await card_mini.DV_leaderboard(Context(jenni, input))
ccgdvleaderboard.commands = ['ccgdvl', 'DV_leaderboard', 'DVL', 'leaderboard_DV', 'dv_top', 'top_dv']
ccgdvleaderboard.priority = 'low'
ccgdvleaderboard.thread = False
ccgdvleaderboard.rate = 0


async def ccgbankleaderboard(jenni, input):
    if not card_mini:
        return
    try:
        count = int(input.group(2))
        await card_mini.bank_leaderboard(Context(jenni, input), count)
    except:
        await card_mini.bank_leaderboard(Context(jenni, input))
ccgbankleaderboard.commands = ['ccgbal', 'bank_leaderboard', 'leaderboard_bank', 'bank_top', 'top_bank']
ccgbankleaderboard.priority = 'low'
ccgbankleaderboard.thread = False
ccgbankleaderboard.rate = 0


async def ccgsetonseason(jenni, input):
    if not card_mini or not input.owner:
        return
    try:
        series = input.group(2)
        await card_mini.setOnSeason(Context(jenni, input), series)
    except:
        await invalid(jenni)
ccgsetonseason.commands = ['ccgsetonseason']
ccgsetonseason.priority = 'low'
ccgsetonseason.thread = False
ccgsetonseason.rate = 0


async def ccgsetoffseasonchance(jenni, input):
    if not card_mini or not input.owner:
        return
    try:
        percent = int(input.group(2))
        await card_mini.setOffSeasonChance(Context(jenni, input), percent)
    except:
        await invalid(jenni)
ccgsetoffseasonchance.commands = ['ccgsetoffseasonchance']
ccgsetoffseasonchance.priority = 'low'
ccgsetoffseasonchance.thread = False
ccgsetoffseasonchance.rate = 0


async def ccgsetrarities(jenni, input):
    if not card_mini or not input.owner:
        return
    try:
        indexes = input.group(2).split(" ")
        series = indexes.pop(0)
        await card_mini.set_rarities(Context(jenni, input), series, indexes)
    except:
        await invalid(jenni)
ccgsetrarities.commands = ['ccgsetrarities']
ccgsetrarities.priority = 'low'
ccgsetrarities.thread = False
ccgsetrarities.rate = 0


async def ccgminesalt(jenni, input):
    if not card_mini:
        return
    await card_mini.work(Context(jenni, input))
ccgminesalt.commands = ['ccgminesalt', 'ccgmine', 'ccgsalt', 'ccgwork']
ccgminesalt.priority = 'low'
ccgminesalt.thread = False
ccgminesalt.rate = 30


async def ccgsetsellmod(jenni, input):
    if not card_mini or not input.owner:
        return
    try:
        mod = float(input.group(2))
        await card_mini.set_sell_mod(Context(jenni, input), mod)
    except:
        await invalid(jenni)
ccgsetsellmod.commands = ['ccgsetsellmod']
ccgsetsellmod.priority = 'low'
ccgsetsellmod.thread = False
ccgsetsellmod.rate = 0


async def ccgsetbuymod(jenni, input):
    if not card_mini or not input.owner:
        return
    try:
        mod = float(input.group(2))
        await card_mini.set_buy_mod(Context(jenni, input), mod)
    except:
        await invalid(jenni)
ccgsetbuymod.commands = ['ccgsetbuymod']
ccgsetbuymod.priority = 'low'
ccgsetbuymod.thread = False
ccgsetbuymod.rate = 0


async def ccgviewcard(jenni, input):
    if not card_mini:
        return
    try:
        indexes = input.group(2).split(" ")
        name = indexes.pop(0)
        try:
            season = indexes.pop(0)
        except IndexError:
            season = card_mini.get_on_season()
        await card_mini.view_card(Context(jenni, input), name, season)
    except:
        await invalid(jenni)
ccgviewcard.commands = ['ccgcard', 'ccgviewcard', 'ccgcardview']
ccgviewcard.priority = 'low'
ccgviewcard.thread = False
ccgviewcard.rate = 0


async def ccgsellcard(jenni, input):
    if not card_mini:
        return
    try:
        indexes = input.group(2).split(" ")
        name = indexes.pop(0)
        season = indexes.pop(0)
        await card_mini.sell_card(Context(jenni, input), name, season)
    except:
        await invalid(jenni)
ccgsellcard.commands = ['ccgsellcard', 'ccgcardsell']
ccgsellcard.priority = 'low'
ccgsellcard.thread = False
ccgsellcard.rate = 0


async def ccgbuycard(jenni, input):
    if not card_mini:
        return
    try:
        indexes = input.group(2).split(" ")
        name = indexes.pop(0)
        season = indexes.pop(0)
        await card_mini.buy_card(Context(jenni, input), name, season)
    except:
        await invalid(jenni)
ccgbuycard.commands = ['ccgbuycard', 'ccgcardbuy']
ccgbuycard.priority = 'low'
ccgbuycard.thread = False
ccgbuycard.rate = 0


async def ccgchkbank(jenni, input):
    if not card_mini:
        return
    await card_mini.chk_bank(Context(jenni, input))
ccgchkbank.commands = ['ccgchkbank', 'ccgbank']
ccgchkbank.priority = 'low'
ccgchkbank.thread = False
ccgchkbank.rate = 0


async def ccgsetbank(jenni, input):
    if not card_mini or not input.owner:
        return
    try:
        indexes = input.group(2).split(" ")
        bank = indexes.pop(0)
        acct = jenni.user_for_text(indexes.pop(0))
        await card_mini.set_bank(Context(jenni, input), bank, acct)
    except:
        await invalid(jenni)
ccgsetbank.commands = ['ccgsetbank']
ccgsetbank.priority = 'low'
ccgsetbank.thread = False
ccgsetbank.rate = 0


async def ccgviewdeck(jenni, input):
    if not card_mini:
        return
    try:
        indexes = input.group(2).split(" ")
        name, count = "", 10
        if len(indexes) > 0:
            name = jenni.user_for_text(indexes.pop(0))
        if len(indexes) > 0:
            count = int(indexes.pop(0))
        await card_mini.view_deck(Context(jenni, input), name, count)
    except:
        await card_mini.view_deck(Context(jenni, input))
ccgviewdeck.commands = ['ccgdeck', 'ccgviewdeck']
ccgviewdeck.priority = 'low'
ccgviewdeck.thread = False
ccgviewdeck.rate = 0


async def ccgsetstealchance(jenni, input):
    if not card_mini or not input.owner:
        return
    try:
        percent = int(input.group(2))
        await card_mini.set_steal_chance(Context(jenni, input), percent)
    except:
        await invalid(jenni)
ccgsetstealchance.commands = ['ccgsetstealchance']
ccgsetstealchance.priority = 'low'
ccgsetstealchance.thread = False
ccgsetstealchance.rate = 0


async def cchopenpack(jenni, input):
    if not card_mini:
        return
    await card_mini.random_user(Context(jenni, input))
cchopenpack.commands = ['ccgopen', 'ccgrandomuser']
cchopenpack.priority = 'low'
cchopenpack.thread = False
cchopenpack.rate = 5


async def ccgdeldeck(jenni, input):
    if not card_mini or not input.owner:
        return
    try:
        acct = jenni.user_for_input(input)
        await card_mini.delete_deck(Context(jenni, input), acct)
    except:
        await invalid(jenni)
ccgdeldeck.commands = ['ccgdeldeck']
ccgdeldeck.priority = 'low'
ccgdeldeck.thread = False
ccgdeldeck.rate = 0


async def cchlistseasons(jenni, input):
    if not card_mini:
        return
    await card_mini.list_series(Context(jenni, input))
cchlistseasons.commands = ['ccglistseason', 'ccglistseasons']
cchlistseasons.priority = 'low'
cchlistseasons.thread = False
cchlistseasons.rate = 0


async def ccgdelcard(jenni, input):
    if not card_mini or not input.owner:
        return
    try:
        indexes = input.group(2).split(" ")
        user_id = int(indexes.pop(0))
        series = indexes.pop(0)
        await card_mini.delete_card(Context(jenni, input), user_id, series)
    except:
        await invalid(jenni)
ccgdelcard.commands = ['ccgdelcard']
ccgdelcard.priority = 'low'
ccgdelcard.thread = False
ccgdelcard.rate = 0


async def ccgdelseries(jenni, input):
    if not card_mini or not input.owner:
        return
    try:
        series = input.group(2)
        await card_mini.delete_series(Context(jenni, input), series)
    except:
        await invalid(jenni)
ccgdelseries.commands = ['ccgdelseries']
ccgdelseries.priority = 'low'
ccgdelseries.thread = False
ccgdelseries.rate = 0


async def ccgnewseason(jenni, input):
    if not card_mini or not input.owner:
        return
    try:
        indexes = input.group(2).split(" ")
        series = indexes.pop(0)

        params = []
        for i in range(0, 5):
            try:
                params.append(int(indexes.pop(0)))
            except (IndexError, ValueError):
                params.append(None)

        await card_mini.new_season(Context(jenni, input), series, params[0], params[1], params[2], params[3], params[4])
    except:
        await invalid(jenni)
ccgnewseason.commands = ['ccgnewseason']
ccgnewseason.priority = 'low'
ccgnewseason.thread = False
ccgnewseason.rate = 0


async def ccgonmessage(jenni, input):
    if hasattr(input, 'message'):
        await card_mini.on_message(input.message)
ccgonmessage.rule = r'(.*)'
ccgonmessage.priority = 'low'
