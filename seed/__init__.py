from mcdreforged.api.all import *

server_inst: ServerInterface

get_seed = False

seed: str = '0'


def on_load(server: ServerInterface, old_module):
    global server_inst
    server_inst = server

    server.register_command(Literal('!!seed').runs(run))
    server.register_help_message('!!seed', server.tr('seed.help_msg'))


def run():
    global get_seed, seed
    if seed == '0':
        get_seed = True
        server_inst.execute('seed')
    else:
        print_seed(seed)


# reference code https://github.com/MCDReforged/Seed
def on_info(server: ServerInterface, info: Info):
    global get_seed, seed
    if info.content.startswith('Seed: [') and get_seed:
        seed = info.content.split('[')[1].split(']')[0]
        print_seed(seed)
        get_seed = False


def print_seed(value: str):
    server_inst.tell('@a',
                     RTextList(
                         RText(server_inst.tr('seed.get_seed'), color=RColor.yellow),
                         RText('[', color=RColor.white),
                         RText(value, color=RColor.green, styles=RStyle.underlined).set_hover_text(
                             server_inst.tr('seed.copy_to_clipboard')).set_click_event(RAction.copy_to_clipboard, value),
                         RText(']', color=RColor.white))
                     )
