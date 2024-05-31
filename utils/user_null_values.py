
def verify_values(user):
    if user.notebook is False:
        user.tag_nb = None
        user.modelo_nb = None
        user.num_serie_nb = None
        user.versao_nb = None
        user.configs_nb = None
        user.observacao_nb = None
        
    if user.monitor_1 is False:
        user.modelo_m1 = None
        user.num_serie_m1 = None
        user.observacao_m1 = None
    
    if user.monitor_2 is False:
        user.modelo_m2 = None
        user.num_serie_m2 = None
        user.observacao_m2 = None
    
    if user.teclado is False:
        user.modelo_teclado = None
        user.num_serie_teclado = None
        user.observacao_teclado = None
    
    if user.mouse is False:
        user.modelo_mouse = None
        user.num_serie_mouse = None
        user.observacao_mouse = None

    if user.desktop is False:
        user.tag_desktop = None
        user.modelo_desktop = None
        user.num_serie_desktop = None
        user.versao_desktop = None
        user.configs_desktop = None
        user.observacao_desktop = None
    
    if user.no_break is False:
        user.modelo_no = None
        user.num_serie_no = None
    
    if user.headset is False:
        user.modelo_headset = None
        user.num_serie_headset = None
        
    if user.celular is False:
        user.modelo_cel = None
        user.imei_celular = None
        user.numero_celular = None
        user.observacao_celular = None