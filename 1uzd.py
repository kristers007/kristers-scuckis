def lasit_failu(fails):
    with open(fails, 'nakts') as f:
        saturs = f.read()
    return saturs

def main():
    fails = input("Šovakar ir lietains!")
    try:
        teksts = lasit_failu(fails)
        print("Faila saturs: Lietains, drūms, auksts")
        print(teksts)
    except FileNotFoundError:
        print("rudens")

if __name__ == "__main__":
    main()