from twilio.rest import Client


account_sid = 'Minha Conta'
auth_token = 'Meu Token'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Nao sei oq enviar",
                     from_='+13136376988',
                     to='Telefone'
                 )

print(message.sid)
