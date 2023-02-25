from mcdreforged.api.all import *

server_inst: ServerInterface

get_seed = False


def on_load(server: ServerInterface, old_module):
    global server_inst
    server_inst = server
    server.register_command(Literal('!!seed').runs(run))
    server.register_help_message('!!seed', 'get world seed')


def run():
    global get_seed
    get_seed = True
    server_inst.execute('seed')


# reference code https://github.com/MCDReforged/Seed
def on_info(server: ServerInterface, info: Info):
    global get_seed
    if info.content.startswith('Seed: [') and get_seed:
        seed = info.content.split('[')[1].split(']')[0]
        server.execute(
            'tellraw @a [{"text":"服务器种子: [","color":"yellow"},{"text":"' + seed + '","color":"green","insertion":"' + seed + '","clickEvent":{"action":"copy_to_clipboard","value":"'+ seed + '"},"hoverEvent":{"action":"show_text","value":"点击复制到剪贴板"}},{"text":"]","color":"yellow"}]')
        get_seed = False
