# CNES 360 v2 - Portal da Equipe

## 🚀 Deploy Instructions

### Railway Deploy
1. Conecte seu repositório GitHub ao Railway
2. Configure as variáveis de ambiente:
   - `NODE_ENV`: production
   - `PORT`: 8080
3. Railway irá detectar automaticamente o projeto

### Vercel Deploy
1. Importe o projeto no Vercel
2. Configure como Static Site
3. Defina o diretório de saída: `./`
4. Build command: `echo "Build completed"`
5. Output directory: `./`

## 📁 Estrutura do Projeto
```
├── portal_equipe.html    # Land page principal
├── INDEX.html           # Portal de documentação
├── ANALISE_*.html       # Análises interativas
├── *.pdf                # Versões para impressão
├── package.json         # Configuração Node.js
└── README.md           # Este arquivo
```

## 🌐 Acesso
- **Railway**: https://cnes-360-portal.up.railway.app
- **Vercel**: https://cnes-360-portal.vercel.app

## 📊 Conteúdo
- Análise de Desertos e Concentração de Leitos
- Tipologias e Taxonomias de Leitos Hospitalares
- Guias de Tomada de Decisão
- Documentação Técnica ETL
