from __future__ import print_function
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


# Se estiver modificando esses escopos, exclua o arquivo token.json. Tirar o '.readonly' para poder modificar as planilhas
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

#escolher a planilha que quer conectar e uma pagina/linha para conferir se conectou.
SAMPLE_SPREADSHEET_ID = '1z_7_QHVNttG11AdONLQOBwxIluXs-qiGAciOJDjsPA4' #id da planilha é a parte do meio do link da planilha no google
SAMPLE_RANGE_NAME = 'Página1!A1:C5' #nome da pagina ! celulas da planilha

def main():
    """Mostra o uso básico da Sheets API.
    Imprime valores de uma planilha de amostra.
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

service = build('sheets', 'v4', credentials= creds )

sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range=SAMPLE_RANGE_NAME).execute()
values = result.get('values', [])

if not values:
    print('No data found.')
else:
    print('Conexão Bem sucedida')

# lendo e pegando valores das celulas da pagina marcadas
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                               range=SAMPLE_RANGE_NAME).execute()
values = result.get('values', [])
print(values)

#escrevendo valores na planilha

values = [
            [
                'Uma coisa qualquer '
            ]
        ]
body = {
            'values': values
        }
result = service.spreadsheets().values().update(
    spreadsheetId=SAMPLE_SPREADSHEET_ID, range='Página2!A1',
    valueInputOption="USER_ENTERED", body=body).execute()


#Adicionar um valor no final da tabela
values = [
            [
                'Luiz', 'luiz@gmail.com', 'estagiario'
            ],
    [
        'Pedro','pedro@gmail.com','pleno'
    ]
        ]
body = {
            'values': values
        }
result = service.spreadsheets().values().append(
    spreadsheetId=SAMPLE_SPREADSHEET_ID, range='Página1!A1',
    valueInputOption="USER_ENTERED", body=body).execute()