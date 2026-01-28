#!/usr/bin/env python3
"""
Análise de Dados de Macrorregiões de Saúde - IBGE
Integração com dados CNES para análise regionalizada
"""

import pandas as pd

print("=== ANÁLISE DE DADOS DE MACRORREGIÕES DE SAÚDE - IBGE ===")
print()

# Carregar dados e limpar formatação
df_ibge = pd.read_csv('dados macroregião/TB_IBGE_DTB (1).csv', sep=';')

# Limpar colunas numéricas
df_ibge['nu_area'] = df_ibge['nu_area'].astype(str).str.replace(
    ',', '').astype(float)
df_ibge['nu_idh'] = df_ibge['nu_idh'].astype(str).str.replace(
    ',', '.').astype(float)

print("1. ESTRUTURA DOS DADOS")
print("-" * 50)
print(f"Total de registros: {len(df_ibge):,}")
print(f"Total de municípios: {df_ibge['co_municipio_ibge'].nunique():,}")
print(f"Total de UFs: {df_ibge['co_uf'].nunique():,}")
print(f"Total de macrorregiões: "
      f"{df_ibge['Macrorregião de Saúde'].nunique():,}")
print(f"Total de regiões de saúde: "
      f"{df_ibge['Região de Saúde'].nunique():,}")
print()

# Análise por macrorregião
print("2. MACRORREGIÕES DE SAÚDE - MAIORES (Top 20)")
print("-" * 70)
macro_stats = df_ibge.groupby('Macrorregião de Saúde').agg({
    'co_municipio_ibge': 'count',
    'nu_area': 'sum',
    'nu_idh': 'mean'
}).round(2)
macro_stats.columns = [
    'Nº Municípios', 'Área Total (km²)', 'IDH Médio'
]
macro_stats = macro_stats.sort_values('Nº Municípios', ascending=False)
print(macro_stats.head(20))
print()

# Análise por UF
print("3. DISTRIBUIÇÃO POR UNIDADE FEDERATIVA")
print("-" * 50)
uf_stats = df_ibge.groupby(['sg_uf', 'no_uf']).agg({
    'co_municipio_ibge': 'count',
    'Macrorregião de Saúde': 'nunique',
    'Região de Saúde': 'nunique',
    'nu_idh': 'mean'
}).round(2)
uf_stats.columns = [
    'Municípios', 'Macrorregiões', 'Regiões de Saúde', 'IDH Médio'
]
print(uf_stats.sort_values('Municípios', ascending=False))
print()

# Análise por região geográfica
print("4. ANÁLISE POR REGIÃO GEOGRÁFICA")
print("-" * 50)
regiao_stats = df_ibge.groupby('no_regiao').agg({
    'co_municipio_ibge': 'count',
    'Macrorregião de Saúde': 'nunique',
    'nu_area': 'sum',
    'nu_idh': ['mean', 'min', 'max']
}).round(2)
regiao_stats.columns = [
    'Municípios', 'Macrorregiões', 'Área Total',
    'IDH Médio', 'IDH Mínimo', 'IDH Máximo'
]
print(regiao_stats)
print()

# Análise de IDH
print("5. ANÁLISE DE IDH POR MACRORREGIÃO")
print("-" * 50)
idh_macro = df_ibge.groupby('Macrorregião de Saúde')['nu_idh'].agg(['count', 'mean', 'std', 'min', 'max']).round(3)
idh_macro.columns = [
    'Municípios', 'IDH Médio', 'Desvio Padrão',
    'IDH Mínimo', 'IDH Máximo'
]
idh_macro = idh_macro.sort_values('IDH Médio', ascending=False)
print("Top 15 Macrorregiões por IDH Médio:")
print(idh_macro.head(15))
print()

# Análise de área
print("6. MACRORREGIÕES - MAIORES ÁREAS")
print("-" * 50)
area_macro = df_ibge.groupby('Macrorregião de Saúde')['nu_area'].agg(['count', 'sum', 'mean']).round(2)
area_macro.columns = [
    'Municípios', 'Área Total (km²)',
    'Área Média/Município'
]
area_macro = area_macro.sort_values('Área Total (km²)', ascending=False)
print(area_macro.head(15))
print()

# Verificar correspondência com dados CNES
print("7. INTEGRAÇÃO COM DADOS CNES")
print("-" * 50)
# Carregar dados CNES
try:
    df_cnes = pd.read_csv('arq7_analise_municipios.csv', sep=';')
    
    # Converter códigos municipais para comparar
    df_ibge['co_municipio_ibge'] = df_ibge['co_municipio_ibge'].astype(str)
    df_cnes['codufmun'] = df_cnes['codufmun'].astype(str)
    
    # Merge para enriquecer dados
    df_merge = df_cnes.merge(
        df_ibge[['co_municipio_ibge', 'Macrorregião de Saúde',
                'no_regiao', 'nu_idh']],
        left_on='codufmun', right_on='co_municipio_ibge', how='left'
    )
    
    print(f"Municípios CNES: {len(df_cnes):,}")
    print(f"Municípios com correspondência IBGE: {df_merge['Macrorregião de Saúde'].notna().sum():,}")
    print(f"Taxa de correspondência: {df_merge['Macrorregião de Saúde'].notna().sum()/len(df_cnes)*100:.1f}%")
    print()
    
    # Análise por macrorregião de saúde (dados IBGE)
    if df_merge['Macrorregião de Saúde'].notna().sum() > 0:
        print("Análise de Leitos por Macrorregião de Saúde (IBGE):")
        print("-" * 60)
        macro_leitos = df_merge.groupby(
            'Macrorregião de Saúde'
        ).agg({
            'total_leitos': 'sum',
            'leitos_sus': 'sum',
            'n_estabelecimentos': 'sum',
            'codufmun': 'count',
            'nu_idh': 'mean'
        }).round(1)
        macro_leitos.columns = [
            'Leitos Totais', 'Leitos SUS', 'Estabelecimentos',
            'Municípios', 'IDH Médio'
        ]
        macro_leitos['% SUS'] = (
            macro_leitos['Leitos SUS'] /
            macro_leitos['Leitos Totais'] * 100
        ).round(1)
        macro_leitos['Leitos/Município'] = (
            macro_leitos['Leitos Totais'] /
            macro_leitos['Municípios']
        ).round(1)
        print(macro_leitos.sort_values(
            'Leitos Totais', ascending=False
        ).head(15))
        
        # Salvar arquivo enriquecido
        df_merge.to_csv(
            'arq8_analise_municipios_enriquecido.csv',
            sep=';', index=False, encoding='utf-8'
        )
        print()
        print("Arquivo enriquecido salvo: arq8_analise_municipios_enriquecido.csv")
        
except Exception as e:
    print(f"Erro ao integrar com dados CNES: {e}")

print()
print("=== ESTATÍSTICAS FINAIS ===")
print(f"Total de macrorregiões de saúde no Brasil: {df_ibge['Macrorregião de Saúde'].nunique():,}")
print(f"Média de municípios por macrorregião: "
      f"{len(df_ibge)/df_ibge['Macrorregião de Saúde'].nunique():.1f}")
print(f"IDH médio nacional: {df_ibge['nu_idh'].mean():.3f}")
print(f"Área total coberta: {df_ibge['nu_area'].sum():,.0f} km²")

# Salvar análise de macrorregiões
macro_stats.to_csv(
    'analise_macrorregioes_ibge.csv',
    sep=';', encoding='utf-8'
)
print("Análise de macrorregiões salva: "
      "analise_macrorregioes_ibge.csv")
