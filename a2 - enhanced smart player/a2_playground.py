from block import Block
from settings import COLOUR_LIST


logo = '''
   _____                          _    _       _
  / ____|                        | |  | |     (_)
 | (___   __ ___   ____   ___   _| |  | |_ __  _
  \___ \ / _` \ \ / /\ \ / / | | | |  | | '_ \| |
  ____) | (_| |\ V /  \ V /| |_| | |__| | | | | |
 |_____/ \__,_| \_/    \_/  \__, |\____/|_| |_|_|
                             __/ |
                            |___/
'''


def block_simple0() -> Block:
    """
    0
    """
    b0 = Block(position=(0, 0), size=100, colour=(1, 128, 181), level=0, max_depth=0)
    mb = b0
    return mb


def block_simple3() -> Block:
    """
    00000000
    00000000
    00000000
    00000000
    00000000
    00000000
    00000000
    00000000
    """
    b0 = Block(position=(0, 0), size=100, colour=(1, 128, 181), level=0, max_depth=3)
    mb = b0
    return mb


def block_two_level1() -> Block:
    """
    00
    20
    """
    b0 = Block(position=(0, 0), size=100, colour=None, level=0, max_depth=1)
    b03 = Block(position=(50, 50), size=50, colour=(1, 128, 181), level=1, max_depth=1)
    b02 = Block(position=(0, 50), size=50, colour=(138, 151, 71), level=1, max_depth=1)
    b01 = Block(position=(0, 0), size=50, colour=(1, 128, 181), level=1, max_depth=1)
    b00 = Block(position=(50, 0), size=50, colour=(1, 128, 181), level=1, max_depth=1)
    b0.children = [b00, b01, b02, b03]
    mb = b0
    return mb


def block_three_level1() -> Block:
    """
    1200
    1233
    1301
    0231
    """
    b0 = Block(position=(0, 0), size=100, colour=None, level=0, max_depth=2)
    b03 = Block(position=(50, 50), size=50, colour=None, level=1, max_depth=2)
    b033 = Block(position=(75, 75), size=25, colour=(199, 44, 58), level=2, max_depth=2)
    b032 = Block(position=(50, 75), size=25, colour=(255, 211, 92), level=2, max_depth=2)
    b031 = Block(position=(50, 50), size=25, colour=(1, 128, 181), level=2, max_depth=2)
    b030 = Block(position=(75, 50), size=25, colour=(199, 44, 58), level=2, max_depth=2)
    b02 = Block(position=(0, 50), size=50, colour=None, level=1, max_depth=2)
    b023 = Block(position=(25, 75), size=25, colour=(138, 151, 71), level=2, max_depth=2)
    b022 = Block(position=(0, 75), size=25, colour=(1, 128, 181), level=2, max_depth=2)
    b021 = Block(position=(0, 50), size=25, colour=(199, 44, 58), level=2, max_depth=2)
    b020 = Block(position=(25, 50), size=25, colour=(255, 211, 92), level=2, max_depth=2)
    b01 = Block(position=(0, 0), size=50, colour=None, level=1, max_depth=2)
    b013 = Block(position=(25, 25), size=25, colour=(138, 151, 71), level=2, max_depth=2)
    b012 = Block(position=(0, 25), size=25, colour=(199, 44, 58), level=2, max_depth=2)
    b011 = Block(position=(0, 0), size=25, colour=(199, 44, 58), level=2, max_depth=2)
    b010 = Block(position=(25, 0), size=25, colour=(138, 151, 71), level=2, max_depth=2)
    b00 = Block(position=(50, 0), size=50, colour=None, level=1, max_depth=2)
    b003 = Block(position=(75, 25), size=25, colour=(255, 211, 92), level=2, max_depth=2)
    b002 = Block(position=(50, 25), size=25, colour=(255, 211, 92), level=2, max_depth=2)
    b001 = Block(position=(50, 0), size=25, colour=(1, 128, 181), level=2, max_depth=2)
    b000 = Block(position=(75, 0), size=25, colour=(1, 128, 181), level=2, max_depth=2)
    b0.children = [b00, b01, b02, b03]
    b03.children = [b030, b031, b032, b033]
    b02.children = [b020, b021, b022, b023]
    b01.children = [b010, b011, b012, b013]
    b00.children = [b000, b001, b002, b003]
    mb = b0
    return mb


