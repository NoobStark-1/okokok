# Â©  - MetaVoid (Moezilla) And Alexa Team For Modification
# Give Credit â£ï¸Day

from pyrogram import Client, filters
import asyncio
from pyrogram.types import *
from pymongo import MongoClient
import requests
import random
from pyrogram.errors import (
    PeerIdInvalid,
    ChatWriteForbidden
)
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
import os
import re


API_ID = os.environ.get("API_ID", "16869914") 
API_HASH = os.environ.get("API_HASH", "9cf099ff3bd3a365c34f04eeb0a8cfa3") 
SESSION_NAME = os.environ.get("SESSION_NAME","BQA4rWmSkwf3FfayS3FUvDjDaKoioPtBAtjHL5-Ctnanx_hydPQRXBrxQgFlIbVZGvm1ukAn1u2RPJd0oZJwSDwhqmcQODTfi7oSxzJwL7KVjgTQlZ-5VnsBhhd0rrMe5LQ_OKH-g4Oy2pA26nBfN37yptVkprPTUZgcCuXuL0PUmjSSMo0zCUCBeJPGgF_hvPrKTCYPaMIhjqZJczbb4LXCLnUKAs2gpgiwSLvxw1k2C3AexmbKuhC-e1sU356EnyiQJDroQ1wZ7VGhwkje-cbKf0GLWChBdfBCXRZCBRkWEdxbBxyC9rpIaTkP-Pjy6mqjdu3nmG_Yhb2eqhG1GYJ3AAAAATo1jaIA")
MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srv://copyninja101:liyaxlambert*143@cluster0.3qincix.mongodb.net/?retryWrites=true&w=majority")


client = Client(SESSION_NAME, API_ID, API_HASH)


@client.on_message(
    filters.command("repo", prefixes=["/", ".", "?", "-"])
    & ~filters.private)
