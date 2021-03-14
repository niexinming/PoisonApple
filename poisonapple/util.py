"""poisonapple.util"""

import os
import crayons

STATUS_MESSAGES = {
    'failure':          '[!] Failure! The persistence mechansim action failed',
    'python_error':     '[-] Error! Traceback',
    'missing_command':  '[-] Error! Need to specifiy either --command <COMMAND> OR --popup',
    'missing_option':   '[-] Error! Missing required option, see --help for more info...',
    'success':          '[+] Success! The persistence mechanism action was successful',
}


def print_error(name, text=str()):
    message = STATUS_MESSAGES[name]
    if text:
        message += f': {text}'
    if message.startswith('[+]'):
        message_with_color = crayons.green(message)
    elif message.startswith('[-]'):
        message_with_color = crayons.red(message)
    elif message.startswith('[!]'):
        message_with_color = crayons.magenta(message)
    elif message.startswith('[~]'):
        message_with_color = crayons.yellow(message)
    else:
        message_with_color = crayons.white(message)
    print(message_with_color)


def get_popup_command(technique_name):
    directory = os.path.abspath(os.path.dirname(__file__))
    popup = os.path.join(directory, 'bin/popup.bin')
    return f'{popup} {technique_name}'
