// Navigation Header para CNES 360 v2
(function() {
    const currentPath = window.location.pathname;
    
    // Determinar nível de profundidade para links relativos
    const depth = (currentPath.match(/\//g) || []).length - 1;
    const prefix = depth > 1 ? '../' : '';
    
    // Criar header de navegação
    const navHTML = `
    <div id="cnes-nav-header" style="
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        z-index: 9999;
        background: linear-gradient(135deg, #0066cc, #004499);
        padding: 12px 20px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.2);
        display: flex;
        justify-content: space-between;
        align-items: center;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    ">
        <div style="display: flex; align-items: center; gap: 15px;">
            <a href="${prefix}index.html" style="
                color: white;
                text-decoration: none;
                font-weight: 600;
                font-size: 1.1rem;
                display: flex;
                align-items: center;
                gap: 8px;
            ">
                <span style="font-size: 1.3rem;">🏥</span>
                CNES 360 v2
            </a>
            <span style="color: rgba(255,255,255,0.5);">|</span>
            <a href="${prefix}INDEX.html" style="
                color: rgba(255,255,255,0.9);
                text-decoration: none;
                font-size: 0.9rem;
                padding: 6px 12px;
                border-radius: 6px;
                transition: background 0.2s;
            " onmouseover="this.style.background='rgba(255,255,255,0.1)'" onmouseout="this.style.background='transparent'">
                📚 Índice
            </a>
        </div>
        <div style="display: flex; align-items: center; gap: 10px;">
            <button onclick="history.back()" style="
                background: rgba(255,255,255,0.15);
                border: none;
                color: white;
                padding: 8px 16px;
                border-radius: 6px;
                cursor: pointer;
                font-size: 0.85rem;
                display: flex;
                align-items: center;
                gap: 6px;
                transition: background 0.2s;
            " onmouseover="this.style.background='rgba(255,255,255,0.25)'" onmouseout="this.style.background='rgba(255,255,255,0.15)'">
                ← Voltar
            </button>
            <button onclick="history.forward()" style="
                background: rgba(255,255,255,0.15);
                border: none;
                color: white;
                padding: 8px 16px;
                border-radius: 6px;
                cursor: pointer;
                font-size: 0.85rem;
                display: flex;
                align-items: center;
                gap: 6px;
                transition: background 0.2s;
            " onmouseover="this.style.background='rgba(255,255,255,0.25)'" onmouseout="this.style.background='rgba(255,255,255,0.15)'">
                Avançar →
            </button>
            <a href="${prefix}index.html" style="
                background: #00a86b;
                color: white;
                text-decoration: none;
                padding: 8px 16px;
                border-radius: 6px;
                font-size: 0.85rem;
                font-weight: 500;
                display: flex;
                align-items: center;
                gap: 6px;
                transition: background 0.2s;
            " onmouseover="this.style.background='#008f5b'" onmouseout="this.style.background='#00a86b'">
                🏠 Portal
            </a>
        </div>
    </div>
    `;
    
    // Inserir no início do body
    document.body.insertAdjacentHTML('afterbegin', navHTML);
    
    // Adicionar padding ao body para compensar o header fixo
    document.body.style.paddingTop = '60px';
    
    // Ajustar sidebar do Quarto se existir
    const sidebar = document.querySelector('#quarto-sidebar');
    if (sidebar) {
        sidebar.style.top = '60px';
    }
    
    const marginSidebar = document.querySelector('#quarto-margin-sidebar');
    if (marginSidebar) {
        marginSidebar.style.top = '60px';
    }
})();
