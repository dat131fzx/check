import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Lấy full_name để giữ đúng tên người dùng
    user_name = update.effective_user.full_name

    # Định dạng bằng thẻ HTML
    welcome_message = (
        f"👋 Welcome, <b>{user_name}</b>, to our verification service!\n\n"
        "🤖 <b>Official Bot:</b> <code>@auth_ccv_bot</code>\n"
        "🟢 <b>Status:</b> Online 24/7\n\n"
        "📌 <b>Main Features:</b>\n"
        " 🟢 Automated system checking\n"
        " ⚡️ High-speed and accurate verification\n"
        " 🔒 100% Secure & Automated\n\n"
        "⚠️ <b>SCAM WARNING:</b>\n"
        "Our ONLY official handle is <code>@auth_ccv_bot</code>. "
        "Please beware of impostors and fake accounts!\n\n"
        "💡 Type /help to see the list of supported commands."
    )

    # Gửi tin nhắn với parse_mode="HTML"
    await update.message.reply_text(welcome_message, parse_mode="HTML")

def main() -> None:
    TOKEN = "8702559788:AAGQYEbQmxxfmahg-pETQsEeUoEK5vLLXeg"
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.run_polling()

if __name__ == "__main__":
    main()