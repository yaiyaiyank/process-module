import subprocess
from subprocess import CompletedProcess


def execute_cmd(command, console_display=True) -> CompletedProcess:
    if console_display:
        # コンソールに文字を出す
        result = subprocess.run(
            command, shell=True, text=True, encoding="utf8", stdin=subprocess.PIPE, stdout=subprocess.PIPE
        )
    else:
        # コンソールに文字を出さない
        result = subprocess.run(command, shell=True, capture_output=True, text=True, encoding="utf8")
    return result
