from twilio.rest import Client
import twilio

conta_sid = "sid"
token = "token"
meu_numero = "numero_celular"
numero_twilio = "coloque_aqui"

cliente = Client(conta_sid, token)

mensagem = """
<Response>
    <Say language="pt-BR">
        Alô, quem está falando?
    </Say>
</Response>
"""

ligacao = cliente.calls.create(
    to=meu_numero,
    from_=numero_twilio,
    twiml=mensagem
)