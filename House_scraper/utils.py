from discord_webhook import DiscordWebhook, DiscordEmbed
from .constants import *
import time


def on_message(status_code: int, website: str):
    webhook = DiscordWebhook(
        url=f"{PREFIX}{ERRORWEBHOOK}"
    )
    embed = DiscordEmbed(title="REQUEST_ERROR", color=COLOR_DS, url=website)
    embed.set_thumbnail(url=IMAGE_ERROR_2)
    embed.add_embed_field(name="STATUS_CODE", value=status_code, inline=True)
    embed.set_footer(
        text="Error_Monitor",
        icon_url=IMAGE_ERROR,
    )
    embed.set_timestamp()
    webhook.add_embed(embed)
    resp = webhook.execute()
    time.sleep(2)
