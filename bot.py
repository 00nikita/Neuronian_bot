import io
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

BOT_TOKEN = "8648705328:AAFbdAt_aULjtXyrKI54tmgwHFkGv6Yme8Y"
SERVER_URL = "https://your-server.com"  # will be used later

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text

    # --- replace this block when server is ready ---
    output = f"Mock response for text: {user_input}"
    # response = requests.post(f"{SERVER_URL}/process-text", json={"data": user_input})
    # output = response.json()["output"]
    # ------------------------------------------------

    await update.message.reply_text(output)

async def handle_document(update: Update, context: ContextTypes.DEFAULT_TYPE):
    doc = update.message.document
    file = await doc.get_file()

    buf = io.BytesIO()
    await file.download_to_memory(buf)
    buf.seek(0)
    buf.name = doc.file_name

    # --- replace this block when server is ready ---
    output = f"Mock response for file: {doc.file_name}"
    # response = requests.post(f"{SERVER_URL}/process-file", files={"file": buf})
    # output = response.json()["output"]
    # ------------------------------------------------

    await update.message.reply_text(output)

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))
    app.add_handler(MessageHandler(filters.Document.ALL, handle_document))
    app.run_polling()