def block_complicated() -> Block:
    """
    22333311
    22333311
    02220033
    10222033
    00003301
    00003300
    00002112
    00003222
    """
    b0 = Block(position=(0, 0), size=100, colour=None, level=0, max_depth=3)
    b03 = Block(position=(50, 50), size=50, colour=None, level=1, max_depth=3)
    b033 = Block(position=(75, 75), size=25, colour=None, level=2, max_depth=3)
    b0333 = Block(position=(87, 87), size=12, colour=(138, 151, 71), level=3, max_depth=3)
    b0332 = Block(position=(75, 87), size=12, colour=(138, 151, 71), level=3, max_depth=3)
    b0331 = Block(position=(75, 75), size=12, colour=(199, 44, 58), level=3, max_depth=3)
    b0330 = Block(position=(87, 75), size=12, colour=(138, 151, 71), level=3, max_depth=3)
    b032 = Block(position=(50, 75), size=25, colour=None, level=2, max_depth=3)
    b0323 = Block(position=(62, 87), size=12, colour=(138, 151, 71), level=3, max_depth=3)
    b0322 = Block(position=(50, 87), size=12, colour=(255, 211, 92), level=3, max_depth=3)
    b0321 = Block(position=(50, 75), size=12, colour=(138, 151, 71), level=3, max_depth=3)
    b0320 = Block(position=(62, 75), size=12, colour=(199, 44, 58), level=3, max_depth=3)
    b031 = Block(position=(50, 50), size=25, colour=(255, 211, 92), level=2, max_depth=3)
    b030 = Block(position=(75, 50), size=25, colour=None, level=2, max_depth=3)
    b0303 = Block(position=(87, 62), size=12, colour=(1, 128, 181), level=3, max_depth=3)
    b0302 = Block(position=(75, 62), size=12, colour=(1, 128, 181), level=3, max_depth=3)
    b0301 = Block(position=(75, 50), size=12, colour=(1, 128, 181), level=3, max_depth=3)
    b0300 = Block(position=(87, 50), size=12, colour=(199, 44, 58), level=3, max_depth=3)
    b02 = Block(position=(0, 50), size=50, colour=(1, 128, 181), level=1, max_depth=3)
    b01 = Block(position=(0, 0), size=50, colour=None, level=1, max_depth=3)
    b013 = Block(position=(25, 25), size=25, colour=(138, 151, 71), level=2, max_depth=3)
    b012 = Block(position=(0, 25), size=25, colour=None, level=2, max_depth=3)
    b0123 = Block(position=(12, 37), size=12, colour=(1, 128, 181), level=3, max_depth=3)
    b0122 = Block(position=(0, 37), size=12, colour=(199, 44, 58), level=3, max_depth=3)
    b0121 = Block(position=(0, 25), size=12, colour=(1, 128, 181), level=3, max_depth=3)
    b0120 = Block(position=(12, 25), size=12, colour=(138, 151, 71), level=3, max_depth=3)
    b011 = Block(position=(0, 0), size=25, colour=(138, 151, 71), level=2, max_depth=3)
    b010 = Block(position=(25, 0), size=25, colour=(255, 211, 92), level=2, max_depth=3)
    b00 = Block(position=(50, 0), size=50, colour=None, level=1, max_depth=3)
    b003 = Block(position=(75, 25), size=25, colour=(255, 211, 92), level=2, max_depth=3)
    b002 = Block(position=(50, 25), size=25, colour=None, level=2, max_depth=3)
    b0023 = Block(position=(62, 37), size=12, colour=(1, 128, 181), level=3, max_depth=3)
    b0022 = Block(position=(50, 37), size=12, colour=(138, 151, 71), level=3, max_depth=3)
    b0021 = Block(position=(50, 25), size=12, colour=(1, 128, 181), level=3, max_depth=3)
    b0020 = Block(position=(62, 25), size=12, colour=(1, 128, 181), level=3, max_depth=3)
    b001 = Block(position=(50, 0), size=25, colour=(255, 211, 92), level=2, max_depth=3)
    b000 = Block(position=(75, 0), size=25, colour=(199, 44, 58), level=2, max_depth=3)
    b0.children = [b00, b01, b02, b03]
    b03.children = [b030, b031, b032, b033]
    b033.children = [b0330, b0331, b0332, b0333]
    b032.children = [b0320, b0321, b0322, b0323]
    b030.children = [b0300, b0301, b0302, b0303]
    b01.children = [b010, b011, b012, b013]
    b012.children = [b0120, b0121, b0122, b0123]
    b00.children = [b000, b001, b002, b003]
    b002.children = [b0020, b0021, b0022, b0023]
    mb = b0
    return mb


