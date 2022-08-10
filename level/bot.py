import requests
from discord import Webhook, RequestsWebhookAdapter

webhook = Webhook.from_url("https://discord.com/api/webhooks/1002131463900250193/R-F2BSMowbOde_v2w1A3V2D0kSu0z79NWD1-Sj9HT8QanczwBuj8xdCiQx_KICfnUSCT", adapter=RequestsWebhookAdapter())
#webhook.send("Hello")
webhook.avatar
#webhook.edit_message(message_id= 1002131737171726366 , fields= 'none')
webhook.delete_message(message_id=1002132066831446066)