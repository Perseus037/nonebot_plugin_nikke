import importlib
from pathlib import Path

from nonebot.plugin import PluginMetadata

__version__ = "0.1.0.post1"
__plugin_meta__ = PluginMetadata(
    name="nonebot_plugin_nikke",
    description="胜利女神：妮姬多功能插件",
    usage="使用命令：nikke 角色名称 或 nk 角色名称",
    homepage="https://github.com/Perseus037/nonebot_plugin_nikke",
    type="application",
    config=None,
    supported_adapters={"~onebot.v11"},
)

def load_commands():
    command_path = Path(__file__).parent / 'commands'
    if not command_path.is_dir():
        print(f"Commands directory not found: {command_path}")
        return

    for module in command_path.iterdir():
        if module.is_file() and module.suffix == '.py' and not module.stem.startswith('_'):
            module_name = f"{__package__}.commands.{module.stem}"
            importlib.import_module(module_name)

load_commands()



