import platform
import sys
import subprocess
from modules.print import unix

subprocess.run(["source ./.venv/bin/activate"])

print("Ciao, inserire il percorso completo del file. " +
      "Non deve contenere spazi: ")

filepath = input()

print("Indicare il carattere usato come delimitatore: ")
delimiter = input()

if len(delimiter) != 1:
    sys.exit("Il delimitatore deve essere composto da un carattere solo.")


if platform.system() == "Windows":
    print("Non ancora implementato.")

elif platform.system() in ("Linux", "Darwin"):
    print("INFO: executing on unix platform")
    unix(filepath=filepath, delimiter=delimiter)


else:
    sys.exit("Piattaforma non supportata.")
