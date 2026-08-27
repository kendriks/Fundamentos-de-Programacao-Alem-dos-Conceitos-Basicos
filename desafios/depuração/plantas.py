def recomendacion_planta(cuidado):
    if cuidado == 'bajo': #adicionado o segundo =
        print('suculenta')
    elif cuidado == 'medio':
        print('pothos')
    elif cuidado == 'alto': #troca de medio por alto
        print('orquídea')

recomendacion_planta('bajo')
recomendacion_planta('medio')
recomendacion_planta('alto')