import abc


class Pagamento(abc.ABC):
    _valor = 0
    _status = "Pendente"

    def __init__(self, valor=0):
        self._valor = valor

    def __str__(self):
        return f"Pagamento de R${self._valor}, Status: {self._status}"

    @abc.abstractclassmethod
    def pagar(self):
        pass

    def consultar(
        self,
    ):
        return self._status


class Pix(Pagamento):
    def pagar(self):
        ##BC.PIX(NAEFOIAEF)
        self._status = "Pago na hora com PIX"


class Cartao(Pagamento):
    def pagar(self):
        # CIELO.PAGAR(VALOR, *(!@*(!@#)))
        self._status = "PAGO"
        # RETURN TRUE


class Boleto(Pagamento):
    def pagar(self):
        # ITAU.GERABOLETO(IOAHEFAE)
        self._status = "Aguardando boleto ser pago (d+1)"
        # erturn URL_BOLETO


pedidos = list[(int, Pagamento, str)]
bol = Boleto(100)  # (Ir no banco) vai gerar um URL pra pagamento
cc = Cartao(
    120
)  # (Operadora, VISA< Master)vai fazer um pagamento na hora, caso reprovado, codigos retornarao
pix = Pix(200)  # (BC) pagamento vai instantaneamente, caso algum problema retorno

pedido1 = (100, bol, bol._status)
pedido2 = (101, cc, cc._status)
pedido3 = (102, bol, bol._status)
pedido4 = (103, cc, cc._status)
pedido5 = (104, bol, bol._status)
pedido6 = (105, cc, cc._status)
pedido7 = (106, bol, bol._status)
pedido8 = (107, pix, cc._status)

pedidos = [pedido1, pedido2, pedido3, pedido4, pedido5, pedido6, pedido7, pedido8]

for pedido in pedidos:
    pedido[1].pagar()
    print(pedido[1])
