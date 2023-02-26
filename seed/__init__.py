import time
from typing import Optional

from mcdreforged.api.all import *
from parse import parse

getting_seed = False
seed: Optional[str] = None
config: dict = None


def on_load(server: PluginServerInterface, old_module):
    global config
    config = server.load_config_simple(default_config={
        'command': 'seed',
        'parser': 'Seed: [{}]'
    })

    if server.is_server_running():
        get_seed(server)
    server.register_command(Literal('!!seed').runs(print_seed))
    server.register_help_message('!!seed', server.tr('seed.help_msg'))


def on_server_startup(server: PluginServerInterface):
    if seed is None:
        get_seed(server)


@new_thread('seed')
def get_seed(server: PluginServerInterface):
    global seed, getting_seed
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
    server.logger.error(server.tr('seed.failed'))
    getting_seed = False


def on_info(server: ServerInterface, info: Info):
    global getting_seed, seed
    if getting_seed:
        result = parse(config['parser'], info.content)
        if result:
            seed = result[0]


def print_seed(source: CommandSource):
    if seed is None:
        source.reply(RText(RTextMCDRTranslation('seed.failed'), RColor.red))
    source.reply(RTextList(
        RTextMCDRTranslation('seed.get_seed', RColor.yellow),
        RText('[', RColor.white),
        RText(seed, RColor.green, RStyle.underlined).
            h(RTextMCDRTranslation('seed.copy_to_clipboard')).
            c(RAction.copy_to_clipboard, seed),
        RText(']', RColor.white))
    )