async def chatbot(client, message):
    await message.delete()
    alexaai = await message.reply("ð¤­ð¤âï¸")
    await asyncio.sleep(1)
    await alexaai.edit("**Êá´Êá´á´ á´á´Éªá´ Êá´ Êá´á´á´ á´Êá´ÊÉªÊá´**")
    await asyncio.sleep(1)
    await alexaai.edit("**Éª á´á´ á´á´ÉªÉ´É¢ á´Ê Êá´á´ á´ ð**")
    await alexaai.delete()
    await asyncio.sleep(2)
    umm = await message.reply_sticker("CAACAgIAAxkBAAEForNjAykaq_efq4Wd-9KZv-nNxJRn3AACIgMAAm2wQgO8x8PfoXC1eCkE")
    await asyncio.sleep(2)
    await message.reply_photo(
        photo=f"https://telegra.ph/file/2fabd1c33e888e0533891.jpg",
        caption=f"""ââââââââââââââââââââââââ
ð¥ A á´á´á´¡á´ÊÒá´Ê á´Éª Êá´á´
á´Ò â»ï¸ á´Ê á´sá´á´ á´ÊÉª ð¥
âââââââââââââââââ
á´á´á´á´Êá´sá´ Êá´á´á´á´É´á´ Êá´á´ Òá´Ê á´É¢...
âââââââââââââââââââ
â£â á´Êá´á´á´á´Ê [á´sá´á´ á´ÊÉª](https://t.me/Dr_Asad_Ali)
â£â Êá´á´Êá´ á´s  [Êá´á´Êá´ â¤ï¸](https://t.me/Give_Me_Heart)
â£â Êá´á´ á´á´á´á´á´á´s [á´á´Ê á´á´Êá´Ê Êá´á´s](https://t.me/AsadSupport)
â£â á´Êá´xá´ Òá´á´ [Òá´á´ Êá´É¢s](https://t.me/AlexaFed_Logs)
â£â sá´á´Êá´á´ á´á´á´á´ : [á´ÊÉªá´á´ Êá´Êá´](https://github.com/jankarikiduniya/AlexaAiMachineBot)
â£â É´á´á´á´¡á´Êá´ [Êá´á´á´s](https://t.me/Shayri_Music_Lovers)
âââââââââââââââââââ
ð 
IF HAVE ANY QUESTION THEN CONTACT Â» TO Â» MY Â» [OWNER] @Jankari_Ki_Duniya""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("ð¼ á´Êá´xá´ á´Êá´á´ ð®", url=f"https://t.me/Alexa_Help")]]
        ),
    ) 


@client.on_message(
    filters.command("alive", prefixes=["/", ".", "?", "-"])
    & ~filters.private)
async def start(client, message):
    await message.reply_text(f"**á´Êá´xá´ á´Éª á´sá´ÊÊá´á´ Òá´Ê á´Êá´á´á´ÉªÉ´É¢ Éªs á´¡á´Êá´ÉªÉ´É¢**")
    
    
@client.on_message(
 (
        filters.text
        | filters.sticker
    )
    & ~filters.private
    & ~filters.me
    & ~filters.bot,
)
async def alexaai(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"]   

   if not message.reply_to_message:
       alexadb = MongoClient(MONGO_URL)
       alexa = alexadb["AlexaDb"]["Alexa"] 
       is_alexa = alexa.find_one({"chat_id": message.chat.id})
       if not is_alexa:
           await client.send_chat_action(message.chat.id, "typing")
           K = []  
           is_chat = chatai.find({"word": message.text})  
           k = chatai.find_one({"word": message.text})      
           if k:               
               for x in is_chat:
                   K.append(x['text'])          
               hey = random.choice(K)
               is_text = chatai.find_one({"text": hey})
               Yo = is_text['check']
               if Yo == "sticker":
                   await message.reply_sticker(f"{hey}")
               if not Yo == "sticker":
                   await message.reply_text(f"{hey}")
   
   if message.reply_to_message:  
       alexadb = MongoClient(MONGO_URL)
       alexa = alexadb["AlexaDb"]["Alexa"] 
       is_alexa = alexa.find_one({"chat_id": message.chat.id})    
       getme = await client.get_me()
       user_id = getme.id                             
       if message.reply_to_message.from_user.id == user_id: 
           if not is_alexa:                   
               await client.send_chat_action(message.chat.id, "typing")
               K = []  
               is_chat = chatai.find({"word": message.text})
               k = chatai.find_one({"word": message.text})      
               if k:       
                   for x in is_chat:
                       K.append(x['text'])
                   hey = random.choice(K)
                   is_text = chatai.find_one({"text": hey})
                   Yo = is_text['check']
                   if Yo == "sticker":
                       await message.reply_sticker(f"{hey}")
                   if not Yo == "sticker":
                       await message.reply_text(f"{hey}")
       if not message.reply_to_message.from_user.id == user_id:          
           if message.sticker:
               is_chat = chatai.find_one({"word": message.reply_to_message.text, "id": message.sticker.file_unique_id})
               if not is_chat:
                   chatai.insert_one({"word": message.reply_to_message.text, "text": message.sticker.file_id, "check": "sticker", "id": message.sticker.file_unique_id})
           if message.text:                 
               is_chat = chatai.find_one({"word": message.reply_to_message.text, "text": message.text})                 
               if not is_chat:
                   chatai.insert_one({"word": message.reply_to_message.text, "text": message.text, "check": "none"})                                                                                                                                               

@client.on_message(
 (
        filters.sticker
        | filters.text
    )
    & ~filters.private
    & ~filters.me
    & ~filters.bot,
)
async def alexastickerai(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"]   

   if not message.reply_to_message:
       alexadb = MongoClient(MONGO_URL)
       alexa = alexadb["AlexaDb"]["Alexa"] 
       is_alexa = alexa.find_one({"chat_id": message.chat.id})
       if not is_alexa:
           await client.send_chat_action(message.chat.id, "typing")
           K = []  
           is_chat = chatai.find({"word": message.sticker.file_unique_id})      
           k = chatai.find_one({"word": message.text})      
           if k:           
               for x in is_chat:
                   K.append(x['text'])
               hey = random.choice(K)
               is_text = chatai.find_one({"text": hey})
               Yo = is_text['check']
               if Yo == "text":
                   await message.reply_text(f"{hey}")
               if not Yo == "text":
                   await message.reply_sticker(f"{hey}")
   
   if message.reply_to_message:
       alexadb = MongoClient(MONGO_URL)
       alexa = alexadb["AlexaDb"]["Alexa"] 
       is_alexa = alexa.find_one({"chat_id": message.chat.id})
       getme = await client.get_me()
       user_id = getme.id
       if message.reply_to_message.from_user.id == user_id: 
           if not is_alexa:                    
               await client.send_chat_action(message.chat.id, "typing")
               K = []  
               is_chat = chatai.find({"word": message.text})
               k = chatai.find_one({"word": message.text})      
               if k:           
                   for x in is_chat:
                       K.append(x['text'])
                   hey = random.choice(K)
                   is_text = chatai.find_one({"text": hey})
                   Yo = is_text['check']
                   if Yo == "text":
                       await message.reply_text(f"{hey}")
                   if not Yo == "text":
                       await message.reply_sticker(f"{hey}")
       if not message.reply_to_message.from_user.id == user_id:          
           if message.text:
               is_chat = chatai.find_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.text})
               if not is_chat:
                   toggle.insert_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.text, "check": "text"})
           if message.sticker:                 
               is_chat = chatai.find_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.sticker.file_id})                 
               if not is_chat:
                   chatai.insert_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.sticker.file_id, "check": "none"})    
              


@client.on_message(
    (
        filters.text
        | filters.sticker
    )
    & filters.private
    & ~filters.me
    & ~filters.bot,
)
async def alexaprivate(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"]
   if not message.reply_to_message: 
       await client.send_chat_action(message.chat.id, "typing")
       K = []  
       is_chat = chatai.find({"word": message.text})                 
       for x in is_chat:
           K.append(x['text'])
       hey = random.choice(K)
       is_text = chatai.find_one({"text": hey})
       Yo = is_text['check']
       if Yo == "sticker":
           await message.reply_sticker(f"{hey}")
       if not Yo == "sticker":
           await message.reply_text(f"{hey}")
   if message.reply_to_message:            
       getme = await client.get_me()
       user_id = getme.id       
       if message.reply_to_message.from_user.id == user_id:                    
           await client.send_chat_action(message.chat.id, "typing")
           K = []  
           is_chat = chatai.find({"word": message.text})                 
           for x in is_chat:
               K.append(x['text'])
           hey = random.choice(K)
           is_text = chatai.find_one({"text": hey})
           Yo = is_text['check']
           if Yo == "sticker":
               await message.reply_sticker(f"{hey}")
           if not Yo == "sticker":
               await message.reply_text(f"{hey}")
                     
@client.on_message(
 (
        filters.sticker
        | filters.text
    )
    & filters.private
    & ~filters.me
    & ~filters.bot,
)
async def alexaprivatesticker(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"] 
   if not message.reply_to_message:
       await client.send_chat_action(message.chat.id, "typing")
       K = []  
       is_chat = chatai.find({"word": message.sticker.file_unique_id})                 
       for x in is_chat:
           K.append(x['text'])
       hey = random.choice(K)
       is_text = chatai.find_one({"text": hey})
       Yo = is_text['check']
       if Yo == "text":
           await message.reply_text(f"{hey}")
       if not Yo == "text":
           await message.reply_sticker(f"{hey}")
   if message.reply_to_message:            
       getme = await client.get_me()
       user_id = getme.id       
       if message.reply_to_message.from_user.id == user_id:                    
           await client.send_chat_action(message.chat.id, "typing")
           K = []  
           is_chat = chatai.find({"word": message.sticker.file_unique_id})                 
           for x in is_chat:
               K.append(x['text'])
           hey = random.choice(K)
           is_text = chatai.find_one({"text": hey})
           Yo = is_text['check']
           if Yo == "text":
               await message.reply_text(f"{hey}")
           if not Yo == "text":
               await message.reply_sticker(f"{hey}")
               

client.run()
