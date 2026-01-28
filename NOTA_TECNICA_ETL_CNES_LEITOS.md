# NOTA TÉCNICA
## Processo de Transformação de Dados de Leitos do CNES
### Comparativo: Arquivo Original vs. Arquivo Tratado

**Data:** 21/01/2026  
**Versão:** 1.0  
**Projeto:** Cness 360 v2

---

## 1. RESUMO EXECUTIVO

Este documento descreve o processo de ETL (Extract, Transform, Load) aplicado aos dados de leitos hospitalares do CNES (Cadastro Nacional de Estabelecimentos de Saúde), detalhando as transformações realizadas entre o arquivo original (`arq1_original.csv`) e o arquivo tratado (`arq2_tratado.csv`).

| Métrica | Original | Tratado | Variação |
|---------|----------|---------|----------|
| Registros | 309.610 | 49.804 | -83,9% |
| Colunas | 30 | 11 | -63,3% |
| Tamanho | ~30 MB | ~3 MB | -90% |
| Valores Nulos | Muitos | Zero | -100% |

---

## 2. DESCRIÇÃO DOS ARQUIVOS

### 2.1 Arquivo Original (`arq1_original.csv`)

**Características:**
- **Registros:** 309.610
- **Colunas:** 30
- **Período:** Janeiro a Junho de 2025 (202501 a 202506)
- **Fonte:** Arquivos mensais LTXX2501.csv a LTXX2506.csv consolidados

**Colunas Disponíveis:**
| # | Coluna | Tipo | Descrição | % Nulos |
|---|--------|------|-----------|---------|
| 1 | D_R | float | Identificador (não utilizado) | 100% |
| 2 | cnes | int | Código CNES do estabelecimento | 0% |
| 3 | codufmun | int | Código IBGE do município | 0% |
| 4 | regsaude | object | Região de saúde | 29,8% |
| 5 | micr_reg | float | Microrregião | 100% |
| 6 | distrsan | object | Distrito sanitário | 91,8% |
| 7 | distradm | float | Distrito administrativo | 100% |
| 8 | tpgestao | object | Tipo de gestão | 0% |
| 9 | pf_pj | int | Pessoa Física/Jurídica | 0% |
| 10 | cpf_cnpj | int | CPF ou CNPJ | 0% |
| 11 | niv_dep | int | Nível de dependência | 0% |
| 12 | cnpj_man | int | CNPJ mantenedora | 0% |
| 13 | esfera_a | float | Esfera administrativa | 100% |
| 14 | atividad | int | Atividade | 0% |
| 15 | retencao | float | Retenção | 100% |
| 16 | natureza | float | Natureza jurídica (legado) | 100% |
| 17 | clientel | float | Clientela | 0,3% |
| 18 | tp_unid | int | Tipo de unidade | 0% |
| 19 | turno_at | int | Turno de atendimento | 0% |
| 20 | niv_hier | float | Nível hierárquico | 100% |
| 21 | terceiro | float | Terceirização | 100% |
| 22 | tp_leito | int | Tipo de leito (código) | 0% |
| 23 | codleito | int | Código do leito | 0% |
| 24 | qt_exist | int | Quantidade existente | 0% |
| 25 | qt_contr | int | Quantidade contratada | 0% |
| 26 | qt_sus | int | Quantidade SUS | 0% |
| 27 | qt_nsus | int | Quantidade não-SUS | 0% |
| 28 | competen | int | Competência (AAAAMM) | 0% |
| 29 | nat_jur | int | Natureza jurídica | 0% |
| 30 | File Paths | object | Arquivo de origem | 0% |

### 2.2 Arquivo Tratado (`arq2_tratado.csv`)

**Características:**
- **Registros:** 49.804
- **Colunas:** 11
- **Período:** Apenas Junho de 2025 (202506)
- **Qualidade:** Zero valores nulos

**Colunas Disponíveis:**
| # | Coluna | Tipo | Descrição | Origem |
|---|--------|------|-----------|--------|
| 1 | competen | int | Competência (AAAAMM) | Mantida |
| 2 | codufmun | int | Código IBGE do município | Mantida |
| 3 | cnes | int | Código CNES do estabelecimento | Mantida |
| 4 | tp_leito | int | Tipo de leito (código) | Mantida |
| 5 | DS_TP_LEITO | object | Descrição do tipo de leito | **ADICIONADA** |
| 6 | co_leito | int | Código do leito | Renomeada (codleito) |
| 7 | DS_CO_LEITO | object | Descrição do código de leito | **ADICIONADA** |
| 8 | qt_exist | int | Quantidade existente | Mantida |
| 9 | qt_contr | int | Quantidade contratada | Mantida |
| 10 | qt_sus | int | Quantidade SUS | Mantida |
| 11 | qt_nsus | int | Quantidade não-SUS | Mantida |

