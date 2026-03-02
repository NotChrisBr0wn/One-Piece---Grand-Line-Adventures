# tp1_p1_main.py
from tripulante import Tripulante
from navio import Navio
from colorama import init, Fore, Style

init(autoreset=True)

def main():
    print(Fore.CYAN + Style.BRIGHT + "\n" + "="*65)
    print(Fore.YELLOW + Style.BRIGHT + " 🏴‍☠️   BEM-VINDO À GRANDE ERA DOS PIRATAS! 🏴‍☠️")
    print(Fore.CYAN + Style.BRIGHT + "="*65)
    
    nome_do_barco = input(Fore.YELLOW + "⚓ Capitão, qual é o nome deste grande navio?: ")
    
    meu_barco = Navio(nome_do_barco)
    
    print(Fore.GREEN + f"\n{meu_barco.nome} é um nomme digno de navegar na Grand Line! Vamos zarpar.")
    print(Fore.CYAN + "-"*65)
    
    luffy = Tripulante("Monkey D. Luffy", "Capitão", "Gomu Gomu no Mi", 1500000000.0, 100, 100)
    zoro = Tripulante("Roronoa Zoro", "Espadachim", "Nenhuma", 320000000.0, 95, 100)
    
    meu_barco.recrutar(luffy)
    meu_barco.recrutar(zoro)

    while True:
        print(Fore.CYAN + Style.BRIGHT + "\n" + "="*45)
        print(Fore.YELLOW + Style.BRIGHT + "   🌊 GESTÃO DO NAVIO ONE PIECE 🌊")
        print(Fore.CYAN + Style.BRIGHT + "="*45)
        print("1. ⚓ Recrutar novo Tripulante")
        print("2. 👞 Expulsar Tripulante")
        print("3. 📜 Mostrar Manifesto do Navio")
        print("4. ⚔️ Mostrar Poder Total da Tripulação")
        print("5. ✨ Ordenar Tripulação (Por Poder/Bounty)")
        print("6. 💾 Guardar Jogo")
        print("7. 📂 Carregar Jogo")
        print(Fore.RED + "8. ❌ Sair")
        
        opcao = input(Fore.YELLOW + "👉 Escolhe uma opção (1-8): ")
        
        if opcao == "1":
            print(Fore.CYAN + "\n--- NOVO RECRUTA ---")
            nome = input("Nome: ")
            funcao = input("Função (ex: Navegadora): ")
            fruta = input("Fruta (ou 'Nenhuma'): ")
            
            try:
                recompensa = float(input("Recompensa (Bounty): "))
                poder = int(input("Poder de Combate (0-100): "))
                energia = int(input("Energia (0-100): "))
                
                novo_pirata = Tripulante(nome, funcao, fruta, recompensa, poder, energia)
                meu_barco.recrutar(novo_pirata)
                
            except ValueError as erro:
                print(Fore.RED + f"\n❌ ERRO: Dados inválidos! {erro}")
                print(Fore.YELLOW + "Recrutamento cancelado. Volta a tentar.")
                
        elif opcao == "2":
            print(Fore.CYAN + "\n--- EXPULSÃO ---")
            nome_expulsar = input("Qual o nome do pirata a expulsar? ")
            meu_barco.expulsar(nome_expulsar)
            
        elif opcao == "3":
            meu_barco.mostrar_manifesto()
            
        elif opcao == "4":
            poder_total = meu_barco.calcular_poder_total()
            print(Fore.MAGENTA + Style.BRIGHT + f"\n⚔️ O Poder de Combate Total da frota é: {poder_total}")
            
        elif opcao == "5":
            meu_barco.ordenar_tripulacao()
            input(Fore.YELLOW + "Pressiona Enter para ver o manifesto atualizado...")
        
        elif opcao == "6":
            meu_barco.guardar_jogo()
            input(Fore.GREEN + "💾 Jogo guardado com sucesso! Pressione ENTER para voltar ao menu... ")
            
        elif opcao == "7":
            meu_barco.carregar_jogo()
            input(Fore.GREEN + "📂 Jogo carregado com sucesso! Pressione ENTER para voltar ao menu... ")
            
        elif opcao == "8":
            print(Fore.GREEN + "\n⚓ A levantar âncora! Jogo terminado.")
            break
            
        else:
            print(Fore.RED + "\n❌ Opção inválida! Escreve apenas um número de 1 a 6.")

if __name__ == "__main__":
    main()