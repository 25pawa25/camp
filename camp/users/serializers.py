from rest_framework import serializers
from .models import *
import telebot

bot = telebot.TeleBot('')

@bot.message_handler()
def send_telegram(data):
    channel_id = ""

    if data.get('fio'):
        text = f'ФИО: {data.get("fio")}\n' \
               f'Телефон: {data.get("phone")}\n' \
               f'Класс: {data.get("form")}'

    else:
        text = f'Телефон: {data.get("phone")}'

    bot.send_message(channel_id, text)


class UserRegistrationSerializer(serializers.ModelSerializer):
    phone = PhoneNumberField()

    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        send_telegram(validated_data)
        user = User.objects.create(**validated_data)
        return user


class FeedBackSerializer(serializers.ModelSerializer):
    phone = PhoneNumberField()

    class Meta:
        model = Feedback
        fields = '__all__'

    def create(self, validated_data):
        send_telegram(validated_data)
        feedback = Feedback.objects.create(**validated_data)
        return feedback
