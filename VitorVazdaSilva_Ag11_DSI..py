from colorama import Fore, Style, init

init()

niveis = [
    "Muito baixo (crítico)",
    "Baixo",
    "Médio",
    "Alto",
    "Muito alto (alerta)"
]

cores = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE]

def mostrar_nivel(i):
    print(cores[i] + "Nível " + str(i+1) + " - " + niveis[i])

for i in range(len(niveis)):
    mostrar_nivel(i)

print(Style.RESET_ALL)