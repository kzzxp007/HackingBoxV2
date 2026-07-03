import os
import pyfiglet
from colorama import Fore, init
import random

init(autoreset=True)

def menu_main():
    print(Fore.BLUE + pyfiglet.figlet_format("HackingBox", font="slant"))
    print(Fore.BLUE + "Bem-Vindo a HackingBox - V5")
    print(Fore.BLUE + 'Escreva "help" para ajuda')

def menu_help():
    print("\n=====OPÇÕES=====\n")
    print("1. DDoS")
    print("2. OSINT")
    print("3. NMAP")
    print("4. Malware")
    print("5. Exploração de vuln")
    print("6. Phishing")
    print("==========")

    rehelp = input("Selecione a sua opção: ")

    if rehelp == "1":
        print("=====DDoS=====")
        print("1. NAMI-DDoS")
        print("2. DDoS Slayer")
        print("3. HULK")
        print("4. Mais de 60 DDoS")

        respddos = input("Selecione sua opção:  ")
        if respddos == "1":
            print("=====DDoS=====")
            print("git clone https://github.com/cutipu/NAMI")
            print("cd NAMI")
            print("python ddos.py")
        elif respddos == "2":
            print("=====DDoS=====")
            print("git clone https://github.com/blackhatethicalhacking/DDoSlayer")
            print("cd DDoSlayer")
            print("python DDoSlayer.py")
        elif respddos == "3":
            print("=====DDoS=====")
            print("git clone https://github.com/R3DHULK/HULK")
            print("cd HULK")
            print("pip install -r requirements.txt")
            print("python hulk.py")
        elif respddos == "4":
            print("=====DDoS=====")
            print("60 Tools de DDoS neste site:")
            print("https://github.com/lucthienphong1120/full-60-ddos-tools")
        else:
            print("Opção não encontrada")

    elif rehelp == "2":
        print("=====OSINT=====")
        print("1. Whois")
        print("2. theHarvester")
        print("3. Sherlock")
        print("4. Amass")
        resposint = input("Selecione sua opção:  ")
        if resposint == "1":
            print("pkg update && pkg upgrade -y")
            print("pkg install whois -y")
        elif resposint == "2":
            print("pkg update && pkg upgrade -y")
            print("git clone https://github.com/laramies/theHarvester.git")
            print("cd theHarvester")
            print("pip install -r requirements/base.txt")
            print("python3 theHarvester.py")
        elif resposint == "3":
            print("pkg update && pkg upgrade -y")
            print("git clone https://github.com/sherlock-project/sherlock.git")
            print("cd sherlock")
            print("pip install -r requirements.txt")
            print("Para usar:")
            print("python3 sherlock.py nome_de_usuario")
        elif resposint == "4":
            print("pkg update && pkg upgrade -y")
            print("pkg install amass")
            print(Fore.RED + "Caso der algum erro, ou o pacote não existir:")
            print("pkg install git golang -y")
            print("go install github.com/owasp-amass/amass/v4/...@master")
            print("echo 'export PATH=$PATH:$HOME/go/bin' >> ~/.bashrc")
            print("source ~/.bashrc")
            print("amass -h")
            print(Fore.RED + "Se instalou via Go:")
            print("~/go/bin/amass -h")
        else:
            print("Opção não encontrada")

    elif rehelp == "3":
        print("=====NMAP=====")
        print("pkg install nmap")

    elif rehelp == "4":
        print("=====Malware=====")
        print("1. CraxsRAT (Data pra lançamento: 20 de julho)")
        print("2. Malware-Exhibit")
        print("3. The-MALWARE-Repo")
        print("4. Metaploit Framework")
        respomalware = input("Insira sua opção:  ")
        if respomalware == "1":
            print("Data de lançamento: 20 de julho!!!")
        elif respomalware == "2":
            print("Entre no site:")
            print("https://github.com/alvin-tosh/Malware-Exhibit")
        elif respomalware == "3":
            print("Entre no site:")
            print("https://github.com/Da2dalus/The-MALWARE-Repo")
        elif respomalware == "4":
            print("pkg update && pkg upgrade -y")
            print("pkg install wget curl git -y")
            print("wget https://raw.githubusercontent.com/gushmazuko/metasploit_in_termux/main/metasploit.sh")
            print("chmod +x metasploit.sh")
            print("./metasploit.sh")
            print("Quando a instalação acabar:")
            print("msfconsole")
            print("Se aparecer erro de banco de dados, inicialize-o com:")
            print("msfdb init")
        else:
            print("Opção não encontrada")

    elif rehelp == "5":
        print("=====Exploração de vuln=====")
        print("1. SQLMap")
        print("2. Nuclei")
        print("3. Nikto")
        print("4. XSStrike")
        print("5. wpscan")
        print("6. Subfinder")
        respovuln = input("Selecione sua opção:  ")
        if respovuln == "1":
            print("git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git")
            print("cd sqlmap")
            print("python sqlmap.py --version")
        elif respovuln == "2":
            print("pkg install golang git")
            print("go install github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest")
            print("echo 'export PATH=$PATH:$HOME/go/bin' >> ~/.bashrc")
            print("source ~/.bashrc")
            print("nuclei -version")
            print("nuclei -update-templates")
        elif respovuln == "3":
            print("pkg install git perl")
            print("git clone https://github.com/sullo/nikto.git")
            print("cd nikto/program")
            print("perl nikto.pl -Version")
            print("perl nikto.pl -h")
        elif respovuln == "4":
            print("git clone https://github.com/s0md3v/XSStrike.git")
            print("cd XSStrike")
            print("pip install -r requirements.txt")
            print("python xsstrike.py -h")
        elif respovuln == "5":
            print("pkg install ruby git")
            print("gem update --system")
            print("gem install wpscan")
            print("wpscan --help")
        elif respovuln == "6":
            print("pkg install golang git")
            print("go install github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest")
            print("echo 'export PATH=$PATH:$HOME/go/bin' >> ~/.bashrc")
            print("source ~/.bashrc")
            print("subfinder -h")
        else:
            print("Opção não encontrada")

    elif rehelp == "6":
        print("=====Phishing=====")
        print("1. ZPhisher")
        print("2. MaskPhish")
        print("3. Cloudflared")
        respophi = input("Insira sua opção:  ")
        if respophi == "1":
            print("git clone --depth=1 https://github.com/htr-tech/zphisher.git")
            print("cd zphisher")
            print("bash zphisher.sh")
        elif respophi == "2":
            print("git clone https://github.com/jaykali/maskphish")
            print("cd maskphish")
            print("bash maskphish.sh")
        elif respophi == "3":
            print("apt install php")
            print("git clone https://github.com/XPH4N70M/HACK-CAMERA.git")
            print("cd HACK-CAMERA")
            print("chmod +x hack_camera.sh")
            print("bash setup")
            print("bash hack_camera.sh")
        else:
            print("Opção não encontrada")

