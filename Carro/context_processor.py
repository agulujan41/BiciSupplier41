def importe_total_carro (request):
    total = 0

    if request.user.is_authenticated:
        if "carro" not in request.session.keys():
            request.session['carro']={}
        for key,value in request.session['carro'].items():
            total = total + (float(value['precio']))

    return {"importe_total_carro":total} 