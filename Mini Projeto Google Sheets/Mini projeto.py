from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1RTAiJlh0BRJpeqtFUUqXbWnHx3853RFmfq16CnlT91c'
SAMPLE_RANGE_NAME = 'Página1!A1:D9'


def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """


creds = None
if os.path.exists('token.json'):
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
    with open('token.json', 'w') as token:
        token.write(creds.to_json())

service = build('sheets', 'v4', credentials=creds)

sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range=SAMPLE_RANGE_NAME).execute()
values = result.get('values', [])
if not values:
    print('No data found.')
else:
    print('Conexão Bem sucedida')

linha = 1


def valores(conteudo):
    body = {
        'values': [[conteudo]]
    }
    return service.spreadsheets().values().update(
        spreadsheetId=SAMPLE_SPREADSHEET_ID, range=f'Página1!D{linha}',
        valueInputOption="USER_ENTERED", body=body).execute()


for lista in values:
    if len(lista) < 4:

        if lista[2] == 'Boleto Gerado':
            print('Mensagem Do Boleto Enviada por Email')
            valores('Mensagem do Boleto Enviada')

        elif lista[2] == 'Comprou':
            print('Mensagem Da compra Enviada por Email')
            valores('Compra Finalizada')

        elif lista[2] == 'Sem Saldo':
            print('Mensagem Da falta de Saldo Enviada por Email')
            valores('Mensagem Sem Saldo no Cartão Enviada')

    linha += 1