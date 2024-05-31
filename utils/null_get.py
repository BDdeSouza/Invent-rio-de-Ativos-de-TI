def filter_user(user):
    if user['notebook']['tag_nb'] is None and user['notebook']['modelo_nb'] is None:
        user["notebook"] = None
        
    if user['monitor_1']['modelo_m1'] is None and user['monitor_1']['num_serie_m1'] is None:
        user["monitor_1"] = None
        
    if user['monitor_2']['modelo_m2'] is None and user['monitor_2']['num_serie_m2'] is None:
        user["monitor_2"] = None   
    
    if user['teclado']['modelo_teclado'] is None and user['teclado']['num_serie_teclado'] is None:
        user["teclado"] = None 
        
    if user['mouse']['modelo_mouse'] is None and user['mouse']['num_serie_mouse'] is None:
        user["mouse"] = None
    
    if user['desktop']['tag_desktop'] is None and user['desktop']['modelo_desktop'] is None:
        user["desktop"] = None
    
    if user['no_break']['modelo'] is None and user['no_break']['num_serie'] is None:
        user["no_break"] = None
    
    if user['headset']['modelo_headset'] is None and user['headset']['num_serie_headset'] is None:
        user["headset"] = None
    
    if user['celular']['modelo_cel'] is None and user['celular']['imei_celular'] is None:
        user["celular"] = None