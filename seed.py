from mcdreforged.api.all import *

PLUGIN_METADATA = {
    'id': 'seed',
    'version': '1.0.0',
    'name': 'Seed',
    'description': 'Get world seed quickly',
    'author': 'OptiJava',
    'link': 'https://github.com/OptiJava/Seed',
    'dependencies': {
        'mcdreforged': '>=2.0.0',
    }
}

server_inst: ServerInterface

get_seed = False


def on_load(server: ServerInterface, old_module):
    global server_inst
    server_inst = server
    server.register_command(Literal('!!seed').runs(run))
    server.register_help_message('!!seed', 'Get world seed')


def run():
    global get_seed
    get_seed = True
    server_inst.execute('seed')



def on_info(server: ServerInterface, info: Info):
    global get_seed
    if info.content.startswith('Seed: [') and get_seed:
        seed = info.content.split('[')[1].split(']')[0]
        server.execute('tellraw @a [{"text":"Seed:[","bold":false,"italic":false,"underlined":false,"strikethrough":false,"obfuscated":false},{"text":"' + seed + '","color":"green","bold":false,"italic":false,"underlined":false,"strikethrough":false,"obfuscated":false,"insertion":"' + seed + '","clickEvent":{"action":"suggest_command","value":"' + seed + '"},"hoverEvent":{"action":"show_text","value":"点击复制到聊天栏"}},{"text":"]","bold":false,"italic":false,"underlined":false,"strikethrough":false,"obfuscated":false}]')
        get_seed = False

