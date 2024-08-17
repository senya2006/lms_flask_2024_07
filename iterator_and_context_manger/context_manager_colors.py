from colors import bcolors


class colorizer:
    def __init__(self, color):
        self.color = color

    def __enter__(self):
        print(self.color, end='')

    def __exit__(self, *args):
        print(bcolors.ENDC, end='')


# Examples:
print('printed in default color')

with colorizer(bcolors.FAIL):  # red
    print('printed in red (FAIL)')

with colorizer(bcolors.GREENBG):  # green background
    print('printed with green background')

with colorizer(bcolors.BOLD + bcolors.BLUEBG):  # bold text with blue background
    print('printed bold with blue background')

print('printed in default color again')

