# ©  - MetaVoid (Moezilla) And Alexa Team For Modification
# Give Credit ❣️Day

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
    alexaai = await message.reply("🤭🤏✌️")
    await asyncio.sleep(1)
    await alexaai.edit("**ʙᴏʜᴀᴛ ᴛᴀɪᴊ ʜᴏ ʀᴇᴘᴏ ᴄʜᴀʜɪʏᴇ**")
    await asyncio.sleep(1)
    await alexaai.edit("**ɪ ᴀᴍ ᴅᴏɪɴɢ ᴍʏ ʟᴏᴠᴇ 💕**")
    await alexaai.delete()
    await asyncio.sleep(2)
    umm = await message.reply_sticker("CAACAgIAAxkBAAEForNjAykaq_efq4Wd-9KZv-nNxJRn3AACIgMAAm2wQgO8x8PfoXC1eCkE")
    await asyncio.sleep(2)
    await message.reply_photo(
        photo=f"https://telegra.ph/file/2fabd1c33e888e0533891.jpg",
        caption=f"""━━━━━━━━━━━━━━━━━━━━━━━━
💥 A ᴘᴏᴡᴇʀғᴜʟ ᴀɪ ʙᴏᴛ
ᴏғ ♻️ ᴅʀ ᴀsᴀᴅ ᴀʟɪ 🔥
━━━━━━━━━━━━━━━━━
ᴅᴀᴛᴀʙᴀsᴇ ʙᴀᴄᴋᴇɴᴅ ʙᴏᴛ ғᴏʀ ᴛɢ...
┏━━━━━━━━━━━━━━━━━┓
┣★ ᴄʀᴇᴀᴛᴇʀ [ᴀsᴀᴅ ᴀʟɪ](https://t.me/Dr_Asad_Ali)
┣★ ʜᴇᴀʀᴛ ᴜs  [ʜᴇᴀʀᴛ ❤️](https://t.me/Give_Me_Heart)
┣★ ʙᴏᴛ ᴜᴏᴅᴀᴛᴇs [ᴏᴜʀ ᴏᴛʜᴇʀ ʙᴏᴛs](https://t.me/AsadSupport)
┣★ ᴀʟᴇxᴀ ғᴇᴅ [ғᴇᴅ ʟᴏɢs](https://t.me/AlexaFed_Logs)
┣★ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ : [ᴄʟɪᴄᴋ ʜᴇʀᴇ](https://github.com/jankarikiduniya/AlexaAiMachineBot)
┣★ ɴᴇᴛᴡᴏʀᴋ [ʀᴏᴄᴋs](https://t.me/Shayri_Music_Lovers)
┗━━━━━━━━━━━━━━━━━┛
💞 
IF HAVE ANY QUESTION THEN CONTACT » TO » MY » [OWNER] @Jankari_Ki_Duniya""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🌼 ᴀʟᴇxᴀ ᴄʜᴀᴛ 💮", url=f"https://t.me/Alexa_Help")]]
        ),
    ) 


@client.on_message(
    filters.command("alive", prefixes=["/", ".", "?", "-"])
    & ~filters.private)
async def start(client, message):
    await message.reply_text(f"**ᴀʟᴇxᴀ ᴀɪ ᴜsᴇʀʙᴏᴛ ғᴏʀ ᴄʜᴀᴛᴛɪɴɢ ɪs ᴡᴏʀᴋɪɴɢ**")
    
    
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
