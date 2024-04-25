def lasit_rindas(fails):
    ar_failu = open(fails, 'r')
    rindas = ar_failu.readlines()
    ar_failu.close()
    return rindas

def main():
    try:
        rindas = lasit_rindas(fails)
        tresa_rinda = rindas[2] if len(rindas) > 2 else "Nav tresās rindas"
        otra_rinda = rindas[3] if len(rindas) > 3 else "Nav otrās rindas"

        print("Trešās rindas saturs:", tresa_rinda)
        print("Otrās rindas saturs:", otra_rinda)
    except FileNotFoundError:
        print("Faila nav atrasts.")

if __name__ == "__main__":
    main()