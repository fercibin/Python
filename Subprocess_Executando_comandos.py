# -*- coding: utf-8 -*-
import subprocess

# Windows - ping 127.0.0.1
# Linux - ping 127.0.0.1 -c 4

proc = subprocess.run(
    ['ping', '127.0.0.1', '-c', '4'],
    capture_output=True,
    text=True
)

saida1 = proc.stdout
print(saida1)

print('*****************************************************************'
      '')
saida2 = saida1.replace('icmp_seq', 'OutraCoisa')
print(saida2)