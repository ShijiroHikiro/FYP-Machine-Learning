from flask import Flask, render_template, request,jsonify
from flask import send_from_directory
import pickle
import numpy as np
import pandas as pd
import requests
from oauth2client.service_account import ServiceAccountCredentials
import gspread
from datetime import datetime
from googleapiclient.discovery import build


scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive',
]

creds = ServiceAccountCredentials.from_json_keyfile_name("C:\\Users\\Dayah Azmi\\Desktop\\fyp\\projectfyp-388706-b9e079cdbdae.json", scopes=scopes)

file = gspread.authorize(creds)

# Open a specific spreadsheet
workbook = file.open("Data_Rainfall")
sheet = workbook.sheet1

TELEGRAM_API_URL = "https://api.telegram.org/bot5811354859:AAGYbGlIJ74Pg0z_C7w9ln5UTISISWLYans/sendMessage"

bot_token = "5811354859:AAGYbGlIJ74Pg0z_C7w9ln5UTISISWLYans"  # Replace with your Telegram bot token
api_url = f"https://api.telegram.org/bot{bot_token}/setWebhook"

app = Flask (__name__, template_folder='template', static_url_path='/static')

@app.route('/')
def second_page():
    return render_template('second_page.html') 



@app.route('/index')
def index(): 
    
    # Connect to Google Sheets API
    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()

    # Define the sheet ID and range
    sheet_id = '1XfpbylxHKKVsxs1q92NneDdhD62UuJ6D2LrGR6XoeKg'
    range_name = 'DataRainfall!A1:D87'

    # Retrieve data from Google Sheets
    result = sheet.values().get(spreadsheetId=sheet_id, range=range_name).execute()
    values = result.get('values', [])

    if not values:
        print('No data found.')
        data = []
    else:
        # Convert the retrieved data to a list of dictionaries
        headers = values[0]
        rows = values[1:]
        data = [dict(zip(headers, row)) for row in rows]
       
    
    return render_template('index.html', data=data)
    

model = pickle.load(open("model_knn.pickle","rb"))

def send_telegram_message(message):
    telegram_bot_token = '5961538768:AAEv2rWbm-9I54KzvwBX-oozOxS2NpcqV7Y'
    chat_id = '312939398'
    telegram_api_url = f'https://api.telegram.org/bot{telegram_bot_token}/sendMessage'
    data = {
        'chat_id': chat_id,
        'text': message
    }
    response = requests.post(telegram_api_url, data=data)
    if response.status_code != 200:
        print('Failed to send Telegram message')
        


@app.route('/predict', methods=['POST'])
def predict():    
    
    feature = float(request.form['feature1'])   
    year = int(request.form['year'].split('-')[0])
    month = request.form['month']    

    # Connect to Google Sheets API
    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()

    # Define the sheet ID and range
    sheet_id = '1XfpbylxHKKVsxs1q92NneDdhD62UuJ6D2LrGR6XoeKg'     

    # Use the dictionary to get the letter range for the current month    
    range_name = f'DataRainfall!A1:L1'

    # Prepare the data to be inserted
    values = [[year, month, feature]]

    # Insert the data into the sheet
    result = sheet.values().append(
        spreadsheetId=sheet_id,
        range=range_name,
        valueInputOption='USER_ENTERED',
        body={'values': values}
    ).execute()
    
    # Retrieve data from Google Sheet
    client = gspread.authorize(creds)
    sheet = client.open('Data_Rainfall').sheet1
    data = sheet.get_all_records()
    
    if feature >= 60:
        send_telegram_message("Attention! Rainfall data found that it has exceeded the limit that has been set. Please be prepared for the evacuation of people.\n\n"
                              "Perhatian! Data taburan hujan mendapati ia telah melebihi had yang telah ditetapkan. Harap semua pihak bersiap sedia untuk pemindahan rakyat.")
            
    elif feature >= 31 and feature < 60:
        send_telegram_message("Rainfall data indicates a significant increase. Stay vigilant and be prepared for potential flooding.\n \n"
                               "Data taburan hujan menunjukkan peningkatan yang ketara. Tetap berwaspada dan bersiap sedia untuk banjir yang mungkin berlaku.")
                               
    if feature >= 60:
        prediction_text = "Warning! Rainfall has exceeded the limit that has been set, please be prepared."
    else:
             # Create a dummy input with 13 features
        dummy_input = np.zeros(13)
        dummy_input[0] = feature
        
            # Reshape the dummy input to match the expected input shape of the KNN model
        dummy_input = dummy_input.reshape(1, -1)
    
            # Make predictions using the loaded KNN model
        prediction = model.predict(dummy_input)      
    
    
        if prediction[0] == 1:
            prediction_text = "Warning! Rainfall has exceeded 60 millimeters, please be prepared."
        elif feature >= 31 and feature < 60:
            prediction_text = "Potential Flood Alert!"
        else:
            prediction_text = "No Flood Happen"    
            
    return render_template("index.html",  data=data, prediction_text=prediction_text)

@app.route('/third_page')
def third_page():
    return render_template('third_page.html')  

@app.route('/template/<path:path>')
def send_image(path):
    return send_from_directory('template', path)

if __name__== "__main__":
    
    app.run(debug=True)
    