def main():
    menu_main()

    while True:
        resp = input(Fore.GREEN + "root@user > ")

        if resp.lower() == "help":
            menu_help()
        elif resp.lower() == "tabelas":
            menu_help()
        elif resp.lower() == "game":
            while True:
                print(Fore.CYAN + "\n=== Acerte o Número ===")
                print("Digite um número de 1 a 10.")
                print("Digite 'sair' para voltar ao menu.")

                numero = random.randint(1, 10)
                resposta = input("Número: ")

                if resposta.lower() == "sair":
                    break

                if not resposta.isdigit():
                    print(Fore.RED + "Digite apenas números!")
                    continue

                resposta = int(resposta)

                if resposta == numero:
                    print(Fore.GREEN + f"Você acertou! O número era {numero}.\n")
                else:
                    print(Fore.RED + f"Você errou! O número era {numero}.\n")
        elif resp.lower() == "about":
            print(Fore.CYAN + """
        ╔══════════════════════════════════════════════════════╗
        ║                  HACKINGBOX V5                      ║
        ╠══════════════════════════════════════════════════════╣
        ║ Criador    : kalizzx                                ║
        ║ Linguagem  : Python                                 ║
        ║ Interface  : Command Line (CLI)                     ║
        ║ Plataforma : Termux                                 ║
        ║ Versão     : 5.0                                    ║
        ║ Build      : 2026.07                                ║
        ║ Status     : Ativa                                  ║
        ║ Licença    : MIT                                    ║
        ╠══════════════════════════════════════════════════════╣
        ║ Módulos Disponíveis                                 ║
        ║ • OSINT                                             ║
        ║ • NMAP                                              ║
        ║ • Malware                                           ║
        ║ • Exploração de Vulnerabilidades                    ║
        ║ • Phishing                                          ║
        ║ • Games                                             ║
        ║ • About                                             ║
        ╠══════════════════════════════════════════════════════╣
        ║ Objetivo:                                           ║
        ║ Reunir ferramentas, utilitários e recursos          ║
        ║ em uma interface simples, rápida e organizada.      ║
        ╠══════════════════════════════════════════════════════╣
        ║ GitHub : Em breve                                   ║
        ║ Discord: Em breve                                   ║
        ╠══════════════════════════════════════════════════════╣
        ║             "Knowledge is Power."                   ║
        ╚══════════════════════════════════════════════════════╝
        """)
        elif resp.lower() == "system":
            os.system("fastfetch")
        elif resp.lower() == "tor":
            os.system("tor &")

        elif resp.lower() == "exit":
            break

main()
