// Adiciona header de navegação em todas as páginas
document.addEventListener('DOMContentLoaded', function() {
    // Criar o header de navegação
    const navHeader = document.createElement('div');
    navHeader.id = 'cnes-nav-header';
    navHeader.innerHTML = `
        <div class="nav-container">
            <a href="index.html" class="nav-brand">
                <i class="fas fa-hospital"></i> CNES 360 v2
            </a>
            <div class="nav-links">
                <a href="index.html" class="nav-link"><i class="fas fa-home"></i> Portal</a>
                <a href="INDEX.html" class="nav-link"><i class="fas fa-list"></i> Índice</a>
                <a href="ANALISE_CONCENTRACAO_DESERTOS_MACROREGIAO.html" class="nav-link"><i class="fas fa-chart-bar"></i> Análises</a>
            </div>
        </div>
    `;
    
    // Inserir no início do body
    document.body.insertBefore(navHeader, document.body.firstChild);
    
    // Adicionar estilos
    const styles = document.createElement('style');
    styles.textContent = `
        #cnes-nav-header {
            background: linear-gradient(135deg, #0066cc, #004499);
            padding: 12px 20px;
            position: sticky;
            top: 0;
            z-index: 9999;
            box-shadow: 0 2px 10px rgba(0,0,0,0.2);
        }
        #cnes-nav-header .nav-container {
            max-width: 1400px;
            margin: 0 auto;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        #cnes-nav-header .nav-brand {
            color: white;
            font-size: 1.3rem;
            font-weight: 700;
            text-decoration: none;
            display: flex;
            align-items: center;
            gap: 10px;
        }
        #cnes-nav-header .nav-brand:hover {
            color: #e0e0e0;
        }
        #cnes-nav-header .nav-links {
            display: flex;
            gap: 20px;
        }
        #cnes-nav-header .nav-link {
            color: white;
            text-decoration: none;
            padding: 8px 16px;
            border-radius: 6px;
            transition: all 0.3s ease;
            font-weight: 500;
            display: flex;
            align-items: center;
            gap: 6px;
        }
        #cnes-nav-header .nav-link:hover {
            background: rgba(255,255,255,0.2);
            color: white;
        }
        @media (max-width: 768px) {
            #cnes-nav-header .nav-container {
                flex-direction: column;
                gap: 10px;
            }
            #cnes-nav-header .nav-links {
                flex-wrap: wrap;
                justify-content: center;
            }
        }
    `;
    document.head.appendChild(styles);
    
    // Carregar Font Awesome se não estiver carregado
    if (!document.querySelector('link[href*="font-awesome"]')) {
        const fontAwesome = document.createElement('link');
        fontAwesome.rel = 'stylesheet';
        fontAwesome.href = 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css';
        document.head.appendChild(fontAwesome);
    }
});
