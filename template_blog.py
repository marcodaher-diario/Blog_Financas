def obter_esqueleto_html(dados):
    cor_base = "#073763"  # Azul MD Arte Foto
    # Definimos os estilos como variáveis para facilitar mudanças globais
    estilo_corpo = f"color: {cor_base} !important; font-family: Arial, sans-serif; font-size: 17px !important; line-height: 1.7 !important;"
    estilo_titulo = f"color: {cor_base} !important; font-size: 38px !important; font-weight: bold; text-align: center; margin-bottom: 20px;"
    estilo_subtitulo = f"color: {cor_base} !important; font-size: 26px !important; font-weight: bold; text-align: left; margin: 25px 0 5px 0;"

    html = f"""
    <div style="{estilo_corpo} width: 100%; max-width: 100%; box-sizing: border-box; overflow-wrap: break-word;">
        
        <h1 style="{estilo_titulo} display: block;">
            {dados['titulo'].upper()}
        </h1>

        <div style='text-align:center; margin-bottom:20px;'>
            <img src='{dados['img_topo']}' style='width:100%; height:auto; aspect-ratio:16/9; object-fit:cover; border-radius:10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);'/>
        </div>

        <div style="{estilo_corpo} text-align: justify; margin:10px 0;">
            {dados['intro']}
        </div>

        <p style='{estilo_subtitulo}'>
            {dados['sub1']}
        </p>
        <div style='{estilo_corpo} text-align: justify; margin:10px 0;'>
            {dados['texto1']}
        </div>

        <div style='text-align:center; margin:30px 0;'>
            <img src='{dados['img_meio']}' style='width:100%; height:auto; aspect-ratio:16/9; object-fit:cover; border-radius:10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);'/>
        </div>

        <p style='{estilo_subtitulo}'>
            {dados['sub2']}
        </p>
        <div style='{estilo_corpo} text-align: justify; margin:10px 0;'>
            {dados['texto2']}
        </div>

        <p style='{estilo_subtitulo}'>
            {dados['sub3']}
        </p>
        <div style='{estilo_corpo} text-align: justify; margin:10px 0;'>
            {dados['texto3']}
        </div>

        <p style='{estilo_subtitulo}'>
            CONSIDERAÇÕES FINAIS
        </p>
        <div style='{estilo_corpo} text-align: justify; margin:10px 0;'>
            {dados['texto_conclusao']}
        </div>

        <div style='margin-top: 20px; border-top: 1px solid #ccc;'>
            {dados['assinatura']}
        </div>
    </div>
    """
    return html
