import json
import os
import httpx

from nonebot import on_command
from nonebot.adapters import Bot, Event
from nonebot.log import logger
from nonebot.adapters.onebot.v11 import MessageSegment


current_directory = os.path.dirname(__file__)
json_file_path = os.path.join(current_directory, '..', 'json', 'character_rating.json')

with open(json_file_path, 'r', encoding='utf-8') as file:
    character_rating_data = json.load(file)

cmd_character_rating_gamekee = on_command("nk评分", aliases={"nikke角色评分"})

async def get_character_rating_image(rating_number):
    # 默认情况下已经确保 rating_number 是有效的（1，2 或 3）
    picture_name = character_rating_data.get(f"603260-{rating_number}", {}).get("picture_name")
    if picture_name:
        image_url = f"https://git.acwing.com/Perseus_037/nikke-data/-/raw/main/603260_{rating_number}.png"
        try:
            async with httpx.AsyncClient() as client:
               resp = await client.get(image_url)
               if resp.status_code == 200:
                   return resp.content
        except httpx.HTTPError as e:
            logger.error(f"获取图片时发生错误: {e}")
    return None

@cmd_character_rating_gamekee.handle()
async def _(bot: Bot, event: Event):
    args = str(event.get_message()).strip()
    rating_number = args.split(maxsplit=1)[1] if len(args.split(maxsplit=1)) > 1 else "3"

    if rating_number not in ['1', '2', '3']:
        await bot.send(event, "非法字符，请输入1、2或3查询相应的爆裂阶段")
        return

    image_bytes = await get_character_rating_image(rating_number)
    if image_bytes:
        await bot.send(event, MessageSegment.image(image_bytes))
    else:
        await bot.send(event, "没有找到对应的评分图片")


