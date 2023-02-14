import discord, os, json, aiohttp, random
from discord.ext import commands
from datetime import datetime

with open(".token", 'r') as f: token = str(f.readline())

bot = commands.Bot(intents=discord.Intents.all(), description="Coded by DeadSkajp#5906", help_command=None)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


@bot.event
async def on_ready(): clear(); await bot.change_presence(status=discord.Status.online, activity=discord.Game("by DeadSkajp#5906")); print(f'\n\n|> {bot.user}({bot.user.id}) is now running!\n|> Use "/geoip"')

@bot.slash_command(name="geoip", description="Gives basic info about ip using api's")
async def ip(interaction: discord.Interaction, ip : str):
    ipv4 = ip
    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://ipapi.co/{ipv4}/json/") as api:
                ip = "?"; network = "?"; city = "?"; region = "?"; regcode = "?"; countryname = "?"; countrycode = "?"; countrycap = "?"; tld = "?"; contcode = "?"; ineu = "?"; postal = "?"; Lag = "?"; Long = "?"; googlemap = "?"; timezone = "?"; utc_off = "?"; call = "?"; cur = "?"; lang = "?"; org = "?"
                async with aiohttp.ClientSession() as session:
                    async with session.get(f"https://ipapi.co/{ipv4}/json/") as api:
                        json_stats = await api.json()
                        ip = json_stats["ip"]; network = json_stats["network"] ; city = json_stats["city"]; region = json_stats["region"] ; regcode = json_stats["region_code"]; countryname = json_stats["country_name"]; countrycode = json_stats["country_code"]; countrycap = json_stats["country_capital"]; tld = json_stats["country_tld"] ; contcode = json_stats["continent_code"]; ineu = json_stats["in_eu"]; postal = json_stats["postal"] ; Lag = json_stats["latitude"]; Long = json_stats["longitude"]; timezone = json_stats["timezone"] ; utc_off = json_stats["utc_offset"] ; call = json_stats["country_calling_code"] ; cur = json_stats["currency"]; lang = json_stats["languages"]; org = json_stats["asn"] + ", " + json_stats["org"]
                try:
                    async with aiohttp.ClientSession() as session:
                        async with session.get(f"https://vpnapi.io/api/{ipv4}") as api: json_stats = await api.json(); vpn = json_stats["security"]["vpn"]; proxy = json_stats["security"]["proxy"]; tor = json_stats["security"]["tor"]
                except: vpn = "?"; proxy = "?"; tor = "?"
                embed = discord.Embed(title=f"IP info  |  {ipv4}", description=f"\nGoogle Maps: [Open](https://www.google.com/maps/search/google+map++{Lag},{Long})\n```IP: {ip}\nNetwork: {network}\nCity: {city}\nRegion: {region}\nRegion Code: {regcode}\nCountry: {countryname}\nCountry Code: {countrycode}\nCapital: {countrycap}\nTLD: {tld}\nContinent Code: {contcode}\nIn Europe: {ineu}\nPostal: {postal}\nLocation: {Lag}, {Long}\nTimezone: {timezone}\nUTC Offset: {utc_off}\nCalling Code: {call}\nCurrency: {cur}\nLanguage: {lang}\nORG: {org}\nVPN: {vpn}\nProxy: {proxy}\nTor: {tor}```", color=25 + random.randrange(999999), timestamp=datetime.utcnow())
                embed.set_footer(text="By DeadSkajp#5906")
    await interaction.response.send_message(embed=embed, ephemeral=True)

bot.run(token)