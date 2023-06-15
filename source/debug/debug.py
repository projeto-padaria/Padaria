def printError(error) -> None:
    red = '\033[1;31m'
    bold = '\033[;1m'
    reset = '\033[0;0m'
    return print(f'{bold}{red}ERROR: {reset}{error}')

def printSuccess(success) -> None:
    green = '\033[0;32m'
    reset = '\033[0;0m'
    bold = '\033[;1m'
    return print(f'{bold}{green}SUCCESS: {reset}{success}')

def printWarning(warning) -> None:
    reset = '\033[0;0m'
    bold = '\033[;1m'
    yellow = '\033[33m'
    return print(f'{bold}{yellow}WARNING: {reset}{warning}')

def printInfo(info) -> None:
    cyan = '\033[1;36m'
    reset = '\033[0;0m'
    bold = '\033[;1m'
    return print(f'{bold}{cyan}INFO: {reset}{info}')

def printTitle(title) -> None:
    reset = '\033[0;0m'
    bold = '\033[;1m'
    menubar = '—' * len(title)
    return print(f'{bold}{menubar} {title} {menubar} {reset}')