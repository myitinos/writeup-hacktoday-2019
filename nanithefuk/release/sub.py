import subprocess


def start(executable_file):
    return subprocess.Popen(
        executable_file,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )


def read(process, n=14):
    return process.stdout.read(n)  # .decode('utf8')


def write(process, message):
    process.stdin.write(f"{message.strip()}\n".encode("utf-8"))
    process.stdin.flush()


def terminate(process):
    process.stdin.close()
    process.terminate()
    process.wait(timeout=0.2)


process = start("./nani-the-fuk")

# s = "s1g_c0ntorl_fl0w_xD_"
s = ''

while len(s) < 20:
    for i in range(255):
        process = start("./nani-the-fuk")
        read(process, 13)
        for j in s:
            read(process)
            write(process, j)
        read(process)
        write(process, chr(i))
        output = read(process)
        terminate(process)
        if output != b'':
            s = s + chr(i)
            print(s)
            break

print('hacktoday{'+s+'}')
