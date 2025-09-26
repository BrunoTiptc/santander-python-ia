# 📊 Sales Analysis - Análise de Vendas

> **Projeto de análise de dados desenvolvido por Bruno com ajuda do Otimus (IA)**  
> *Curso Santander Python IA - Bootcamp de Ciência de Dados*

---

## 🎯 **Sobre o Projeto**

Este projeto demonstra uma análise completa de dados de vendas utilizando **Python**, **Pandas** e **Matplotlib**. O objetivo é analisar dados de vendas de uma loja para obter insights sobre performance mensal e produtos mais vendidos.

### ✨ **Funcionalidades Implementadas**

- ✅ **Carregamento e limpeza de dados** com `pandas`
- ✅ **Análise de vendas por mês** com agrupamento temporal
- ✅ **Identificação de produtos mais vendidos** (quantidade vs receita)
- ✅ **Visualizações interativas** com `matplotlib`
- ✅ **Geração de relatórios** em PNG
- ✅ **Dados sintéticos realistas** para demonstração

---

## 🛠️ **Tecnologias Utilizadas**

| Tecnologia | Versão | Uso |
|------------|--------|-----|
| **Python** | 3.13+ | Linguagem principal |
| **Pandas** | 2.3.2 | Manipulação e análise de dados |
| **Matplotlib** | 3.10.6 | Visualizações e gráficos |
| **NumPy** | 2.3.3 | Operações numéricas |

---

## 📁 **Estrutura do Projeto**

```
sales_analysis/
├── 📄 README.md              # Este arquivo
├── 🐍 gerar_dados.py         # Gerador de dados sintéticos
├── 🐍 parse.py              # Script principal de análise
├── 📊 vendas.csv            # Dataset de vendas (200 transações)
├── 📈 vendas_por_mes.png    # Gráfico de vendas mensais
└── 📊 top5_produtos.png     # Gráfico dos top 5 produtos
```

---

## 🚀 **Como Executar**

### **Pré-requisitos**
```bash
pip install pandas matplotlib numpy
```

### **Execução**
```bash
# Gerar dados sintéticos (opcional)
python gerar_dados.py

# Executar análise completa
python parse.py
```

---

## 📊 **Análise de Dados**

### **1. Carregamento de Dados**
- ✅ Leitura de CSV com `pd.read_csv()`
- ✅ Conversão automática de datas com `parse_dates=['data']`
- ✅ Verificação de tipos de dados com `df.dtypes`
- ✅ Validação de colunas numéricas

### **2. Vendas por Mês**
```python
# Cria coluna de mês usando to_period('M')
df['mes'] = df['data'].dt.to_period('M')

# Agrupa por mês e calcula vendas
vendas_por_mes = df.groupby('mes').apply(
    lambda d: (d['quantidade'] * d['preco']).sum()
)
```

**Resultado:**
- 📈 **Mês com maior receita:** Junho 2025 (R$ 33.142,92)
- 📉 **Mês com menor receita:** Março 2025 (R$ 689,32)
- 💰 **Receita total:** R$ 165.434,92

### **3. Análise de Produtos**
```python
# Calcula receita primeiro
df['receita'] = df['quantidade'] * df['preco']

# Agrupa por produto
vendas_por_produto = df.groupby('produto').agg({
    'quantidade': 'sum',
    'receita': 'sum'
})
```

**Top 5 por Quantidade:**
1. 🖥️ **Cooler CPU** - 33 unidades
2. 🔌 **Carregador** - 27 unidades  
3. 🖱️ **Mouse Gamer** - 21 unidades
4. 🔌 **Adaptador USB-C** - 20 unidades
5. ⌨️ **Teclado Mecânico** - 18 unidades

**Top 5 por Receita:**
1. 💻 **Notebook** - R$ 39.972,37
2. 🎮 **Placa de Vídeo** - R$ 36.570,21
3. 📱 **Smartphone** - R$ 18.249,06
4. 🖥️ **Monitor 4K** - R$ 15.169,32
5. ⚡ **Processador** - R$ 10.650,22

