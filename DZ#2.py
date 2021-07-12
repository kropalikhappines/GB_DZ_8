import re

regul_file = (r"([0-9.]+)")


def parse_logs():
    with open('nginx_logs.txt', 'r') as f:
        for line in f:
            regul_file = re.compile(r"([0-9.]+) .+\[(.+)] \"(.+) (/.+)\" (\d+) (\d+)")
            print(regul_file.findall(line))


parse_logs()