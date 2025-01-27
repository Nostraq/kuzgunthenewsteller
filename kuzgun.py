from pushbullet import Pushbullet
from telethon import TelegramClient, events

pb = Pushbullet("o.6wcjvUKDy4aSyEyWE2jdGjjl3wmPW2PN") # Pushbullet API anahtarı

# Telegram API bilgileri
api_id = 23187136  # My Telegram'dan aldığın API ID
api_hash = 'd92fdd57c6bd282396872f5a20cf1ddd'  # My Telegram'dan aldığın API Hash
session_name = 'my_session'  # Oturum için rastgele bir isim verebilirsin

# Telegram istemcisini oluştur
client = TelegramClient(session_name, api_id, api_hash)

KEYWORDS = ["kat özel", "katı özel", "katı kombine", "özel oran", "katı / maks"]  # İzlenecek anahtar kelimeler

# Pushbullet ile bildirim gönder
def send_push_notification(message):
    push = pb.push_note("Özel Oran Bulundu!", message)
    print(f"Bildirim Gönderildi: {message}")

# Mesajları dinleme
@client.on(events.NewMessage(chats=["-1001298847594", "-1002162241096", "-1002410897471", "-1002291105468", "-1002402728990", "-1002321250370"]))  # Kanal ID'lerini buraya ekle
async def handle_new_message(event):
    message_text = event.message.message.lower()  # Mesajları küçük harfe çevir
    for keyword in KEYWORDS:
        if keyword in message_text:
            print(f"📢 Anahtar kelime bulundu: {message_text}")
            break  # Bir eşleşme bulduktan sonra devam etmeye gerek yok

# Botun çalıştığını belirten bir mesaj yazdır
print("Bot çalışıyor...")

# Telegram istemcisini başlat
client.start()
