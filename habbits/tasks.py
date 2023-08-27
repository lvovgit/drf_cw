from django.conf import settings
from telebot import TeleBot

from djangoProject6.celery import app
from habbits.models import Habit


@app.task
def send_telegram_message(habit_id):
    habit = Habit.objects.get(id=habit_id)
    bot = TeleBot(settings.TG_BOT_TOKEN)
    message = f"Напоминание о выполнении привычки {habit.action} в {habit.time} в {habit.place}"
    bot.send_message(habit.owner.chat_id, message)


