hora = input('Que horas são? ')
hora_int = int(hora)

bom_dia = hora_int >= 0 and hora_int <= 11
boa_tarde = hora_int >= 12 and hora_int <= 17
boa_noite = hora_int >= 18 and hora_int <= 23

if bom_dia is True:
    print('Bom dia')

if boa_tarde is True:
    print('Boa tarde')

if boa_noite is True:
    print('Boa noite')