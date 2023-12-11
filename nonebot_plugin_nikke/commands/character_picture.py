import json
import os
import httpx

from nonebot import on_command
from nonebot.adapters import Bot, Event
from nonebot.log import logger
from nonebot.adapters.onebot.v11 import MessageSegment

   
current_directory = os.path.dirname(__file__)
json_file_path = os.path.join(current_directory, 'character_data.json')

with open(json_file_path, 'r', encoding='utf-8') as file:
    character_data = json.load(file)

cmd_character_gamekee = on_command("nk角评", aliases={"nikke角评"})

async def get_character_image(character_name):
    for id, data in character_data.items():
        if data['character_name'] == character_name:
            # 更新后的 URL 格式
            image_url = f"https://git.acwing.com/Perseus_037/nikke-data/-/raw/main/{id}.png"
            try:
                async with httpx.AsyncClient() as client:
                   resp = await client.get(image_url)

                   if resp.status_code == 200:
                       return resp.content
                   
            except httpx.HTTPError as e:
                logger.error(f"获取图片时发生错误: {e}")
                return None
                
    return None

@cmd_character_gamekee.handle()
async def handle_cmd_character_gamekee(bot: Bot, event: Event):
    args = str(event.get_message()).strip()
    character_name = args.split(maxsplit=1)[1] if len(args.split(maxsplit=1)) > 1 else ""

    if not character_name:
        await bot.send(event, "请提供角色名称")
        return

    image_bytes = await get_character_image(character_name)
    if image_bytes:
        await bot.send(event, MessageSegment.image(image_bytes))
    else:
        await bot.send(event, f"没有找到角色: {character_name}")

