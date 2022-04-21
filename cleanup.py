banned_things = [
    '.file',
    '.ent',
    '.section',
    '.nan',
    '.section',
    '.end',
    '.ent',
    '.type',
    '.frame',
    '.mask',
    '.fmask',
    '.size',
    '.ident',
    '.rdata,'
    '.module',
    '.module',
    '.previous',
    '#',
    '.rdata',
    '.set'
]


def main() -> None:
    new_contents = ''
    with open('./main.asm', 'r') as f:
        for line in f.readlines():
            if is_banned(line) or line.strip() == '':
                continue
            else:
                new_contents += line
    with open('./main.asm', 'w') as f:
        f.write(new_contents)


def is_banned(line: str) -> bool:
    line = line.strip()
    for thing in banned_things:
        if line.startswith(thing):
            return True

    return False


if __name__ == '__main__':
    main()
