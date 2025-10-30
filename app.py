from flask import Flask, request
import requests
import os

app = Flask(__name__)

# Ambil dari environment (lebih aman dibanding hardcode)
BOT_TOKEN = os.getenv("BOT_TOKEN") or "YOUR_TELEGRAM_BOT_TOKEN"
CHAT_ID = os.getenv("CHAT_ID") or "YOUR_CHAT_ID"

@app.route('/')
def home():
    return "✅ TradingView → Telegram Bot Active"

@app.route('/alert', methods=['POST'])
def alert():
    try:
        data = request.get_json(force=True) or {}
    except Exception:
        data = {}

    # TradingView akan mengirim JSON; ambil 'message' kalau ada
    message = data.get('message', '⚠ TradingView Alert Received')

    # Kirim ke Telegram
    url = f'https://api.telegram.org/bot8336507443:AAE9TYcR85Xgv9p4X6aUBBX1wVZYKJeaMQ8/sendMessage'
    payload = {
        'chat_id': 205477343,
        'text': message,
        'parse_mode': 'HTML'
    }
    resp = requests.post(url, json=payload)

    # Optional: debug kalau gagal
    if resp.status_code != 200:
        return f"Telegram error: {resp.text}", 500

    return "OK", 200

if __name__ == '__main__':
    # Hanya untuk lokal. Di Render pakai gunicorn (Start Command).
    app.run(host='0.0.0.0', port=5000)
