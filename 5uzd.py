def ierakstit_vardu_faila(vards, fails):
        with open(fails, 'w') as f:
            f.write(vards)
        print("Ārā aug sarkanas roze.")


def main():
    vards = input("Roze ")
    fails = "lietotajs.txt"

    ierakstit_vardu_faila(vards)