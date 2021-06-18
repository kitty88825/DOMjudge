import sys


str_list = [
    'D', 'E', 'F', 'G', 'H',
    'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R',
    'S', 'T', 'U', 'V', 'W',
    'X', 'Y', 'Z', 'A', 'B', 'C',
]


def decode_text(text: str):
    encode_list = [
        '00', '01', '100', '101', '1100',
        '1101', '11100', '11101', '111100', '111101',
    ]
    if text[0:2] in encode_list:
        return f'{encode_list.index(text[0:2])}{encode_list.index(text[2::])}'
    elif text[0:3] in encode_list:
        return f'{encode_list.index(text[0:3])}{encode_list.index(text[3::])}'


for line in sys.stdin.read().splitlines()[1::]:
    num = int(decode_text(line))
    print(str_list[num-1])