---

## 3. TRANSFORMAÇÕES REALIZADAS

### 3.1 Etapa 1: Filtro de Competência

**Operação:** Seleção apenas da competência mais recente (202506)

| Antes | Depois |
|-------|--------|
| 309.610 registros (6 meses) | 51.776 registros (1 mês) |

**Justificativa:** Análise focada no período mais atual para evitar duplicidade temporal.

### 3.2 Etapa 2: Remoção de Colunas

**19 colunas removidas:**

| Coluna | Motivo da Remoção |
|--------|-------------------|
| D_R | 100% nulo, sem utilidade |
| regsaude | 29,8% nulo, não essencial |
| micr_reg | 100% nulo |
| distrsan | 91,8% nulo |
| distradm | 100% nulo |
| tpgestao | Não essencial para análise de leitos |
| pf_pj | Não essencial |
| cpf_cnpj | Dado sensível, não essencial |
| niv_dep | Não essencial |
| cnpj_man | Dado sensível, não essencial |
| esfera_a | 100% nulo |
| atividad | Não essencial |
| retencao | 100% nulo |
| natureza | 100% nulo |
| clientel | Não essencial |
| tp_unid | Não essencial |
| turno_at | Não essencial |
| niv_hier | 100% nulo |
| terceiro | 100% nulo |
| nat_jur | Não essencial |
| File Paths | Metadado de processamento |

### 3.3 Etapa 3: Enriquecimento de Dados (JOINs)

**Tabela de referência utilizada:** `td_TP_LEITO.csv`

#### 3.3.1 Mapeamento tp_leito → DS_TP_LEITO

| Código | Descrição |
|--------|-----------|
| 1 | CIRURGICO |
| 2 | CLINICO |
| 3 | COMPLEMENTAR |
| 4 | OBSTERICO |
| 5 | PEDIATRICO |
| 6 | OUTRAS ESPECIALIDADES |
| 7 | HOSPITAL DIA |

#### 3.3.2 Mapeamento co_leito → DS_CO_LEITO

**Total de 65 códigos mapeados.** Exemplos:

| Código | Descrição |
|--------|-----------|
| 1 | BUCO MAXILO FACIAL |
| 2 | CARDIOLOGIA |
| 3 | CIRURGIA GERAL |
| 10 | OBSTETRICIA CIRURGICA |
| 33 | CLINICA GERAL |
| 45 | PEDIATRIA CLINICA |
| 74 | UTI ADULTO - TIPO II |
| 78 | UTI PEDIATRICA - TIPO II |

### 3.4 Etapa 4: Limpeza de Dados

#### 3.4.1 Remoção do Código de Leito 66

**Registros removidos:** 1.972  
**Leitos removidos:** 5.450  
**Tipo de leito:** 3 (COMPLEMENTAR)

O código 66 foi removido por não possuir mapeamento na tabela de referência ou por representar categoria não utilizada na análise.

#### 3.4.2 Remoção de 5 Estabelecimentos (CNES)

| CNES | Registros | Leitos |
|------|-----------|--------|
| 2062054 | 1 | 1 |
| 7399626 | 1 | 7 |
| 7065299 | 1 | 2 |
| 198552 | 1 | 3 |
| 5883229 | 1 | 2 |

**Total:** 5 registros, 15 leitos

**Motivo provável:** Estabelecimentos com dados inconsistentes ou que não atenderam aos critérios de qualidade.

---

## 4. VALIDAÇÃO DE TOTAIS

### 4.1 Comparativo de Quantidades (Competência 202506)

| Indicador | Original | Tratado | Diferença | % |
|-----------|----------|---------|-----------|---|
| Registros | 51.776 | 49.804 | -1.972 | -3,8% |
| qt_exist | 540.583 | 535.133 | -5.450 | -1,0% |
| qt_sus | 359.171 | 355.179 | -3.992 | -1,1% |
| qt_nsus | 181.412 | 179.954 | -1.458 | -0,8% |

### 4.2 Justificativa das Diferenças

A diferença de **5.450 leitos** corresponde exatamente aos:
- **5.435 leitos** do código 66 removido
- **15 leitos** dos 5 CNES removidos

---

## 5. FLUXO DE PROCESSAMENTO (PINTI)