def block_very_complicated() -> Block:
    """
    0333331133333313
    3033331133333310
    1102330233332233
    3001331333332233
    2222320230112222
    2222233202312222
    2222131133112222
    2222333033012222
    3123102233201111
    2312022333121111
    2213001113001111
    2200001133121111
    1111110103333323
    1111112313013300
    1111110001030022
    1111110003310022
    """
    b0 = Block(position=(0, 0), size=100, colour=None, level=0, max_depth=4)
    b03 = Block(position=(50, 50), size=50, colour=None, level=1, max_depth=4)
    b033 = Block(position=(75, 75), size=25, colour=None, level=2, max_depth=4)
    b0333 = Block(position=(87, 87), size=12, colour=(138, 151, 71), level=3, max_depth=4)
    b0332 = Block(position=(75, 87), size=12, colour=(1, 128, 181), level=3, max_depth=4)
    b0331 = Block(position=(75, 75), size=12, colour=(255, 211, 92), level=3, max_depth=4)
    b0330 = Block(position=(87, 75), size=12, colour=None, level=3, max_depth=4)
    b03303 = Block(position=(93, 81), size=6, colour=(1, 128, 181), level=4, max_depth=4)
    b03302 = Block(position=(87, 81), size=6, colour=(1, 128, 181), level=4, max_depth=4)
    b03301 = Block(position=(87, 75), size=6, colour=(138, 151, 71), level=4, max_depth=4)
    b03300 = Block(position=(93, 75), size=6, colour=(255, 211, 92), level=4, max_depth=4)
    b032 = Block(position=(50, 75), size=25, colour=None, level=2, max_depth=4)
    b0323 = Block(position=(62, 87), size=12, colour=None, level=3, max_depth=4)
    b03233 = Block(position=(68, 93), size=6, colour=(199, 44, 58), level=4, max_depth=4)
    b03232 = Block(position=(62, 93), size=6, colour=(255, 211, 92), level=4, max_depth=4)
    b03231 = Block(position=(62, 87), size=6, colour=(1, 128, 181), level=4, max_depth=4)
    b03230 = Block(position=(68, 87), size=6, colour=(255, 211, 92), level=4, max_depth=4)
    b0322 = Block(position=(50, 87), size=12, colour=None, level=3, max_depth=4)
    b03223 = Block(position=(56, 93), size=6, colour=(255, 211, 92), level=4, max_depth=4)
    b03222 = Block(position=(50, 93), size=6, colour=(1, 128, 181), level=4, max_depth=4)
    b03221 = Block(position=(50, 87), size=6, colour=(1, 128, 181), level=4, max_depth=4)
    b03220 = Block(position=(56, 87), size=6, colour=(199, 44, 58), level=4, max_depth=4)
    b0321 = Block(position=(50, 75), size=12, colour=None, level=3, max_depth=4)
    b03213 = Block(position=(56, 81), size=6, colour=(255, 211, 92), level=4, max_depth=4)
    b03212 = Block(position=(50, 81), size=6, colour=(199, 44, 58), level=4, max_depth=4)
    b03211 = Block(position=(50, 75), size=6, colour=(1, 128, 181), level=4, max_depth=4)
    b03210 = Block(position=(56, 75), size=6, colour=(255, 211, 92), level=4, max_depth=4)
    b0320 = Block(position=(62, 75), size=12, colour=None, level=3, max_depth=4)
    b03203 = Block(position=(68, 81), size=6, colour=(199, 44, 58), level=4, max_depth=4)
    b03202 = Block(position=(62, 81), size=6, colour=(1, 128, 181), level=4, max_depth=4)
    b03201 = Block(position=(62, 75), size=6, colour=(255, 211, 92), level=4, max_depth=4)
    b03200 = Block(position=(68, 75), size=6, colour=(255, 211, 92), level=4, max_depth=4)
    b031 = Block(position=(50, 50), size=25, colour=None, level=2, max_depth=4)
    b0313 = Block(position=(62, 62), size=12, colour=None, level=3, max_depth=4)
    b03133 = Block(position=(68, 68), size=6, colour=(138, 151, 71), level=4, max_depth=4)
    b03132 = Block(position=(62, 68), size=6, colour=(199, 44, 58), level=4, max_depth=4)
    b03131 = Block(position=(62, 62), size=6, colour=(1, 128, 181), level=4, max_depth=4)
    b03130 = Block(position=(68, 62), size=6, colour=(1, 128, 181), level=4, max_depth=4)
    b0312 = Block(position=(50, 62), size=12, colour=None, level=3, max_depth=4)
    b03123 = Block(position=(56, 68), size=6, colour=(255, 211, 92), level=4, max_depth=4)
    b03122 = Block(position=(50, 68), size=6, colour=(255, 211, 92), level=4, max_depth=4)
    b03121 = Block(position=(50, 62), size=6, colour=(199, 44, 58), level=4, max_depth=4)
    b03120 = Block(position=(56, 62), size=6, colour=(255, 211, 92), level=4, max_depth=4)
    b0311 = Block(position=(50, 50), size=12, colour=(255, 211, 92), level=3, max_depth=4)
    b0310 = Block(position=(62, 50), size=12, colour=None, level=3, max_depth=4)
    b03103 = Block(position=(68, 56), size=6, colour=(138, 151, 71), level=4, max_depth=4)
    b03102 = Block(position=(62, 56), size=6, colour=(199, 44, 58), level=4, max_depth=4)
    b03101 = Block(position=(62, 50), size=6, colour=(138, 151, 71), level=4, max_depth=4)
    b03100 = Block(position=(68, 50), size=6, colour=(1, 128, 181), level=4, max_depth=4)
    b030 = Block(position=(75, 50), size=25, colour=(199, 44, 58), level=2, max_depth=4)
    b02 = Block(position=(0, 50), size=50, colour=None, level=1, max_depth=4)
    b023 = Block(position=(25, 75), size=25, colour=None, level=2, max_depth=4)
    b0233 = Block(position=(37, 87), size=12, colour=(1, 128, 181), level=3, max_depth=4)
    b0232 = Block(position=(25, 87), size=12, colour=(199, 44, 58), level=3, max_depth=4)
    b0231 = Block(position=(25, 75), size=12, colour=(199, 44, 58), level=3, max_depth=4)
    b0230 = Block(position=(37, 75), size=12, colour=None, level=3, max_depth=4)
    b02303 = Block(position=(43, 81), size=6, colour=(255, 211, 92), level=4, max_depth=4)
    b02302 = Block(position=(37, 81), size=6, colour=(138, 151, 71), level=4, max_depth=4)
    b02301 = Block(position=(37, 75), size=6, colour=(1, 128, 181), level=4, max_depth=4)
    b02300 = Block(position=(43, 75), size=6, colour=(199, 44, 58), level=4, max_depth=4)
    b022 = Block(position=(0, 75), size=25, colour=(199, 44, 58), level=2, max_depth=4)
    b021 = Block(position=(0, 50), size=25, colour=None, level=2, max_depth=4)
    b0213 = Block(position=(12, 62), size=12, colour=None, level=3, max_depth=4)
    b02133 = Block(position=(18, 68), size=6, colour=(1, 128, 181), level=4, max_depth=4)
    b02132 = Block(position=(12, 68), size=6, colour=(1, 128, 181), level=4, max_depth=4)
    b02131 = Block(position=(12, 62), size=6, colour=(199, 44, 58), level=4, max_depth=4)
    b02130 = Block(position=(18, 62), size=6, colour=(255, 211, 92), level=4, max_depth=4)
    b0212 = Block(position=(0, 62), size=12, colour=(138, 151, 71), level=3, max_depth=4)
    b0211 = Block(position=(0, 50), size=12, colour=None, level=3, max_depth=4)
    b02113 = Block(position=(6, 56), size=6, colour=(255, 211, 92), level=4, max_depth=4)
    b02112 = Block(position=(0, 56), size=6, colour=(138, 151, 71), level=4, max_depth=4)
    b02111 = Block(position=(0, 50), size=6, colour=(255, 211, 92), level=4, max_depth=4)
    b02110 = Block(position=(6, 50), size=6, colour=(199, 44, 58), level=4, max_depth=4)
    b0210 = Block(position=(12, 50), size=12, colour=None, level=3, max_depth=4)
    b02103 = Block(position=(18, 56), size=6, colour=(138, 151, 71), level=4, max_depth=4)
    b02102 = Block(position=(12, 56), size=6, colour=(199, 44, 58), level=4, max_depth=4)
    b02101 = Block(position=(12, 50), size=6, colour=(138, 151, 71), level=4, max_depth=4)
    b02100 = Block(position=(18, 50), size=6, colour=(255, 211, 92), level=4, max_depth=4)
    b020 = Block(position=(25, 50), size=25, colour=None, level=2, max_depth=4)
    b0203 = Block(position=(37, 62), size=12, colour=(199, 44, 58), level=3, max_depth=4)
    b0202 = Block(position=(25, 62), size=12, colour=(1, 128, 181), level=3, max_depth=4)
    b0201 = Block(position=(25, 50), size=12, colour=None, level=3, max_depth=4)
    b02013 = Block(position=(31, 56), size=6, colour=(138, 151, 71), level=4, max_depth=4)
    b02012 = Block(position=(25, 56), size=6, colour=(1, 128, 181), level=4, max_depth=4)
    b02011 = Block(position=(25, 50), size=6, colour=(199, 44, 58), level=4, max_depth=4)
    b02010 = Block(position=(31, 50), size=6, colour=(1, 128, 181), level=4, max_depth=4)
    b0200 = Block(position=(37, 50), size=12, colour=None, level=3, max_depth=4)
    b02003 = Block(position=(43, 56), size=6, colour=(255, 211, 92), level=4, max_depth=4)
    b02002 = Block(position=(37, 56), size=6, colour=(138, 151, 71), level=4, max_depth=4)
    b02001 = Block(position=(37, 50), size=6, colour=(138, 151, 71), level=4, max_depth=4)
    b02000 = Block(position=(43, 50), size=6, colour=(138, 151, 71), level=4, max_depth=4)
    b01 = Block(position=(0, 0), size=50, colour=None, level=1, max_depth=4)
    b013 = Block(position=(25, 25), size=25, colour=None, level=2, max_depth=4)
    b0133 = Block(position=(37, 37), size=12, colour=None, level=3, max_depth=4)
    b01333 = Block(position=(43, 43), size=6, colour=(1, 128, 181), level=4, max_depth=4)
    b01332 = Block(position=(37, 43), size=6, colour=(255, 211, 92), level=4, max_depth=4)
    b01331 = Block(position=(37, 37), size=6, colour=(199, 44, 58), level=4, max_depth=4)
    b01330 = Block(position=(43, 37), size=6, colour=(199, 44, 58), level=4, max_depth=4)
    b0132 = Block(position=(25, 37), size=12, colour=None, level=3, max_depth=4)
    b01323 = Block(position=(31, 43), size=6, colour=(255, 211, 92), level=4, max_depth=4)
    b01322 = Block(position=(25, 43), size=6, colour=(255, 211, 92), level=4, max_depth=4)
    b01321 = Block(position=(25, 37), size=6, colour=(199, 44, 58), level=4, max_depth=4)
    b01320 = Block(position=(31, 37), size=6, colour=(255, 211, 92), level=4, max_depth=4)
    b0131 = Block(position=(25, 25), size=12, colour=None, level=3, max_depth=4)
    b01313 = Block(position=(31, 31), size=6, colour=(255, 211, 92), level=4, max_depth=4)
    b01312 = Block(position=(25, 31), size=6, colour=(138, 151, 71), level=4, max_depth=4)
    b01311 = Block(position=(25, 25), size=6, colour=(255, 211, 92), level=4, max_depth=4)
    b01310 = Block(position=(31, 25), size=6, colour=(138, 151, 71), level=4, max_depth=4)
    b0130 = Block(position=(37, 25), size=12, colour=None, level=3, max_depth=4)
    b01303 = Block(position=(43, 31), size=6, colour=(138, 151, 71), level=4, max_depth=4)
    b01302 = Block(position=(37, 31), size=6, colour=(255, 211, 92), level=4, max_depth=4)
    b01301 = Block(position=(37, 25), size=6, colour=(1, 128, 181), level=4, max_depth=4)
    b01300 = Block(position=(43, 25), size=6, colour=(138, 151, 71), level=4, max_depth=4)
    b012 = Block(position=(0, 25), size=25, colour=(138, 151, 71), level=2, max_depth=4)
    b011 = Block(position=(0, 0), size=25, colour=None, level=2, max_depth=4)
    b0113 = Block(position=(12, 12), size=12, colour=None, level=3, max_depth=4)
    b01133 = Block(position=(18, 18), size=6, colour=(199, 44, 58), level=4, max_depth=4)
    b01132 = Block(position=(12, 18), size=6, colour=(1, 128, 181), level=4, max_depth=4)
    b01131 = Block(position=(12, 12), size=6, colour=(1, 128, 181), level=4, max_depth=4)
    b01130 = Block(position=(18, 12), size=6, colour=(138, 151, 71), level=4, max_depth=4)
    b0112 = Block(position=(0, 12), size=12, colour=None, level=3, max_depth=4)
    b01123 = Block(position=(6, 18), size=6, colour=(1, 128, 181), level=4, max_depth=4)
    b01122 = Block(position=(0, 18), size=6, colour=(255, 211, 92), level=4, max_depth=4)
    b01121 = Block(position=(0, 12), size=6, colour=(199, 44, 58), level=4, max_depth=4)
    b01120 = Block(position=(6, 12), size=6, colour=(199, 44, 58), level=4, max_depth=4)
    b0111 = Block(position=(0, 0), size=12, colour=None, level=3, max_depth=4)
    b01113 = Block(position=(6, 6), size=6, colour=(1, 128, 181), level=4, max_depth=4)
    b01112 = Block(position=(0, 6), size=6, colour=(255, 211, 92), level=4, max_depth=4)
    b01111 = Block(position=(0, 0), size=6, colour=(1, 128, 181), level=4, max_depth=4)
    b01110 = Block(position=(6, 0), size=6, colour=(255, 211, 92), level=4, max_depth=4)
    b0110 = Block(position=(12, 0), size=12, colour=None, level=3, max_depth=4)
    b01103 = Block(position=(18, 6), size=6, colour=(255, 211, 92), level=4, max_depth=4)
    b01102 = Block(position=(12, 6), size=6, colour=(255, 211, 92), level=4, max_depth=4)
    b01101 = Block(position=(12, 0), size=6, colour=(255, 211, 92), level=4, max_depth=4)
    b01100 = Block(position=(18, 0), size=6, colour=(255, 211, 92), level=4, max_depth=4)
    b010 = Block(position=(25, 0), size=25, colour=None, level=2, max_depth=4)
    b0103 = Block(position=(37, 12), size=12, colour=None, level=3, max_depth=4)
    b01033 = Block(position=(43, 18), size=6, colour=(255, 211, 92), level=4, max_depth=4)
    b01032 = Block(position=(37, 18), size=6, colour=(199, 44, 58), level=4, max_depth=4)
    b01031 = Block(position=(37, 12), size=6, colour=(1, 128, 181), level=4, max_depth=4)
    b01030 = Block(position=(43, 12), size=6, colour=(138, 151, 71), level=4, max_depth=4)
    b0102 = Block(position=(25, 12), size=12, colour=(255, 211, 92), level=3, max_depth=4)
    b0101 = Block(position=(25, 0), size=12, colour=(255, 211, 92), level=3, max_depth=4)
    b0100 = Block(position=(37, 0), size=12, colour=None, level=3, max_depth=4)
    b01003 = Block(position=(43, 6), size=6, colour=(199, 44, 58), level=4, max_depth=4)
    b01002 = Block(position=(37, 6), size=6, colour=(199, 44, 58), level=4, max_depth=4)
    b01001 = Block(position=(37, 0), size=6, colour=(199, 44, 58), level=4, max_depth=4)
    b01000 = Block(position=(43, 0), size=6, colour=(199, 44, 58), level=4, max_depth=4)
    b00 = Block(position=(50, 0), size=50, colour=None, level=1, max_depth=4)
    b003 = Block(position=(75, 25), size=25, colour=(138, 151, 71), level=2, max_depth=4)
    b002 = Block(position=(50, 25), size=25, colour=None, level=2, max_depth=4)
    b0023 = Block(position=(62, 37), size=12, colour=None, level=3, max_depth=4)
    b00233 = Block(position=(68, 43), size=6, colour=(199, 44, 58), level=4, max_depth=4)
    b00232 = Block(position=(62, 43), size=6, colour=(1, 128, 181), level=4, max_depth=4)
    b00231 = Block(position=(62, 37), size=6, colour=(199, 44, 58), level=4, max_depth=4)
    b00230 = Block(position=(68, 37), size=6, colour=(199, 44, 58), level=4, max_depth=4)
    b0022 = Block(position=(50, 37), size=12, colour=(255, 211, 92), level=3, max_depth=4)
    b0021 = Block(position=(50, 25), size=12, colour=None, level=3, max_depth=4)
    b00213 = Block(position=(56, 31), size=6, colour=(138, 151, 71), level=4, max_depth=4)
    b00212 = Block(position=(50, 31), size=6, colour=(1, 128, 181), level=4, max_depth=4)
    b00211 = Block(position=(50, 25), size=6, colour=(255, 211, 92), level=4, max_depth=4)
    b00210 = Block(position=(56, 25), size=6, colour=(1, 128, 181), level=4, max_depth=4)
    b0020 = Block(position=(62, 25), size=12, colour=None, level=3, max_depth=4)
    b00203 = Block(position=(68, 31), size=6, colour=(199, 44, 58), level=4, max_depth=4)
    b00202 = Block(position=(62, 31), size=6, colour=(255, 211, 92), level=4, max_depth=4)
    b00201 = Block(position=(62, 25), size=6, colour=(199, 44, 58), level=4, max_depth=4)
    b00200 = Block(position=(68, 25), size=6, colour=(199, 44, 58), level=4, max_depth=4)
    b001 = Block(position=(50, 0), size=25, colour=(255, 211, 92), level=2, max_depth=4)
    b000 = Block(position=(75, 0), size=25, colour=None, level=2, max_depth=4)
    b0003 = Block(position=(87, 12), size=12, colour=(255, 211, 92), level=3, max_depth=4)
    b0002 = Block(position=(75, 12), size=12, colour=(138, 151, 71), level=3, max_depth=4)
    b0001 = Block(position=(75, 0), size=12, colour=(255, 211, 92), level=3, max_depth=4)
    b0000 = Block(position=(87, 0), size=12, colour=None, level=3, max_depth=4)
    b00003 = Block(position=(93, 6), size=6, colour=(1, 128, 181), level=4, max_depth=4)
    b00002 = Block(position=(87, 6), size=6, colour=(199, 44, 58), level=4, max_depth=4)
    b00001 = Block(position=(87, 0), size=6, colour=(199, 44, 58), level=4, max_depth=4)
    b00000 = Block(position=(93, 0), size=6, colour=(255, 211, 92), level=4, max_depth=4)
    b0.children = [b00, b01, b02, b03]
    b03.children = [b030, b031, b032, b033]
    b033.children = [b0330, b0331, b0332, b0333]
    b0330.children = [b03300, b03301, b03302, b03303]
    b032.children = [b0320, b0321, b0322, b0323]
    b0323.children = [b03230, b03231, b03232, b03233]
    b0322.children = [b03220, b03221, b03222, b03223]
    b0321.children = [b03210, b03211, b03212, b03213]
    b0320.children = [b03200, b03201, b03202, b03203]
    b031.children = [b0310, b0311, b0312, b0313]
    b0313.children = [b03130, b03131, b03132, b03133]
    b0312.children = [b03120, b03121, b03122, b03123]
    b0310.children = [b03100, b03101, b03102, b03103]
    b02.children = [b020, b021, b022, b023]
    b023.children = [b0230, b0231, b0232, b0233]
    b0230.children = [b02300, b02301, b02302, b02303]
    b021.children = [b0210, b0211, b0212, b0213]
    b0213.children = [b02130, b02131, b02132, b02133]
    b0211.children = [b02110, b02111, b02112, b02113]
    b0210.children = [b02100, b02101, b02102, b02103]
    b020.children = [b0200, b0201, b0202, b0203]
    b0201.children = [b02010, b02011, b02012, b02013]
    b0200.children = [b02000, b02001, b02002, b02003]
    b01.children = [b010, b011, b012, b013]
    b013.children = [b0130, b0131, b0132, b0133]
    b0133.children = [b01330, b01331, b01332, b01333]
    b0132.children = [b01320, b01321, b01322, b01323]
    b0131.children = [b01310, b01311, b01312, b01313]
    b0130.children = [b01300, b01301, b01302, b01303]
    b011.children = [b0110, b0111, b0112, b0113]
    b0113.children = [b01130, b01131, b01132, b01133]
    b0112.children = [b01120, b01121, b01122, b01123]
    b0111.children = [b01110, b01111, b01112, b01113]
    b0110.children = [b01100, b01101, b01102, b01103]
    b010.children = [b0100, b0101, b0102, b0103]
    b0103.children = [b01030, b01031, b01032, b01033]
    b0100.children = [b01000, b01001, b01002, b01003]
    b00.children = [b000, b001, b002, b003]
    b002.children = [b0020, b0021, b0022, b0023]
    b0023.children = [b00230, b00231, b00232, b00233]
    b0021.children = [b00210, b00211, b00212, b00213]
    b0020.children = [b00200, b00201, b00202, b00203]
    b000.children = [b0000, b0001, b0002, b0003]
    b0000.children = [b00000, b00001, b00002, b00003]
    mb = b0
    return mb


