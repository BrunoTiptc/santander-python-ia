# Desafio: Pedir ao usuário o caminho para um arquivo de texto e separar em palavras

def main():
    """
    Função principal que pede ao usuário o caminho para um arquivo de texto
    e separa o conteúdo em palavras
    """
    print("=== Leitor de Arquivo de Texto ===")
    
    # Pede o caminho do arquivo para o usuário
    caminho_arquivo = input("Digite o caminho para o arquivo de texto: ")
    
    try:
        # Tenta abrir e ler o arquivo
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            print(f"\nConteúdo do arquivo '{caminho_arquivo}':")
            print("-" * 50)
            print(conteudo)
            print("-" * 50)
            
            # Separa o conteúdo em palavras
            palavras = conteudo.split()
            print(f"\n�� Total de palavras: {len(palavras)}")
            print("\n🔤 Palavras encontradas:")
            print("-" * 30)
            
            for i, palavra in enumerate(palavras, 1):
                print(f"{i:3d}. {palavra}")
            
    except FileNotFoundError:
        print(f"❌ Erro: Arquivo '{caminho_arquivo}' não encontrado!")
    except PermissionError:
        print(f"❌ Erro: Sem permissão para ler o arquivo '{caminho_arquivo}'!")
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")

if __name__ == "__main__":
    main()