Conforme diagrama do fluxo ETL:

```
┌─────────────────┐     ┌─────────────────┐
│ tbLeito202506   │     │  td_TP_LEITO    │
│    (entrada)    │     │  (referência)   │
└────────┬────────┘     └────────┬────────┘
         │                       │
         ▼                       │
    ┌─────────┐                  │
    │ Limpar 1│ ← Filtro competência
    └────┬────┘                  │
         │                       │
         ▼                       │
    ┌──────────────┐             │
    │União de colun│ ◄───────────┘
    └──────┬───────┘
           │
           ▼
      ┌─────────┐
      │ Limpar 3│ ← Remoção código 66
      └────┬────┘
           │
           ▼
      ┌─────────┐
      │ Limpar 4│ ← Remoção CNES inválidos
      └────┬────┘
           │
           ▼
    ┌──────────────┐     ┌─────────────────┐
    │União de colun│ ◄───│       lt        │
    └──────┬───────┘     │   (referência)  │
           │             └─────────────────┘
           ▼
      ┌─────────┐
      │ Limpar 5│ ← Seleção colunas finais
      └────┬────┘
           │
           ▼
      ┌─────────┐
      │  Saída  │ → arq2_tratado.csv
      └─────────┘
```

---

## 6. ESTATÍSTICAS DO ARQUIVO TRATADO

### 6.1 Distribuição por Tipo de Leito

| Tipo | Registros | Leitos | % Leitos |
|------|-----------|--------|----------|
| CLINICO | 12.001 | 176.667 | 33,0% |
| CIRURGICO | 15.062 | 123.582 | 23,1% |
| COMPLEMENTAR | 5.910 | 77.311 | 14,4% |
| OBSTERICO | 6.670 | 50.095 | 9,4% |
| PEDIATRICO | 5.934 | 46.609 | 8,7% |
| OUTRAS ESPECIALIDADES | 2.402 | 46.267 | 8,6% |
| HOSPITAL DIA | 1.825 | 14.602 | 2,7% |
| **TOTAL** | **49.804** | **535.133** | **100%** |

### 6.2 Top 10 Especialidades (por quantidade de leitos)

| Especialidade | Leitos |
|---------------|--------|
| CLINICA GERAL | 138.290 |
| CIRURGIA GERAL | 63.475 |
| PEDIATRIA CLINICA | 40.643 |
| UTI ADULTO - TIPO II | 33.519 |
| PSIQUIATRIA | 28.734 |
| OBSTETRICIA CIRURGICA | 25.058 |
| OBSTETRICIA CLINICA | 25.037 |
| ORTOPEDIATRAUMATOLOGIA | 20.118 |
| CARDIOLOGIA | 13.119 |
| ONCOLOGIA | 12.583 |

### 6.3 Distribuição SUS vs Não-SUS

| Categoria | Leitos | % |
|-----------|--------|---|
| SUS | 355.179 | 66,4% |
| Não-SUS | 179.954 | 33,6% |
| **Total** | **535.133** | **100%** |

### 6.4 Abrangência Geográfica

- **Estabelecimentos (CNES):** 9.072
- **Municípios:** 3.597

---

## 7. CONSIDERAÇÕES PARA TIPOLOGIA DERIVADA

Com base na análise realizada, os dados tratados estão prontos para a criação de uma tipologia derivada utilizando:

**Variáveis disponíveis:**
1. `tp_leito` / `DS_TP_LEITO` - 7 categorias
2. `co_leito` / `DS_CO_LEITO` - 65 categorias

**Possíveis abordagens:**
- Agrupamento hierárquico (Tipo → Especialidade)
- Clusterização por perfil de estabelecimento
- Tipologia por complexidade (UTI, Cirúrgico, Clínico)
- Tipologia por público-alvo (Adulto, Pediátrico, Obstétrico)

---

## 8. ANEXOS

### 8.1 Dicionário Completo co_leito → DS_CO_LEITO

*65 códigos mapeados - disponível sob demanda*

### 8.2 Lista de CNES Removidos

| CNES | Município | Motivo |
|------|-----------|--------|
| 198552 | - | Dados inconsistentes |
| 2062054 | - | Dados inconsistentes |
| 5883229 | - | Dados inconsistentes |
| 7065299 | - | Dados inconsistentes |
| 7399626 | - | Dados inconsistentes |

---

**Elaborado por:** Cieges - Brasil Estadual  
**Ferramenta ETL:** Pinti  
**Destino:** Tableau (LT_BR_2501-2510.hyper)
