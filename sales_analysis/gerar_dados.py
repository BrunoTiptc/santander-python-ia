#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gerador de Dados de Vendas Sintéticos
Criado por Bruno com ajuda do Otimus (IA)
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

def gerar_dados_vendas(num_registros=200):
    """Gera dados de vendas sintéticos realistas"""
    
    # Produtos disponíveis
    produtos = [
        'Smartphone', 'Notebook', 'Tablet', 'Fone Bluetooth', 'Mouse Gamer',
        'Teclado Mecânico', 'Monitor 4K', 'SSD 1TB', 'Placa de Vídeo', 'Processador',
        'Memória RAM', 'Fonte 750W', 'Gabinete', 'Cooler CPU', 'Webcam HD',
        'Microfone USB', 'Caixa de Som', 'Cabo HDMI', 'Adaptador USB-C', 'Carregador'
    ]
    
    # Preços base para cada produto (em reais)
    precos_base = {
        'Smartphone': 1200.0, 'Notebook': 2500.0, 'Tablet': 800.0, 'Fone Bluetooth': 150.0,
        'Mouse Gamer': 80.0, 'Teclado Mecânico': 200.0, 'Monitor 4K': 1500.0, 'SSD 1TB': 300.0,
        'Placa de Vídeo': 2000.0, 'Processador': 800.0, 'Memória RAM': 200.0, 'Fonte 750W': 400.0,
        'Gabinete': 300.0, 'Cooler CPU': 150.0, 'Webcam HD': 250.0, 'Microfone USB': 180.0,
        'Caixa de Som': 120.0, 'Cabo HDMI': 25.0, 'Adaptador USB-C': 35.0, 'Carregador': 50.0
    }
    
    # Gera datas aleatórias nos últimos 6 meses
    data_inicio = datetime.now() - timedelta(days=180)
    data_fim = datetime.now()
    
    dados = []
    
    for i in range(num_registros):
        # Data aleatória
        data = data_inicio + timedelta(
            days=random.randint(0, (data_fim - data_inicio).days),
            hours=random.randint(9, 21),  # Horário comercial
            minutes=random.randint(0, 59)
        )
        
        # Produto aleatório
        produto = random.choice(produtos)
        
        # Quantidade (mais produtos baratos são vendidos em maior quantidade)
        preco_base = precos_base[produto]
        if preco_base < 100:
            quantidade = random.choices([1, 2, 3, 4, 5], weights=[40, 30, 20, 8, 2])[0]
        elif preco_base < 500:
            quantidade = random.choices([1, 2, 3, 4], weights=[60, 25, 12, 3])[0]
        else:
            quantidade = random.choices([1, 2, 3], weights=[80, 18, 2])[0]
        
        # Preço com variação de ±15%
        variacao_preco = random.uniform(0.85, 1.15)
        preco = round(preco_base * variacao_preco, 2)
        
        dados.append({
            'data': data.strftime('%Y-%m-%d'),
            'produto': produto,
            'quantidade': quantidade,
            'preco': preco
        })
    
    return pd.DataFrame(dados)

def main():
    """Função principal"""
    print("🎯 Gerando dados de vendas sintéticos...")
    print("Desenvolvido por Bruno com ajuda do Otimus! 🤖")
    
    # Gera dados
    df_vendas = gerar_dados_vendas(200)
    
    # Salva como CSV
    caminho_arquivo = 'vendas.csv'
    df_vendas.to_csv(caminho_arquivo, index=False, encoding='utf-8')
    
    print(f"✅ Dados gerados com sucesso!")
    print(f"📊 Total de registros: {len(df_vendas)}")
    print(f"📅 Período: {df_vendas['data'].min()} até {df_vendas['data'].max()}")
    print(f"🛍️ Produtos únicos: {df_vendas['produto'].nunique()}")
    print(f"💰 Receita total: R$ {df_vendas['quantidade'].multiply(df_vendas['preco']).sum():.2f}")
    print(f"📁 Arquivo salvo: {caminho_arquivo}")
    
    # Mostra amostra dos dados
    print(f"\n📋 Primeiras 10 linhas:")
    print(df_vendas.head(10))
    
    # Estatísticas por produto
    print(f"\n📈 Top 5 produtos por quantidade vendida:")
    top_produtos = df_vendas.groupby('produto')['quantidade'].sum().sort_values(ascending=False)
    print(top_produtos.head())
    
    print(f"\n✨ Dados prontos para análise! TMJ! 💪")

if __name__ == "__main__":
    main()
