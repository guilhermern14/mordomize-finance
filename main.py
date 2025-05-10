# -*- coding: utf-8 -*-
from flask import Flask, request  
from twilio.twiml.messaging_response import MessagingResponse  

app = Flask(__name__)  

@app.route("/whatsapp", methods=['POST'])  
def whatsapp_bot():  
    msg = request.form.get('Body', '').lower()  
    resp = MessagingResponse()  
    
    if "#saldo" in msg:  
        resp.message("Seu saldo é R$ 1000,00")  
    elif "#ajuda" in msg:  
        resp.message("Comandos: #saldo, #gastar [valor] [categoria]")  
    
    return str(resp)  

if __name__ == "__main__":  
    app.run(debug=True)  
