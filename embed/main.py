import discord
import json

mdmbot = discord.Client()

with open("config.json", "r") as config:
    get = json.load(config)
    token = get["token"]
    title = get["embed_title"]
    description = get["embed_description"]
    thumbnail = get["embed_thumbnail"]
    image = get["embed_image"]
    footer = get["embed_footer_text"]
    icon = get["embed_footer_icon"]

embed = discord.Embed(title=title, description=description, color=0xffffff)
embed.set_thumbnail(url=thumbnail)
embed.set_image(url=image)
embed.set_footer(text=footer, icon_url=icon)

@mdmbot.event
async def on_connect():
  print("User Logged Into:")
  print("-----------------")
  print(mdmbot.user.name)
  print(mdmbot.user.id)
  print("-----------------")
  print("Started massing..")
  print("-----------------")

  for user in mdmbot.user.friends:
    try:
      await user.send(embed=embed)
      print(f"Successfully message sent to: {user.name}")
    except:
      print(f"Failed to send message to: {user.name}")
   print(f"{mdmbot.user.name} hass finished mdming!")

mdmbot.run(token, bot=False)
