#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Análise de Dados - Mini Projeto
Desenvolvido por Bruno com ajuda do Otimus (IA)
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

def carregar_dados(caminho_arquivo):
    """Carrega dados do CSV"""
    try:
        df = pd.read_csv(caminho_arquivo)
        print(f"✅ Dados carregados com sucesso!")
        print(f"📊 Shape: {df.shape}")
        print(f"📋 Colunas: {list(df.columns)}")
        return df
    except FileNotFoundError:
        print(f"❌ Arquivo não encontrado: {caminho_arquivo}")
        return None
    except Exception as e:
        print(f"❌ Erro ao carregar dados: {e}")
        return None

def calcular_estatisticas(df, coluna):
    """Calcula estatísticas básicas para uma coluna"""
    print(f"\n📈 Estatísticas para {coluna}:")
    print(f"   Média: {df[coluna].mean():.2f}")
    print(f"   Mediana: {df[coluna].median():.2f}")
    print(f"   Desvio Padrão: {df[coluna].std():.2f}")
    print(f"   Mínimo: {df[coluna].min():.2f}")
    print(f"   Máximo: {df[coluna].max():.2f}")
    print(f"   Contagem: {df[coluna].count()}")

def gerar_grafico_dispersao(df, coluna_x, coluna_y):
    """Gera gráfico de dispersão"""
    plt.figure(figsize=(10, 6))
    plt.scatter(df[coluna_x], df[coluna_y], alpha=0.7, s=100, c='blue', edgecolors='black')
    plt.xlabel(coluna_x.title())
    plt.ylabel(coluna_y.title())
    plt.title(f'Gráfico de Dispersão: {coluna_x.title()} vs {coluna_y.title()}')
    plt.grid(True, alpha=0.3)
    
    # Adiciona linha de tendência
    z = np.polyfit(df[coluna_x], df[coluna_y], 1)
    p = np.poly1d(z)
    plt.plot(df[coluna_x], p(df[coluna_x]), "r--", alpha=0.8, linewidth=2)
    
    plt.tight_layout()
    plt.show()

def gerar_grafico_histograma(df, coluna):
    """Gera histograma para uma coluna"""
    plt.figure(figsize=(10, 6))
    plt.hist(df[coluna], bins=10, alpha=0.7, color='skyblue', edgecolor='black')
    plt.xlabel(coluna.title())
    plt.ylabel('Frequência')
    plt.title(f'Histograma: {coluna.title()}')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

def main():
    """Função principal"""
    print("🎉 Bem-vindo à Análise de Dados Otimus!")
    print("Desenvolvida por Bruno com ajuda da IA! 🤖")
    
    # Caminho do arquivo
    caminho_arquivo = os.path.join('data', 'dados_exemplo.csv')
    
    # Carrega dados
    df = carregar_dados(caminho_arquivo)
    if df is None:
        return
    
    # Mostra primeiras linhas
    print(f"\n📋 Primeiras 5 linhas:")
    print(df.head())
    
    # Calcula estatísticas para cada coluna numérica
    colunas_numericas = df.select_dtypes(include=[np.number]).columns
    for coluna in colunas_numericas:
        calcular_estatisticas(df, coluna)
    
    # Gera gráficos
    if len(colunas_numericas) >= 2:
        print(f"\n📊 Gerando gráfico de dispersão...")
        gerar_grafico_dispersao(df, colunas_numericas[0], colunas_numericas[1])
        
        print(f"\n📊 Gerando histogramas...")
        for coluna in colunas_numericas:
            gerar_grafico_histograma(df, coluna)
    
    # Análise de correlação
    if len(colunas_numericas) >= 2:
        correlacao = df[colunas_numericas[0]].corr(df[colunas_numericas[1]])
        print(f"\n🔗 Correlação entre {colunas_numericas[0]} e {colunas_numericas[1]}: {correlacao:.3f}")
    
    print(f"\n✨ Análise concluída! TMJ! 💪")

if __name__ == "__main__":
    main()
