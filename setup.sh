#!/bin/zsh

index=0

#setopt KSH_ARRAYS
typeset -a printers

printers=()
while IFS= read -r line; do
  uri=${line#* }        # Remove the word "direct"
  printers+=("$uri")
done <<< "$(lpinfo -v)"

# iterate through printers
for i in {0..${#printers[@]}}; do
    echo "$i $printers[i]"
done

# select let user select printer
echo "Selezionare dispositivo da aggiungere: "
read device

# Validate input 
if [[ $device -lt 1 || $device -gt ${#printers[@]} ]]; then
    echo "Numero non valido."
    exit 1
fi

printer="${printers[device]}"
printer_name=$(echo "$printer" | sed \
  -e 's|.*://||' \
  -e 's|%20|_|g' \
  -e 's|[^a-zA-Z0-9_]||g'
 )

lpadmin -p "$printer_name" -v "$printer" -E

echo "Stampante '$printer_name' aggiunta con successo."
