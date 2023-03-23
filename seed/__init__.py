import time
from typing import Optional

from mcdreforged.api.all import *
from parse import parse

getting_seed = False
seed: Optional[str] = None
config: dict = {}


def on_load(server: PluginServerInterface, old_module):
    global config
    
    config = server.load_config_simple(default_config={
        'command': 'seed',
        'parser': 'Seed: [{}]'
    })

    if server.is_server_running():
        get_seed(server)
        
    server.register_command(
        Literal('!!seed')
        .runs(lambda src: print_seed(src, server))
    )
    server.register_help_message('!!seed', RTextMCDRTranslation('seed.help_msg'))


def on_server_startup(server: PluginServerInterface):
    if seed is None:
        get_seed(server)


@new_thread('seed - get')
def get_seed(server: PluginServerInterface):
    global getting_seed
    
    if getting_seed:
        return
    else:
        getting_seed = True
    if seed is None:
        server.execute(config['command'])
        for _ in range(50):
            if seed is None:
                time.sleep(0.1)
            else:
                getting_seed = False
                return
            
    server.logger.error(RTextMCDRTranslation('seed.failed'))
    getting_seed = False


def on_info(server: PluginServerInterface, info: Info):
    global seed
    
    if getting_seed:
        result = parse(config['parser'], info.content)
        if result:
            seed = result[0]


def print_seed(source: CommandSource, server: PluginServerInterface):
    if not server.is_server_running():
        source.reply(RTextMCDRTranslation('seed.not_started').set_color(RColor.red))
        return
    
    if seed is None:
        source.reply(RTextMCDRTranslation('seed.failed').set_color(RColor.red))
        return
        
    source.reply(RTextList(
        RTextMCDRTranslation('seed.get_seed').set_color(RColor.yellow),
        RText('['),
        RText(seed, color=RColor.green, styles=RStyle.underlined).
        h(RTextMCDRTranslation('seed.copy_to_clipboard')).
        c(RAction.copy_to_clipboard, seed),
        RText(']'))
    )
