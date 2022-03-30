from telethon import TelegramClient, events, functions, types
from telethon.tl.functions.contacts import ResolveUsernameRequest
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.custom import Button
import json
from urllib.request import urlopen 
from urllib.parse import urlencode
from LiteSQL import lsql
from time import time

sql = lsql("fecho")
try:
    a = sql.select_data("1", "id")
except:
    sql.create("id, time, anon, podp, podpanon")
    sql.insert_data([(0, 0, 0, 0, "0")], 5)

list_of_user = sql.get_all_data()

for i in range(len(list_of_user)):
    list_of_user[i] = list_of_user[i][0]

client = TelegramClient('fecho', 
    "???",
    "???").start(bot_token="???:???") 

client.parse_mode = 'html'
def command(*args):
    return '|'.join([i for i in [
        rf'^\/({i})+(\@fechoall2bot\w*(_\w+)*)?([ \f\n\r\t\v\u00A0\u2028\u2029].*)?$' for i in args
    ]])

async def new_user(user):
    if user not in list_of_user:
        sql.insert_data([(int(user), 0, 1, 0, str(user))], 5)
        list_of_user.append(user)

async def sender1(i, ms, inline):
    await client.send_message(i, ms, buttons=inline)

async def sender2(i, ms, inline):
    await client.send_message(i, ms)

class Telegraph:
    def make_request(method, **params):
        url = 'https://api.telegra.ph/' + method
        params = {k: v if isinstance(v, str) else json.dumps(v) for k, v in params.items()}
        r = json.loads(urlopen(url + '?' + urlencode(params)).read())
        if not r['ok']:
            raise ValueError(str(r))
        return r['result']

    def get_access_token(short_name):
        return Telegraph.make_request('createAccount',
            short_name=short_name)['access_token']
            
    def create_page(**params):
        return Telegraph.make_request('createPage', **params)

