# 🏥 CNES 360 v2 - Portal de Inteligência em Saúde

Portal de documentação e análises de leitos hospitalares do Brasil.

## 📁 Estrutura do Projeto

```
cnes-360-portal/
│
├── 📁 docs/                    # Documentação HTML
│   ├── index.html              # Land page principal
│   ├── INDEX.html              # Índice técnico
│   ├── portal_equipe.html      # Portal da equipe
│   │
│   ├── 📁 analises/            # Análises de dados
│   │   ├── ANALISE_CONCENTRACAO_DESERTOS_MACROREGIAO.html
│   │   ├── ANALISE_DESERTOS_LEITOS.html
│   │   └── CLUSTERIZACAO_LEITOS_CNES.html
│   │
│   ├── 📁 metodologias/        # Metodologias aplicadas
│   │   ├── TIPOLOGIA_LEITOS_CNES.html
│   │   └── TAXONOMIA_LEITOS_CNES.html
│   │
│   ├── 📁 guias/               # Guias práticos
│   │   └── GUIA_TOMADA_DECISAO.html
│   │
│   ├── 📁 tecnicos/            # Documentação técnica
│   │   └── NOTA_TECNICA_ETL_CNES_LEITOS.html
│   │
│   ├── 📁 projetos/            # Documentos de projeto
│   │   ├── PROJETO.html
│   │   └── PROJETO_TERRA_SUS.html
│   │
│   └── 📁 pdf/                 # Versões PDF
│       └── *.pdf
│
├── 📁 data/                    # Dados do projeto
│   ├── 📁 raw/                 # Dados originais
│   ├── 📁 processed/           # Dados tratados
│   └── 📁 outputs/             # Resultados de análises
│
├── 📁 scripts/                 # Scripts Python
│   ├── analise_completa_tratamento_dados.py
│   ├── analise_dados_macroregiao.py
│   └── diagrama_relacionamento_tabelas.py
│
├── 📁 src/                     # Código fonte Quarto (.qmd)
│   └── *.qmd
│
├── 📁 assets/                  # Recursos estáticos
│   ├── 📁 css/                 # Estilos
│   ├── 📁 js/                  # Scripts
│   └── 📁 images/              # Imagens
│
└── 📁 config/                  # Configurações
    ├── vercel.json
    ├── railway.toml
    └── package.json
```

## 🌐 Acesso Online

- **Vercel**: https://cnes360v2.vercel.app
- **Land Page**: https://cnes360v2.vercel.app/docs/index.html

## 📊 Conteúdo

### Análises
- Concentração e Desertos de Leitos por Macrorregião
- Análise de Desertos de Leitos por Município
- Clusterização de Especialidades

### Metodologias
- Tipologia de Leitos CNES
- Taxonomia Hierárquica de Leitos

### Guias
- Guia de Tomada de Decisão para Gestores

### Documentação Técnica
- Nota Técnica ETL CNES Leitos

## 🚀 Deploy

### Vercel
```bash
vercel --prod
```

### Local
```bash
cd docs && python -m http.server 8080
```

## 👥 Equipe

**Cieges - Brasil Estadual**

## 📄 Licença

MIT
