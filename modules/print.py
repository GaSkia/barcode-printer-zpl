import csv
import tempfile

# TODO: add windows function

labels = []

label_height = (2.8 / 2.54) * 203
label_length = (10 / 2.54) * 203
small = 'piccolo'
big = 'grande'

def unix(filepath: str, delimiter: str):
    import cups

    with open(filepath, newline='') as f:
        reader = csv.reader(f, delimiter=delimiter)
        for row in reader:
            labels.append(row)


    conn = cups.Connection()
    printers = conn.getPrinters()
    printer_names = list(printers.keys())
    number = 0
    for printer in printers:
        print(f'[{number}]', printer, printers[printer]["device-uri"])
        number = number + 1
    print('Seleziona stampante: ')
    choice = int(input())
    printer = printers[printer_names[choice]]["printer-info"]
    for label in labels:

        if len(label) > 1 :
            dim = str.lower(label[1]).strip()
            if dim == big:
                height = f"""
                    ^A0N, 120, 120^FD{label[0]}^FS
                    ^BCN,100,Y,N,N
                    ^FO20,160^A0N,0,0^FD{label[0]}^FS
                """
            else:
                height = f"""
                    ^A0N, 50, 50^FD{label[0]}^FS
                    ^BCN,100,Y,N,N
                    ^FO20,160^A0N,0,0^FD{label[0]}^FS
                """
                

        with tempfile.NamedTemporaryFile(delete=False,
                                         suffix=".txt", mode='w') as tmp:
            text = f"""
                    ^XA
                    ^LL{label_height}
                    ^PW{label_length}
                    ^FO320,90^BY2
                    ^XZ
                   """
            print('testo: ', text)
            print('stampante: ', printer)
            tmp.write(text)
            tmp_path = tmp.name
            print('file', tmp_path)
            tmp.flush()

        job_id = conn.printFile(printer, tmp_path, label[0], {})
        print(f"Stampando {label}. Job ID: {job_id}")
