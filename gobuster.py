import subprocess, os

def dirscan(url):
    try:
        os.mkdir("GoBuster")
    except Exception:
        pass

    command = "gobuster dir -u " + url + " -w /usr/share/dirb/wordlists/small.txt -o ../toolkit/GoBuster/results.txt"
    subprocess.run(command, shell=True, universal_newlines=True)
    print("\nEscaneo de directorios de: " + url + " completado.")