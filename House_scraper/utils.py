from io import TextIOWrapper
from discord_webhook import DiscordWebhook, DiscordEmbed
from constants import *
import time


def on_message(status_code: int, website: str):
    webhook = DiscordWebhook(url=f"{PREFIX}{ERRORWEBHOOK}")
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


# Unless you are working in a system with limited memory
# reading 288 lines isn't much
def remove_old_entries(csvfile):
    csvfile.seek(0)  # Just in case go to start
    lines = csvfile.readlines()[-5:]  # Read the last 288 lines
    csvfile.truncate(0)  # Empty the file
    csvfile.writelines(lines)  # Put back just the desired lines

    return csvfile


# read out the contents of the file
# delete all the data after reaching 500 lines
# send a webhook message to discord
def read_len_line(csvfile: TextIOWrapper, website: str):
    with open("data.csv", "r") as f:
        lines = f.readlines()
        if len(lines) >= 500:
            csvfile.truncate(0)
            lines_error(len(lines), website)


def lines_error(len: int, website: str):
    webhook = DiscordWebhook(url=f"{PREFIX}{ERRORWEBHOOK}")
    embed = DiscordEmbed(title="LINES_ERROR", color=COLOR_DS, url=website)
    embed.set_thumbnail(url=IMAGE_ERROR_2)
    embed.add_embed_field(name="NUMER_LINES", value=len, inline=True)
    embed.set_footer(
        text="Error_Monitor",
        icon_url=IMAGE_ERROR,
    )
    embed.set_timestamp()
    webhook.add_embed(embed)
    resp = webhook.execute()
    time.sleep(2)
