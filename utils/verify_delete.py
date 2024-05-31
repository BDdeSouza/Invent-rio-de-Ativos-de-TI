def verify_delete_user(user):
    
    print(user["notebook"])
    if user["notebook"] is True:
        return False
    
    if user["monitor_1"] is True:
        return False
    
    if user["monitor_2"] is True:
        return False
    
    if user["teclado"] is True:
        return False
    
    if user["mouse"] is True:
        return False
    
    if user["desktop"] is True:
        return False
    
    if user["no_break"] is True:
        return False
    
    if user["headset"] is True:
        return False
    
    if user["celular"] is True:
        return False
    
    if user["acessorios"] is True:
        return False
    
    if user["suporte_notebook"] is True:
        return False
    
    if user["mouse_pad"] is True:
        return False
    
    return True
    