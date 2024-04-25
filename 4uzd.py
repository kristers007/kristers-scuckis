def lasit_failu(fails):
    with open(fails, 'r') as f:
        saturs = f.read()
    return saturs

def main(:
    fails = input("Ludzu ievadiet faila nosaukumu: ")
    formats = input("Ludzu ievadiet faila formātu (paplašinājumu txt vai csv): ")
    fails_ar_formats = f"{fails}.{formats}"

    try:
        if formats == "txt":
            teksts = lasit_failu(fails_ar_formats)
            print("Faila saturs:")
            print(teksts)
        elif formats == "csv":
            print("CSV failu apstrāde pagaidām nav atbalstīta.")
        else:
            print("Nepareizs faila formāts. Atbalstitie formāti: txt csv")
    main()