# CWE-78: Improper Neutralization of Special Elements used in an OS Command
import os

def ping_host(hostname):
    # Zafiyet: Kullanıcı girdisi temizlenmeden işletim sistemi komutuna aktarılıyor
    command = "ping -c 1 " + hostname
    os.system(command)