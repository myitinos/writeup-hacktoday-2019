#! /usr/env/bin python3
import string
import os
from shutil import copy
from subprocess import Popen, PIPE
import base64
import itertools
import random


def start(executable_file):
    return Popen(
        executable_file,
        stdin=PIPE,
        stdout=PIPE,
        stderr=PIPE
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


def main():
    target = 'Ww6b6IRPm28BAnwpymvaqMgBGmm0YBppNtVO7jrayur/Wq/e'


if __name__ == "__main__":
    main()

n = 32

target = 'Ww6b6IRPm28BAnwpymvaqMgBGmm0YBppNtVO7jrayur/Wq/e'
target_split = [target[i:i+n] for i in range(0, len(target), n)]

base = 'cya'
init = '0000'

copy(base, init)

ans = 'hacktoday{_hets_'
output = ''
current_name = ''
last_name = init

possible_character = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-{}'

# for block in itertools.product('0', '0', '0', pp):
for block in itertools.product(a, repeat=4):
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
