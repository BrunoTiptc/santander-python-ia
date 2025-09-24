#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Calculator.py - Calculadora Interativa
Desenvolvido por Bruno com ajuda do Otimus (IA)
"""

def adicao(a, b):
    """Realiza adição de dois números"""
    return a + b

def subtracao(a, b):
    """Realiza subtração de dois números"""
    return a - b

def multiplicacao(a, b):
    """Realiza multiplicação de dois números"""
    return a * b

def divisao(a, b):
    """Realiza divisão de dois números com tratamento de divisão por zero"""
    if b == 0:
        raise ValueError("Erro: Divisão por zero não é permitida!")
    return a / b

def obter_numero(mensagem):
    """Solicita e valida entrada numérica do usuário"""
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("❌ Por favor, digite um número válido!")

def exibir_menu():
    """Exibe o menu de operações disponíveis"""
    print("\n" + "="*50)
    print("🧮 CALCULADORA OTIMUS 🧮")
    print("="*50)
    print("Operações disponíveis:")
    print("➕ Adição")
    print("➖ Subtração") 
    print("✖️  Multiplicação")
    print("➗ Divisão")
    print("🚪 Sair")
    print("="*50)

def main():
    """Função principal da calculadora"""
    print("🎉 Bem-vindo à Calculadora Otimus!")
    print("Desenvolvida por Bruno com ajuda da IA! 🤖")
    
    # Dicionário de operações para facilitar o código
    operacoes = {
        'adição': adicao,
        'adicao': adicao,
        'soma': adicao,
        '+': adicao,
        'subtração': subtracao,
        'subtracao': subtracao,
        'menos': subtracao,
        '-': subtracao,
        'multiplicação': multiplicacao,
        'multiplicacao': multiplicacao,
        'vezes': multiplicacao,
        '*': multiplicacao,
        'divisão': divisao,
        'divisao': divisao,
        'dividir': divisao,
        '/': divisao
    }
    
    while True:
        exibir_menu()
        
        # Solicita operação
        operacao = input("\nDigite a operação desejada: ").lower().strip()
        
        # Verifica se quer sair
        if operacao in ['saída', 'saida', 'sair', 'exit', 'quit', 'q']:
            print("\n👋 Obrigado por usar a Calculadora Otimus!")
            print("Até a próxima, Bruno! TMJ! ✨")
            break
        
        # Verifica se a operação é válida
        if operacao not in operacoes:
            print("❌ Operação inválida! Tente novamente.")
            continue
        
        try:
            # Solicita os números
            print(f"\n📊 Operação: {operacao.upper()}")
            num1 = obter_numero("Digite o primeiro número: ")
            num2 = obter_numero("Digite o segundo número: ")
            
            # Executa a operação
            resultado = operacoes[operacao](num1, num2)
            
            # Exibe o resultado
            print(f"\n🎯 Resultado: {num1} {operacao} {num2} = {resultado}")
            
        except ValueError as e:
            print(f"❌ {e}")
        except Exception as e:
            print(f"❌ Erro inesperado: {e}")
        
        # Pausa antes de continuar
        input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    main()
