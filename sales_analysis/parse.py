#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Análise de Vendas - Projeto Sales Analysis
Desenvolvido por Bruno com ajuda do Otimus (IA)
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import os

def carregar_dados(caminho_arquivo):
    """
    # 1. Carregar dados CSV
    Carrega os dados de vendas do arquivo CSV
    """
    try:
        # Carrega CSV especificando parse_dates para a coluna data
        df = pd.read_csv(caminho_arquivo, parse_dates=['data'])
        
        print(f"✅ Dados carregados com sucesso!")
        print(f"📊 Shape: {df.shape}")
        print(f"📋 Colunas: {list(df.columns)}")
        print(f"📅 Período: {df['data'].min().strftime('%Y-%m-%d')} até {df['data'].max().strftime('%Y-%m-%d')}")
        
        # Verifica os tipos de dados
        print(f"\n🔍 Tipos de dados:")
        print(df.dtypes)
        
        # Verifica se quantidade e preço são numéricos
        if df['quantidade'].dtype in ['int64', 'float64'] and df['preco'].dtype in ['int64', 'float64']:
            print(f"✅ Colunas 'quantidade' e 'preco' são numéricas!")
        else:
            print(f"⚠️ Convertendo colunas para numérico...")
            df['quantidade'] = pd.to_numeric(df['quantidade'])
            df['preco'] = pd.to_numeric(df['preco'])
        
        return df
    except FileNotFoundError:
        print(f"❌ Arquivo não encontrado: {caminho_arquivo}")
        return None
    except Exception as e:
        print(f"❌ Erro ao carregar dados: {e}")
        return None

def calcular_vendas_por_mes(df):
    """
    # 2. Calcular o total de vendas por mês
    Calcula receita total e quantidade vendida por mês
    """
    print(f"\n📈 === TOTAL DE VENDAS POR MÊS ===")
    
    # Cria coluna de mês usando to_period('M')
    df['mes'] = df['data'].dt.to_period('M')
    
    # Agrupa por mês e calcula vendas (quantidade * preço)
    vendas_por_mes = df.groupby('mes').apply(lambda d: (d['quantidade'] * d['preco']).sum(), include_groups=False)
    
    # Converte para tipo index
    vendas_por_mes = vendas_por_mes.reset_index()
    
    print("Vendas por mês:")
    print(vendas_por_mes)
    
    # Estatísticas resumidas
    receita_total = vendas_por_mes[0].sum()  # Coluna 0 contém os valores
    mes_maior_venda = vendas_por_mes.loc[vendas_por_mes[0].idxmax(), 'mes']
    maior_receita = vendas_por_mes[0].max()
    
    print(f"\n💰 Receita total do período: R$ {receita_total:,.2f}")
    print(f"🏆 Mês com maior receita: {mes_maior_venda} (R$ {maior_receita:,.2f})")
    
    # Retorna a série para compatibilidade com gráficos
    vendas_serie = vendas_por_mes.set_index('mes')[0]
    return vendas_serie

def analisar_produtos(df):
    """
    # 3. Determinar o produto mais vendido e de maior receita
    Analisa produtos por quantidade e receita
    """
    print(f"\n🛍️ === ANÁLISE DE PRODUTOS ===")
    
    # Calcula a receita primeiro
    df['receita'] = df['quantidade'] * df['preco']
    
    # Agrupa por produto e calcula quantidade e receita
    vendas_por_produto = df.groupby('produto').agg({
        'quantidade': 'sum',
        'receita': 'sum'
    })
    
    print("📊 Vendas por produto:")
    print(vendas_por_produto)
    
    # Encontra o produto mais vendido em quantidade
    mais_vendido = vendas_por_produto['quantidade'].idxmax()
    
    # Encontra o produto com maior receita
    maior_receita = vendas_por_produto['receita'].idxmax()
    
    print(f"\n🏆 RESULTADOS:")
    print(f"Produto mais vendido em unidades: {mais_vendido} (total {vendas_por_produto.loc[mais_vendido, 'quantidade']})")
    print(f"Produto com maior receita: {maior_receita} (total R$ {vendas_por_produto.loc[maior_receita, 'receita']:.2f})")
    
    # Mostra top 5 para cada critério
    print(f"\n📊 TOP 5 PRODUTOS POR QUANTIDADE VENDIDA:")
    top_quantidade = vendas_por_produto.sort_values('quantidade', ascending=False).head()
    for i, (produto, row) in enumerate(top_quantidade.iterrows(), 1):
        print(f"   {i}. {produto}: {row['quantidade']} unidades")
    
    print(f"\n💰 TOP 5 PRODUTOS POR RECEITA:")
    top_receita = vendas_por_produto.sort_values('receita', ascending=False).head()
    for i, (produto, row) in enumerate(top_receita.iterrows(), 1):
        print(f"   {i}. {produto}: R$ {row['receita']:,.2f}")
    
    return vendas_por_produto

