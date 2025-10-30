from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN") or "YOUR_TELEGRAM_BOT_TOKEN"

# List Chat ID (pribadi + grup)
# Isi default: chat kamu + grup kamu
CHAT_IDS = [
    "205477343",       # chat pribadi kamu
    "-1003227274933"   # chat ID grup
]

@app.route('/')
def home():
    return "✅ TradingView → Telegram Bot Active"

@app.route('/alert', methods=['POST'])
def alert():
    data = request.get_json(force=True) or {}
    message = data.get('message', '⚠ TradingView Alert Received')

    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'

    # kirim pesan ke semua chat_id
    for cid in CHAT_IDS:
        payload = {
            'chat_id': cid,
            'text': message,
            'parse_mode': 'HTML'
        }
        requests.post(url, json=payload)

    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

