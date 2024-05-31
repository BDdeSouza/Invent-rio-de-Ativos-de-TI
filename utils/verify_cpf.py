def valida_cpf(cpf: str) -> bool:
    cpf = cpf.replace(".", "").replace("-", "")

    if len(cpf) != 11:
        return False

    if cpf == cpf[0] * 11:
        return False

    total = 0
    for i in range(9):
        total += int(cpf[i]) * (10 - i)
    digito_1 = 11 - (total % 11)
    if digito_1 > 9:
        digito_1 = 0

    total = 0
    for i in range(10):
        total += int(cpf[i]) * (11 - i)
    digito_2 = 11 - (total % 11)
    if digito_2 > 9:
        digito_2 = 0

    return cpf[-2:] == f"{digito_1}{digito_2}"
