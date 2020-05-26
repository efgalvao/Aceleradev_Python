from datetime import datetime

def duracao_chamada(registro):
    """ Função para calcular o tempo da chamada utilizando as timestamps do arquivo records."""
    inicio = datetime.fromtimestamp(registro["start"])
    fim = datetime.fromtimestamp(registro["end"])
    limite1 = datetime.strptime("22:00:00", "%H:%M:%S")
    limite2 = datetime.strptime("06:00:00", "%H:%M:%S")
    if inicio.hour >= limite1.hour and inicio.minute >= 0 :
        inicio = inicio.replace(hour=6, minute=00, second = 00)
    elif inicio.hour <= limite2.hour:
        inicio = inicio.replace(hour=6, minute=00, second = 00)
    if fim.hour >= limite1.hour and fim.minute >= 0:
        fim = fim.replace(hour=22, minute=00, second = 00)
    elif fim.hour <= limite2.hour:
        fim = fim.replace(hour=6, minute=00, second = 00)
    duracao = fim - inicio
    duracaototal = (int(duracao.seconds) // 60)
    return duracaototal




def main(records):
    """Função que cria a lista de telefones e valor total com o auxílio de outras funções."""
    conta = []
    for i in records:
        x = {}
        print(type(i), "aqui")
        duracao = duracao_chamada(i)
        custo = round((duracao * 0.09) + 0.36, 2)
        x["source"] = i["source"]
        x["total"] = custo
        check(x, custo, conta)
    return conta

def check(source, custo, conta):
    """" Função para adicionar valores a números de origem já cadastrados."""
    for dic in conta:
        if source['source'] in dic.values():
            dic["total"] += custo
            return conta
    conta.append(source)
    return conta




records = [
    {'source': '48-996355555', 'destination': '48-666666666', 'end': 1564610974, 'start': 1564610674},
    {'source': '41-885633788', 'destination': '41-886383097', 'end': 1564506121, 'start': 1564504821},
{'source': '16-36304799', 'destination': '16-982560674', 'end': 1577853254, 'start': 1577846023}

]
print(main(records))