def block_graph(block) -> str:
    """
    Turn block into a easy to read format.
    """
    from settings import COLOUR_LIST
    if not block.children:
        size = 2 ** (block.max_depth - block.level)
        color_code = str(COLOUR_LIST.index(block.colour))
        return (color_code * size + '\n') * (size - 1) + (color_code * size)
    else:
        c0 = block_graph(block.children[0]).split()
        c1 = block_graph(block.children[1]).split()
        c2 = block_graph(block.children[2]).split()
        c3 = block_graph(block.children[3]).split()
        for i in range(len(c1)):
            c1[i] += c0[i]
            c2[i] += c3[i]
        return '\n'.join(c1 + c2)


def block_playground():
    from block import Block
    from settings import COLOUR_LIST

    # _update_children_positions

    b = block_three_level1()
    print(b)
    b._update_children_positions((10, 10))
    print(b)

    # create_copy

    b = block_three_level1()
    b_copy = b.create_copy()

    # smash

    b = Block(position=(0, 0), size=100, colour=COLOUR_LIST[0], level=0, max_depth=3)
    b.smash()
    print(b)
    print(block_graph(b))

    # swap

    print("before swap")
    print(block_graph(b))
    b.swap(0)
    print('after swap')
    print(block_graph(b))


    # rotate

    print("before rotate")
    print(block_graph(b))
    b.rotate(1)
    print('after rotate')
    print(block_graph(b))

    # paint

    b = block_simple0()
    print("before paint")
    print(block_graph(b))
    b.paint(COLOUR_LIST[1])
    print("after paint")
    print(block_graph(b))

    # combine
    b = block_two_level1()
    print("before combine")
    print(block_graph(b))
    print('after combine')
    b.combine()
    print(block_graph(b))
    print(b)



def blocky_playground():
    from blocky import _block_to_squares

    # _block_to_squares
    b = block_two_level1()
    print(_block_to_squares(b))


def goal_playground():
    from goal import generate_goals, _flatten, PerimeterGoal, BlobGoal
    goals = generate_goals(3)
    print([g.description() for g in goals])

    b = block_three_level1()
    print(block_graph(b))
    print(_flatten(b))

    pg = PerimeterGoal(COLOUR_LIST[0])
    print(pg.score(b))

    bg = BlobGoal(COLOUR_LIST[0])
    print(bg.score((b)))

    bg = BlobGoal(COLOUR_LIST[1])
    print(bg.score((b)))


def player_playground():
    from player import RandomPlayer, SmartPlayer, create_players, _get_block
    b = block_three_level1()

    found = _get_block(b, (0, 0), 0)
    print(block_graph(found))

    found = _get_block(b, (0, 0), 1)
    print(block_graph(found))

    players = create_players(1, 1, [10])
    print(players)


if __name__ == '__main__':
    block_playground()
    # blocky_playground()
    # goal_playground()
    # player_playground()

