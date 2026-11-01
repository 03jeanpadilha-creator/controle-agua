from colorama import init, Fore

init(autoreset=True)

niveis = [
    ("Muito baixo (crítico)", Fore.RED),
    ("Baixo", Fore.YELLOW),
    ("Médio", Fore.GREEN),
    ("Alto", Fore.CYAN),
    ("Muito alto (alerta)", Fore.BLUE)
]

nivel_atual = int(input("Informe o nível do reservatório (1 a 5): "))

if 1 <= nivel_atual <= 5:
    situacao, cor = niveis[nivel_atual - 1]

    print("\n=== CONTROLE DE NÍVEL DE ÁGUA ===")
    print(f"Nível: {nivel_atual}")
    print(cor + f"Situação: {situacao}")

else:
    print(Fore.RED + "Nível inválido! Digite um valor de 1 a 5.")