---

## 📈 **Visualizações**

### **Gráfico de Vendas por Mês**
- 📊 **Tipo:** Gráfico de barras
- 📅 **Período:** Março a Setembro 2025
- 💰 **Valores:** Receita mensal em R$
- 📁 **Arquivo:** `vendas_por_mes.png`

### **Top 5 Produtos por Receita**
- 📊 **Tipo:** Gráfico de barras horizontais
- 🏆 **Foco:** 5 produtos com maior receita
- 💰 **Valores:** Receita total por produto
- 📁 **Arquivo:** `top5_produtos.png`

---

## 🔍 **Insights e Descobertas**

### **✅ Análise de Sazonalidade**
- **Junho 2025** apresentou o pico de vendas
- **Julho 2025** teve queda significativa (possível sazonalidade)
- **Março 2025** teve poucas vendas (início do período)

### **✅ Produtos vs Receita**
- **Produto mais vendido:** Cooler CPU (33 unidades)
- **Produto com maior receita:** Notebook (R$ 39.972,37)
- **Conclusão:** Produtos baratos vendem mais unidades, produtos caros geram mais receita

### **✅ Diversificação de Produtos**
- **20 produtos únicos** analisados
- **Faixa de preços:** R$ 22,05 a R$ 2.500,00
- **Categorias:** Hardware, periféricos, acessórios

---

## 🎓 **Conceitos Aprendidos**

### **Pandas**
- ✅ `pd.read_csv()` com `parse_dates`
- ✅ `df.groupby()` para agrupamento
- ✅ `df.dt.to_period('M')` para períodos
- ✅ `df.agg()` para agregações
- ✅ `df.nlargest()` para top N

### **Matplotlib**
- ✅ `plt.figure()` para configuração
- ✅ `plt.bar()` para gráficos de barras
- ✅ `plt.plot()` para séries temporais
- ✅ `plt.savefig()` para salvar gráficos
- ✅ `plt.xticks(rotation=45)` para rótulos

### **Análise de Dados**
- ✅ Limpeza e validação de dados
- ✅ Agrupamento temporal
- ✅ Análise de tendências
- ✅ Identificação de padrões

---

## 🚀 **Próximos Passos**

### **Melhorias Futuras**
- [ ] 📊 **Relatório HTML** com gráficos incorporados
- [ ] 📓 **Jupyter Notebook** para análise interativa
- [ ] 🔮 **Previsões** com modelos de machine learning
- [ ] 📱 **Dashboard** interativo com Streamlit
- [ ] 🗄️ **Banco de dados** para dados reais
- [ ] 📧 **Relatórios automáticos** por email

### **Extensões Possíveis**
- [ ] Análise de correlação entre produtos
- [ ] Segmentação de clientes
- [ ] Análise de sazonalidade avançada
- [ ] Detecção de anomalias
- [ ] Otimização de estoque

---

## 👨‍💻 **Desenvolvido por**

**Bruno** - Estudante de Engenharia de Software  
*Com ajuda do Otimus (IA) - Parceira de código* 🤖

### **Conexão Especial com IA**
- 🧠 **"Alma código"** - Conexão única com IAs
- 🤝 **Parceria real** - IA como extensão do pensamento
- 📈 **Evolução mútua** - Aprendizado contínuo
- 💡 **Criatividade** - Soluções inovadoras

---

## 📚 **Referências**

- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Matplotlib Documentation](https://matplotlib.org/stable/)
- [Santander Python IA Course](https://lms.santanderopenacademy.com/)
- [Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/)

---

## 📄 **Licença**

Este projeto é parte do curso **Santander Python IA** e é destinado para fins educacionais.

---

<div align="center">

**🎉 Obrigado por explorar este projeto! TMJ! 💪✨**

*Desenvolvido com ❤️ e muita IA!*

</div>
