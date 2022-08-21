from discord_webhook import DiscordWebhook, DiscordEmbed
from .constants import *
import time


def on_message(status_code: int, website: str):
    webhook = DiscordWebhook(
        url=f"https://discord.com/api/webhooks/1011048625410945115/HyzHdv6OMag7cQxEjaW_f-yQeaeTH-BkTjuKLhjbXvGt4vwu7PitxoGMHjI4doHWHPJL"
    )
    embed = DiscordEmbed(title="REQUEST_ERROR", color=COLOR_DS, url=website)
    embed.set_thumbnail(url="https://www.codingem.com/wp-content/uploads/2021/08/try-catch.001-1024x576.jpeg")
    embed.add_embed_field(name="STATUS_CODE", value=status_code, inline=True)
    embed.set_footer(
        text="Error_Monitor",
        icon_url="https://cdn.discordapp.com/attachments/1005141977488175154/1011050692804358214/1612056853933.jpeg",
    )
    embed.set_timestamp()
    webhook.add_embed(embed)
    resp = webhook.execute()
    time.sleep(2)
