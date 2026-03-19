# tp1_p1_main.py
from tripulante import Tripulante
from navio import Navio
from colorama import init, Fore, Style
from tp1_p2_main import Simulacao
from capitao import Capitao
from espadachim import Espadachim
from navegador import Navegador
from medico import Medico
from cozinheiro import Cozinheiro

init(autoreset=True)

def main():
    print(Fore.CYAN + Style.BRIGHT + "\n" + "="*65)
    print(Fore.YELLOW + Style.BRIGHT + " 🏴‍☠️   BEM-VINDO À GRANDE ERA DOS PIRATAS! 🏴‍☠️")
    print(Fore.CYAN + Style.BRIGHT + "="*65)
    
    nome_do_barco = input(Fore.YELLOW + "⚓ Capitão, qual é o nome deste grande navio?: ")
    
    meu_barco = Navio(nome_do_barco)
    
    print(Fore.GREEN + f"\n{meu_barco.nome} é um nome digno de navegar na Grand Line! Vamos zarpar.")
    print(Fore.CYAN + "-"*65)
    
    luffy = Capitao("Monkey D. Luffy", recompensa=1500000000.0, poder=100, fruta="Gomu Gomu no Mi", energia=100)
    zoro = Espadachim("Roronoa Zoro", recompensa=320000000.0, poder=95, fruta="Nenhuma", energia=100, espadas=["Wado Ichimonji", "Enma", "Sandai Kitetsu"])
    
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
        print(Fore.GREEN + "9. 🚢 Zarpar para a Aventura na Grand Line!")
        
        opcao = input(Fore.YELLOW + "👉 Escolhe uma opção (1-9): ")
        
        if opcao == "1":
            print(Fore.CYAN + "\n--- NOVO RECRUTA ---")
            nome = input("Nome: ")
            funcao = input("Função (ex: Navegadora): ")
            fruta = input("Fruta (ou 'Nenhuma'): ")
            
            try:
                recompensa = float(input("Recompensa (Bounty): "))
                poder = int(input("Poder de Combate (0-100): "))
                energia = int(input("Energia (0-100): "))
                
                funcao= funcao.strip().lower()

                if funcao in {"capitao", "capitão"}:
                    novo_pirata = Capitao(nome, recompensa=recompensa, poder=poder, fruta=fruta, energia=energia)
                elif funcao in {"espadachim", "espadachin", "espadachim(a)"}:
                    novo_pirata = Espadachim(nome, recompensa=recompensa, poder=poder, fruta=fruta, energia=energia)
                elif funcao in {"navegador", "navegadora"}:
                    novo_pirata = Navegador(nome, recompensa=recompensa, poder=poder, fruta=fruta, energia=energia)
                elif funcao in {"medico", "médico", "medica", "médica"}:
                    novo_pirata = Medico(nome, recompensa=recompensa, poder=poder, fruta=fruta, energia=energia)
                elif funcao in {"cozinheiro", "cozinheira"}:
                    novo_pirata = Cozinheiro(nome, recompensa=recompensa, poder=poder, fruta=fruta, energia=energia)
                else:
                    print(Fore.YELLOW + "Função não reconhecida. Será criado como Tripulante base.")
                    novo_pirata = Tripulante(
                        nome,
                        recompensa=recompensa,
                        poder=poder,
                        fruta=fruta,
                        energia=energia,
                    )
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
        
        elif opcao == "9":
            if not meu_barco.tripulacao:
                print(Fore.RED + "❌ Não podes zarpar sem tripulação!")
                continue
            
            import pygame
            
            pygame.mixer.init()
            pygame.mixer.music.load("ost.mp3")
            
            pygame.mixer.music.set_volume(0.1) 
            
            print(Fore.CYAN + "\n🎶 A tocar: Tema da Grand Line (10% volume)...")
            pygame.mixer.music.play(-1)
            
            # Inicia a simulação da parte 2
            simulador = Simulacao(meu_barco)
            simulador.jogar()
            
            # Parar musica quando acabar a simulação
            pygame.mixer.music.stop()
            print(Fore.GREEN + "\n⚓ Regressaste ao porto seguro.")
        else:
            print(Fore.RED + "\n❌ Opção inválida! Escreve apenas um número de 1 a 9.")

if __name__ == "__main__":
    main()