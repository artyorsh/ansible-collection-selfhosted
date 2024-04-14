import sys
import subprocess

def main():
    message = sys.argv[1]
    status = sys.argv[2]

    subprocess.run(['/etc/notify.sh', message, status])

main()