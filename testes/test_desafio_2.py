import pytest
import os
import sys

# Adiciona o diretório src ao path para importar o módulo
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

def test_contar_palavras():
    """Testa se o programa conta palavras corretamente"""
    # Texto de teste
    texto_teste = "Python é uma linguagem de programação incrível! Python é fácil de aprender e muito poderosa. Python é usada em ciência de dados, IA e web. Python, Python, Python - a linguagem do futuro!"
    
    # Separa em palavras
    palavras = texto_teste.split()
    
    # Verifica se conta corretamente
    assert len(palavras) == 33, f"Esperado 33 palavras, mas encontrou {len(palavras)}"
    
    # Verifica se contém palavras específicas
    assert "Python" in palavras
    assert "é" in palavras
    assert "linguagem" in palavras

def test_contar_frequencia():
    """Testa se conta a frequência das palavras corretamente"""
    from collections import Counter
    
    # Texto de teste
    texto_teste = "Python é uma linguagem de programação incrível! Python é fácil de aprender e muito poderosa. Python é usada em ciência de dados, IA e web. Python, Python, Python - a linguagem do futuro!"
    
    # Separa em palavras
    palavras = texto_teste.split()
    
    # Conta frequência
    contador = Counter(palavras)
    
    # Verifica se Python aparece 4 vezes
    assert contador["Python"] == 4, f"Esperado 4 ocorrências de 'Python', mas encontrou {contador['Python']}"
    
    # Verifica se 'é' aparece 3 vezes
    assert contador["é"] == 3, f"Esperado 3 ocorrências de 'é', mas encontrou {contador['é']}"

def test_arquivo_inexistente():
    """Testa se trata erro de arquivo não encontrado"""
    # Simula tentativa de abrir arquivo inexistente
    arquivo_inexistente = "arquivo_que_nao_existe.txt"
    
    # Verifica se o arquivo realmente não existe
    assert not os.path.exists(arquivo_inexistente), "Arquivo deveria não existir"

    # para rodar o teste:   pytest testes/test_desafio_2.py -v