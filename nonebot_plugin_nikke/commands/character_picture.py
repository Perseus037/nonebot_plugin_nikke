import json
import os
import httpx
from difflib import get_close_matches

from nonebot import on_command, on_message
from nonebot.adapters import Bot, Event
from nonebot.log import logger
from nonebot.adapters.onebot.v11 import MessageSegment
from nonebot.typing import T_State
from nonebot.rule import Rule

   
current_directory = os.path.dirname(__file__)
json_file_path = os.path.join(current_directory, '..', 'json', 'character_data.json')

with open(json_file_path, 'r', encoding='utf-8') as file:
    character_data = json.load(file)

cmd_character_gamekee = on_command("nk角评", aliases={"nikke角评"})

# 创建一个全局字典来存储选择状态
user_selection_states = {}

def get_similar_character_names(character_name):
    all_names = [data['character_name'] for data in character_data.values()]
    similar_character_names = get_close_matches(character_name, all_names, n=5, cutoff=0.3)
    return similar_character_names

async def get_character_image(character_name):
    exact_match = None
    for id, data in character_data.items():
        if data['character_name'] == character_name:
            exact_match = id
            break

    if exact_match:
        image_url = f"https://git.acwing.com/Perseus_037/nikke-data/-/raw/main/{exact_match}.png"

        try:
            async with httpx.AsyncClient() as client:
                resp = await client.get(image_url)
                if resp.status_code == 200:
                    return resp.content
                
        except httpx.HTTPError as e:
            logger.error(f"获取图片时发生错误: {e}")
    return None


@cmd_character_gamekee.handle()
async def handle_cmd_character_gamekee(bot: Bot, event: Event):
    user_id = event.get_user_id()
    args = str(event.get_message()).strip()
    character_name = args.split(maxsplit=1)[1] if len(args.split(maxsplit=1)) > 1 else ""

    if not character_name:
        await bot.send(event, "请提供角色名称")
        return

    image_bytes = await get_character_image(character_name)
    if image_bytes:
        await bot.send(event, MessageSegment.image(image_bytes))

    else:
        similar_character_names = get_similar_character_names(character_name)

        if similar_character_names:
            response = "找到了多个可能的结果，请发送序号来选择吧：\n" + \
                       "\n".join([f"{i+1}.{name}" for i, name in enumerate(similar_character_names)]) + \
                       "\nps：输入0取消选择。"
            await bot.send(event, response)
            # 储存选择状态
            user_selection_states[user_id] = similar_character_names

        else:
            await bot.send(event, f"没有找到与 '{character_name}' 相关的结果")

async def has_selection_state(bot: Bot, event: Event, state: T_State) -> bool:
    user_id = event.get_user_id()
    return user_id in user_selection_states


# 响应数字序号输入
cmd_selection = on_message(rule=Rule(has_selection_state), block=True)


@cmd_selection.handle()
async def handle_selection(bot: Bot, event: Event):
    user_id = event.get_user_id()
    # 检查是否存在选择状态
    if user_id in user_selection_states:
        message = str(event.get_message()).strip()

        if message.isdigit():
            selected_index = int(message) - 1
            
            if selected_index == -1:
                await bot.send(event, "已取消选择")
                user_selection_states.pop(user_id, None)
                return

            if 0 <= selected_index < len(user_selection_states[user_id]):
                selected_character = user_selection_states[user_id][selected_index]
                image_bytes = await get_character_image(selected_character)

                if image_bytes:
                    await bot.send(event, MessageSegment.image(image_bytes))

                else:
                    logger.error(f"Failed to get image for character: {selected_character}")
                    await bot.send(event, "未能获取图片，请稍后重试")
                user_selection_states.pop(user_id, None)

            else:
                await bot.send(event, "无效的选择，请输入正确的数字序号")

        else:
            await bot.send(event, "请输入数字序号进行选择")

    else:
        # 如果没有进行模糊匹配选择，不处理消息
        pass