class Bot:
    @client.on(events.NewMessage())
    async def send(event):
        if event.message.from_id != None:
            mfi = event.message.from_id.user_id
        else:
            mfi = event.chat.id
        await new_user(mfi)
        Flag = False
        if event.message.message == "" or event.message.message.split()[0] not in [
"/start@fechoall2bot", "/help@fechoall2bot", "source@fechoall2bot", "/menu@fechoall2bot", "/edit@fechoall2bot", "/nick@fechoall2bot", 
"/start", "/help", "/source", "/menu", "/edit", "/nick"
                                        ] and not event.message.out:
            us = sql.select_data(mfi, "id")[0]
            for i in ['<a href="', "@", "dro4ag", "dr04ag", "dr04ag_bot", "raikirigamebot","https://", "http://", "t.me/", ".com", ".ru", "tg://"]:
                if i in event.message.text.replace(" ","").lower():
                    if us[3] != 0:
                        sql.edit_data("id", mfi, "podp", us[3]-1)
                        break
                    else:
                        await client.send_message(event.chat.id, "У тебя не осталось прав на отправку сообщений с сылками!\n\
купить безлимитное количество отправок сообщений с сылками можно за 30 руб у @Error_mak25")
                        Flag = True
            Flag2 = False
            for i in range(3, len(event.message.message), 3):
                if event.message.message.count(event.message.message[i-3:i]) > 7:
                    Flag2 = True
                    break
            if Flag2 or len(event.message.message) >= 2000:
                await client.send_message(event.chat.id, "Сообщение слишком большое (боллее 2000 символов) или содержит повторяющиеся элементы")
                Flag = True
            if not Flag:
                time1 = time()
                if int(us[1])+3 <= time1 or us[1] == 0:
                    sql.edit_data("id", mfi, "time", time1)
                    inline = []
                    if us[2] == 0:
                        inline.append(Button.inline(f"Autor: {us[4]}".replace("861999825", "ADMIN")))
                    if event.message.is_reply:
                        reply = await event.message.get_reply_message()
                        if len(f"n{reply.message}".encode("utf-8")) <= 64:
                            inline.append(Button.inline(f"{reply.message[:20]}...", f"n{reply.message}"))
                        else:
                            tok = Telegraph.get_access_token("bot")
                            link = Telegraph.create_page(access_token=tok, content=[{"tag": "p", "children": [reply.message]}], title="reply")
                            inline.append(Button.url(f"{reply.message[:20]}...", link["url"]))
                    if inline != []:
                        func = sender1
                    else:
                        func = sender2
                    mess = await client.send_message(event.chat.id, "Ваше сообщение прошло проверку на рекламу и готово к отправке. Отправляем...")
                    t = time()
                    for i in list_of_user:
                        try:
                            await func(i, event.message, inline)
                        except Exception as e:
                            if str(e)[:31] == "Could not find the input entity":
                                list_of_user.pop(list_of_user.index(i))
                                sql.delete_data(i, "id")
                    await mess.edit(f"Ваше сообщение было отправлено {len(list_of_user)} пользователям за {round(time()-t, 2)} секунд!")
                else:
                    await client.send_message(event.chat.id, f"Вы уже отправляли сообщение! Отправить следующее можно через \
{round((3 - time1 + int(us[1])), 2)} секунд(-у).", reply_to=event.message)

    @client.on(events.NewMessage(pattern=command("start", "help")))
    async def start(event):
        await client.send_message(event.chat.id, "Просто отправь мне сообщение\n/source - исходный код бота\n/menu - меню настроек\n/nick _ - поставить ник")

    @client.on(events.CallbackQuery())
    async def callback(event):
        txt = event.data.decode("utf-8")
        user = await event.get_sender()
        await new_user(user.id)
        us = sql.select_data(user.id, "id")[0]
        if txt[0] == "a":
            if us[2] == 1:
                sql.edit_data("id", user.id, "anon", 0)
                await client.send_message(event.chat.id, "Теперь ваши сообщения будут подписываться вашим id")
            else:
                sql.edit_data("id", user.id, "anon", 1)
                await client.send_message(event.chat.id, "Теперь ваши сообщения НЕ будут подписываться вашим id, да вы Анонимус!")
        if txt[0] == "n":
            await event.answer(txt[1:], alert=True)
            
    @client.on(events.NewMessage(pattern=command("source")))
    async def source(event):
        await client.send_message(event.chat.id, "Ссылка на репозиторий - https://gitlab.com/Ma-Mush/echoall")

    @client.on(events.NewMessage(pattern=command("menu")))
    async def menu(event):
        if event.message.from_id != None: 
            mfi = event.message.from_id.user_idr
        else: 
            mfi = event.chat.id
        await new_user(mfi)
        us = sql.select_data(mfi, "id")[0]
        await client.send_message(
            event.chat.id, "Меню настроек пользователя (для изменения - нажмите)",
            buttons=[[Button.inline(f"Вы {'Анонимус' if us[2] == 1 else 'не Анонимус'}", "a")],
            [Button.url(f"У вас {us[3]} доступных сообщений с сылкой (тап - купить безлимит)", "t.me/Error_mak25")]]
        )
    @client.on(events.NewMessage(pattern=command("edit")))
    async def edit(event):
        if event.from_id == 861999825 or event.chat_id == 861999825:
            txt = event.message.message.split()
            sql.edit_data(txt[1], int(txt[2]), txt[3], int(txt[4]))
            await client.send_message(861999825, f"{txt[1]}, {txt[2]}, {txt[3]}, {txt[4]}")

    @client.on(events.NewMessage(pattern=command("nick")))
    async def nick(event):
        if event.message.from_id != None: 
            mfi = event.message.from_id.user_idr
        else: 
            mfi = event.chat.id
        await new_user(mfi)
        mess = event.message.message.split()
        if len(mess) >= 2:
            sql.edit_data("id", mfi, "podpanon", " ".join(mess[1:]))
            await client.send_message(event.chat.id, f"Вы устновили подпись {' '.join(mess[1:])}")

client.run_until_disconnected()
