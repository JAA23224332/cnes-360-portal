#!/usr/bin/env python3
import pandas as pd
import numpy as np

# Carregar dados
df = pd.read_csv('arq7_analise_municipios.csv', sep=';')

print("=== ANÁLISE POR MACROREGIÃO DE SAÚDE ===")
print()

# 1. Análise geral por macroregião
print("1. DISTRIBUIÇÃO GERAL DE LEITOS POR MACROREGIÃO")
print("-" * 60)
analise_geral = df.groupby('regiao').agg({
    'n_estabelecimentos': 'sum',
    'total_leitos': 'sum',
    'leitos_sus': 'sum',
    'leitos_nsus': 'sum',
    'leitos_intensivo': 'sum',
    'leitos_semi_intensivo': 'sum',
    'leitos_alta_complexidade': 'sum',
    'leitos_media_baixa': 'sum',
    'codufmun': 'count'
}).round(1)

analise_geral.columns = ['Estabelecimentos', 'Leitos Totais', 'Leitos SUS', 'Leitos Não SUS', 
                        'Leitos UTI', 'Leitos UCI', 'Leitos Alta Complexidade', 'Leitos Média/Baixa', 'Municípios']

# Calcular percentuais
analise_geral['% SUS'] = (analise_geral['Leitos SUS'] / analise_geral['Leitos Totais'] * 100).round(1)
analise_geral['% UTI'] = (analise_geral['Leitos UTI'] / analise_geral['Leitos Totais'] * 100).round(1)
analise_geral['% UCI'] = (analise_geral['Leitos UCI'] / analise_geral['Leitos Totais'] * 100).round(1)

print(analise_geral.sort_values('Leitos Totais', ascending=False))
print()

# 2. Análise de classificação de vazios
print("2. CLASSIFICAÇÃO DE VAZIOS ASSISTENCIAIS POR MACROREGIÃO")
print("-" * 60)
vazios = pd.crosstab(df['regiao'], df['classificacao_vazio'], margins=True)
print(vazios)
print()

# 3. Análise de presença de UTI/UCI
print("3. PRESENÇA DE LEITOS ESPECIALIZADOS POR MACROREGIÃO")
print("-" * 60)
especializados = df.groupby('regiao').agg({
    'tem_uti': 'sum',
    'tem_uci': 'sum',
    'tem_alta': 'sum',
    'codufmun': 'count'
}).round(1)

especializados.columns = ['Municípios com UTI', 'Municípios com UCI', 'Municípios com Alta Complexidade', 'Total Municípios']
especializados['% UTI'] = (especializados['Municípios com UTI'] / especializados['Total Municípios'] * 100).round(1)
especializados['% UCI'] = (especializados['Municípios com UCI'] / especializados['Total Municípios'] * 100).round(1)
especializados['% Alta'] = (especializados['Municípios com Alta Complexidade'] / especializados['Total Municípios'] * 100).round(1)

print(especializados.sort_values('Total Municípios', ascending=False))
print()

# 4. Análise de concentração (HHI)
print("4. CONCENTRAÇÃO DE LEITOS (HHI) POR MACROREGIÃO")
print("-" * 60)
hhi_analise = df.groupby('regiao')['hhi'].agg(['mean', 'median', 'std']).round(3)
hhi_analise.columns = ['HHI Médio', 'HHI Mediana', 'HHI Desvio Padrão']
print(hhi_analise.sort_values('HHI Médio', ascending=False))
print()

# 5. Análise per capita (estimado)
print("5. MÉDIA DE LEITOS POR MUNICÍPIO POR MACROREGIÃO")
print("-" * 60)
per_capita = df.groupby('regiao').agg({
    'total_leitos': ['sum', 'mean'],
    'codufmun': 'count'
}).round(1)
per_capita.columns = ['Total Leitos', 'Média Leitos/Município', 'Nº Municípios']
print(per_capita.sort_values('Média Leitos/Município', ascending=False))
print()

print("=== INDICADORES CHAVE POR MACROREGIÃO ===")
print()

# 6. Indicadores chave
indicadores = df.groupby('regiao').agg({
    'total_leitos': 'sum',
    'leitos_sus': 'sum',
    'leitos_intensivo': 'sum',
    'tem_uti': 'sum',
    'codufmun': 'count'
}).round(1)

indicadores['Leitos SUS per capita'] = (indicadores['leitos_sus'] / indicadores['codufmun']).round(1)
indicadores['Leitos UTI per capita'] = (indicadores['leitos_intensivo'] / indicadores['codufmun']).round(1)
indicadores['% Municípios com UTI'] = (indicadores['tem_uti'] / indicadores['codufmun'] * 100).round(1)
indicadores['Densidade Leitos/1000 hab (estimado)'] = (indicadores['total_leitos'] / indicadores['codufmun'] * 0.3).round(2)  # Estimativa

indicadores.columns = ['Total Leitos', 'Total Leitos SUS', 'Total Leitos UTI', 'Municípios com UTI', 'Nº Municípios',
                      'Leitos SUS/Município', 'Leitos UTI/Município', '% Municípios com UTI', 'Leitos/1000 hab (est.)']

print(indicadores.sort_values('Leitos/1000 hab (est.)', ascending=False))

# Salvar análise completa
analise_geral.to_csv('analise_macroregiao_saude.csv', sep=';', encoding='utf-8')
print()
print("Análise salva em: analise_macroregiao_saude.csv")
