import subprocess
import sys


def get_output(command):
    if type(command) != str:
        print("get_output error : command only string")
        return

    with subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True) as process:
        outputs = process.stdout.read().decode('euc-kr')
        process.kill()
        return outputs


def get_argv():
    if len(sys.argv) != 2:
        print("명령어 에러")
        sys.exit()

    command = sys.argv[1]
    return command

# 로직


def get_ip_incommand_logic():
    command = get_argv()
    output = get_output(command)
    return output


if __name__ == '__main__':
    print(get_ip_incommand_logic())
