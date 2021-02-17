import os.path
from googleapiclient.discovery import build
from google.oauth2 import service_account


# If modifying these scopes, delete the file token.pickle.


# The ID and range of a sample spreadsheet.


def authentic_sheets():
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    SERVICE_ACCOUNT_FILE = 'credentials.json'
    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    service = build('sheets', 'v4', credentials=creds)
    return service


def update_gsheets(service, sheetrange, value_input_option, value_range_body):
    response = service.spreadsheets().values().update(spreadsheetId=os.getenv('SPREADSHEET_ID'), range=sheetrange,
                                                      valueInputOption=value_input_option,
                                                      body=value_range_body).execute()

    return response


def get_city_list(service):
    range_city = 'prices!A2:A'
    request = service.spreadsheets().values().get(spreadsheetId=os.getenv('SPREADSHEET_ID'),
                                                  range=range_city).execute()
    val = request.get('values', [])  # return empty if no values
    return val

def get_prices_list(service):
    range_city = 'prices!C2:C'
    request = service.spreadsheets().values().get(spreadsheetId=os.getenv('SPREADSHEET_ID'),
                                                  range=range_city, valueRenderOption = "UNFORMATTED_VALUE").execute()
    val = request.get('values', [])  # return empty if no values
    return val