// Navegação do CNES 360 v2
(function() {
    // Detectar nível de profundidade da página
    const path = window.location.pathname;
    const isSubfolder = path.includes('/analises/') || path.includes('/metodologias/') || 
                        path.includes('/guias/') || path.includes('/tecnicos/') || 
                        path.includes('/projetos/');
    const prefix = isSubfolder ? '../' : '';
    
    // Mapa de navegação
    const pages = [
        { name: 'Portal', url: prefix + 'index.html', icon: 'fa-home' },
        { name: 'Índice', url: prefix + 'INDEX.html', icon: 'fa-list' },
        { name: 'Análise Macrorregião', url: prefix + 'analises/ANALISE_CONCENTRACAO_DESERTOS_MACROREGIAO.html', icon: 'fa-chart-bar' },
        { name: 'Clusterização', url: prefix + 'analises/CLUSTERIZACAO_LEITOS_CNES.html', icon: 'fa-project-diagram' },
        { name: 'Taxonomia', url: prefix + 'metodologias/TAXONOMIA_LEITOS_CNES.html', icon: 'fa-sitemap' },
        { name: 'Tipologia', url: prefix + 'metodologias/TIPOLOGIA_LEITOS_CNES.html', icon: 'fa-tags' },
        { name: 'Guia Decisão', url: prefix + 'guias/GUIA_TOMADA_DECISAO.html', icon: 'fa-compass' },
        { name: 'Nota Técnica', url: prefix + 'tecnicos/NOTA_TECNICA_ETL_CNES_LEITOS.html', icon: 'fa-cogs' },
        { name: 'Projeto', url: prefix + 'projetos/PROJETO.html', icon: 'fa-info-circle' },
        { name: 'Terra SUS', url: prefix + 'projetos/PROJETO_TERRA_SUS.html', icon: 'fa-globe' }
    ];
    
    // Encontrar página atual
    let currentIndex = -1;
    const currentPath = window.location.pathname;
    pages.forEach((page, index) => {
        if (currentPath.endsWith(page.url.replace(prefix, '').replace('../', ''))) {
            currentIndex = index;
        }
    });
    
    // Criar header de navegação
    const header = document.createElement('div');
    header.className = 'cnes-nav-header';
    header.innerHTML = `
        <div class="cnes-nav-container">
            <div class="cnes-nav-brand">
                <a href="${prefix}index.html">
                    <i class="fas fa-hospital"></i>
                    <span>CNES 360 - Terra SUS</span>
                </a>
            </div>
            <div class="cnes-nav-links">
                <a href="${prefix}index.html" class="cnes-nav-link" title="Portal">
                    <i class="fas fa-home"></i> Portal
                </a>
                <a href="${prefix}INDEX.html" class="cnes-nav-link" title="Índice">
                    <i class="fas fa-list"></i> Índice
                </a>
                <div class="cnes-nav-dropdown">
                    <button class="cnes-nav-link cnes-dropdown-toggle">
                        <i class="fas fa-file-alt"></i> Documentos <i class="fas fa-chevron-down"></i>
                    </button>
                    <div class="cnes-dropdown-menu">
                        <a href="${prefix}analises/ANALISE_CONCENTRACAO_DESERTOS_MACROREGIAO.html"><i class="fas fa-chart-bar"></i> Análise Macrorregião</a>
                        <a href="${prefix}analises/CLUSTERIZACAO_LEITOS_CNES.html"><i class="fas fa-project-diagram"></i> Clusterização</a>
                        <a href="${prefix}metodologias/TAXONOMIA_LEITOS_CNES.html"><i class="fas fa-sitemap"></i> Taxonomia</a>
                        <a href="${prefix}metodologias/TIPOLOGIA_LEITOS_CNES.html"><i class="fas fa-tags"></i> Tipologia</a>
                        <a href="${prefix}guias/GUIA_TOMADA_DECISAO.html"><i class="fas fa-compass"></i> Guia Decisão</a>
                        <a href="${prefix}tecnicos/NOTA_TECNICA_ETL_CNES_LEITOS.html"><i class="fas fa-cogs"></i> Nota Técnica</a>
                        <a href="${prefix}projetos/PROJETO.html"><i class="fas fa-info-circle"></i> Projeto</a>
                        <a href="${prefix}projetos/PROJETO_TERRA_SUS.html"><i class="fas fa-globe"></i> Terra SUS</a>
                    </div>
                </div>
            </div>
            <div class="cnes-nav-arrows">
                ${currentIndex > 0 ? `<a href="${pages[currentIndex - 1].url}" class="cnes-nav-arrow" title="${pages[currentIndex - 1].name}"><i class="fas fa-chevron-left"></i> Anterior</a>` : '<span class="cnes-nav-arrow disabled"><i class="fas fa-chevron-left"></i> Anterior</span>'}
                ${currentIndex < pages.length - 1 && currentIndex >= 0 ? `<a href="${pages[currentIndex + 1].url}" class="cnes-nav-arrow" title="${pages[currentIndex + 1].name}">Próximo <i class="fas fa-chevron-right"></i></a>` : '<span class="cnes-nav-arrow disabled">Próximo <i class="fas fa-chevron-right"></i></span>'}
            </div>
        </div>
    `;
    
    // Inserir no início do body
    document.body.insertBefore(header, document.body.firstChild);
    
    // Adicionar evento de dropdown
    const dropdownToggle = document.querySelector('.cnes-dropdown-toggle');
    const dropdownMenu = document.querySelector('.cnes-dropdown-menu');
    
    if (dropdownToggle && dropdownMenu) {
        dropdownToggle.addEventListener('click', function(e) {
            e.preventDefault();
            dropdownMenu.classList.toggle('show');
        });
        
        // Fechar dropdown ao clicar fora
        document.addEventListener('click', function(e) {
            if (!e.target.closest('.cnes-nav-dropdown')) {
                dropdownMenu.classList.remove('show');
            }
        });
    }
})();
