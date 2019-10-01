import string
import os
import shutil
import subprocess
import base64
import itertools
import random


def start(executable_file):
    return subprocess.Popen(
        executable_file,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )


def read(process, n=14):
    return process.stdout.read(n).decode('utf8')


def write(process, message):
    process.stdin.write(message.strip() + "\n".encode("utf-8"))
    process.stdin.flush()


def terminate(process):
    process.stdin.close()
    process.terminate()
    process.wait(timeout=0.2)


def split_n(target, n=32):
    return [target[i:i+n] for i in range(0, len(target), n)]


def compare_last_block(a):
    # a = split_n(a)
    # print(a)
    # print(b)
    # print(len(a))
    sa = a[-32:]
    sa = split_n(sa, 8)

    sb = target_split[int(len(a)/32-1)]
    sb = split_n(sb, 8)

    # print(sa, sb)
    return (sa[0] == sb[0], sa[1] == sb[1], sa[2] == sb[2], sa[3] == sb[3])


n = 32

target = '010110110000111010011011111010001000010001001111100110110110111100000001000000100111110000101001110010100110101111011010101010001100100000000001000110100110100110110100011000000001101001101001001101101101010101001110111011100011101011011010110010101110101011111111010110101010111111011110'
target_split = [target[i:i+n] for i in range(0, len(target), n)]

base = 'cya'
init = '0000'

shutil.copy(base, init)

ans = 'hacktoday{_hets_'
output = ''
current_name = ''
last_name = init

pp = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_{}'
pp = string.printable.replace('/', '')
# pv = 'aiueoAIUEO'
# pk =

# blocks = []
# for i in itertools.product(pp, repeat=4):
#     blocks.append(''.join(i))
#     # print(i)
# random.shuffle(blocks)

a = '5emuEMU-'
b = 'pqrstuvw'
c = '3cksCkS'
d = 'XYZ_'

# for block in itertools.product('0', '0', '0', pp):
for block in itertools.product(a, b, c, d):
    block = ''.join(block)
    current_name = ans + block
    os.rename(last_name, current_name)
    last_name = current_name
    # print(current_name)
    tmp = start('./' + current_name)
    output = read(tmp, 32)
    output = base64.decodebytes(output.encode('utf8'))
    output = "".join(["{:08b}".format(x) for x in output])
    # print(output, target)
    if True in compare_last_block(output):
        print(compare_last_block(output), block)
'''
while output != target:
    # for block in itertools.product('0', '0', '0', pp):
    for block in itertools.product(pp):
        block = '000' + block[0]
        current_name = ans + block
        os.rename(last_name, current_name)
        last_name = current_name
        print(current_name)

        tmp = start('./' + current_name)
        output = read(tmp, 32)
        output = base64.decodebytes(output.encode('utf8'))
        output = "".join(["{:08b}".format(x) for x in output])

        # print(output, target)
        if True in compare_last_block(output):
            print(compare_last_block(output), ans)
        # print(compare_last_block(output), ans)
        # if compare_last_block(output):
        #     ans = ans + block
        #     print(ans)
        #     break

# print(ans)
'''