def grafico_vendas_por_mes(vendas_por_mes):
    """
    # 4. Gráfico de vendas por mês
    Cria visualização das vendas mensais
    """
    print(f"\n📊 Gerando gráfico de vendas por mês...")
    
    # Se vendas_por_mes for o índice Periodo, converte para str para melhor manuseio
    vendas_por_mes.index = vendas_por_mes.index.astype(str)
    
    plt.figure(figsize=(6, 4))
    
    # Usa o método plot da Series
    vendas_por_mes.plot(kind='bar')
    
    plt.title("Vendas por mês")
    plt.xlabel("Mês")
    plt.ylabel("Vendas (R$)")
    plt.tight_layout()
    
    # Salva o gráfico em PNG
    plt.savefig("vendas_por_mes.png")
    print("📁 Gráfico salvo como: vendas_por_mes.png")
    
    plt.show()

def grafico_top_produtos(vendas_por_produto):
    """
    # 5. Gráfico dos 5 principais produtos por receita
    Cria visualização dos produtos com maior receita
    """
    print(f"\n📊 Gerando gráfico dos top 5 produtos...")
    
    # Pega os 5 produtos com maior receita usando nlargest
    top5 = vendas_por_produto.nlargest(5, 'receita')
    
    plt.figure(figsize=(6, 4))
    
    # Usa plt.bar manual
    plt.bar(top5.index, top5['receita'])
    
    plt.title("Os 5 principais produtos por receita")
    plt.ylabel("Receita (R$)")
    plt.xlabel("Produto")
    
    # Rotaciona os rótulos dos produtos para melhor visualização
    plt.xticks(rotation=45)
    
    plt.tight_layout()
    
    # Salva o gráfico em PNG
    plt.savefig("top5_produtos.png")
    print("📁 Gráfico salvo como: top5_produtos.png")
    
    plt.show()

def main():
    """
    Função principal que executa toda a análise
    """
    print("🎉 === ANÁLISE DE VENDAS - SALES ANALYSIS ===")
    print("Desenvolvido por Bruno com ajuda do Otimus! 🤖")
    print("=" * 50)
    
    # Caminho do arquivo
    caminho_arquivo = 'vendas.csv'
    
    # 1. Carregar dados
    df = carregar_dados(caminho_arquivo)
    if df is None:
        return
    
    # Mostra amostra dos dados
    print(f"\n📋 Primeiras 5 linhas dos dados:")
    print(df.head())
    
    # 2. Calcular vendas por mês
    vendas_por_mes = calcular_vendas_por_mes(df)
    
    # 3. Analisar produtos
    vendas_por_produto = analisar_produtos(df)
    
    # 4. Gráfico de vendas por mês
    grafico_vendas_por_mes(vendas_por_mes)
    
    # 5. Gráfico dos top 5 produtos
    grafico_top_produtos(vendas_por_produto)
    
    print(f"\n✨ Análise concluída com sucesso! TMJ! 💪")
    print(f"📊 Dados analisados: {len(df)} transações")
    print(f"💰 Receita total: R$ {df['receita'].sum():,.2f}")
    print(f"🛍️ Produtos únicos: {df['produto'].nunique()}")

if __name__ == "__main__":
    main()
