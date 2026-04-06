import subprocess
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TELEGRAM_TOKEN = "Insira seu Token aqui" #O Token pode ser obtido através do @BotFather no Telegram

def get_cpu_output():
    result = subprocess.run(["cpu"], capture_output=True, text=True)
    return result.stdout

def get_free_output():
    result = subprocess.run(["free", "-h"], capture_output=True, text=True)
    return result.stdout

async def status_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    cpu_out = get_cpu_output()
    free_out = get_free_output()

    message = (
        f"*CPU Info:*\n```\n{cpu_out}\n```\n"
        f"*Memory Usage:*\n```\n{free_out}\n```"
    )
    await update.message.reply_text(message, parse_mode="Markdown")

def main():
    app = Application.builder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("status", status_handler))
    print("Bot running... Press Ctrl+C to stop.")
    app.run_polling()

if __name__ == "__main__":
    main()
