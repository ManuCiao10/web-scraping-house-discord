from discord_webhook import DiscordWebhook, DiscordEmbed
from constants import *
import time

def on_message():
    webhook = DiscordWebhook(url=f"{PREFIX}{ERRORWEBHOOK}")
    embed = DiscordEmbed(title="PROGRAM_CRASHED", color=COLOR_DS, url="https://www.codingem.com/wp-content/uploads/2021/08/try-catch.001-1024x576.jpeg")
    embed.set_thumbnail(url=IMAGE_ERROR_2)
    embed.add_embed_field(name="STATUS_CODE", value=1, inline=True)
    embed.set_footer(
        text="Error_Monitor",
        icon_url=IMAGE_ERROR,
    )
    embed.set_timestamp()
    webhook.add_embed(embed)
    resp = webhook.execute()
    time.sleep(2)

if __name__ == "__main__":
    on_message()