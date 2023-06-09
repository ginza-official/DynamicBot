from apps.getmyid.models import Profile
from telegram import ParseMode, Update, ReplyKeyboardMarkup
from apps.bots_config.functions import User_create_or_update
######adminpanel
from apps.bots_config.models import Admin_bots
from telegram.ext import CommandHandler, ConversationHandler, MessageHandler, Filters, CallbackContext
# ##########################buttons---------------------------

admin_buttons = ReplyKeyboardMarkup([["user_counts", "user_data"], ['bot_admins','user_finder'],['/admin']],
                                    resize_keyboard=True)


def Statistic(Profile):
    count_active = Profile.objects.filter(is_active=True).count()
    count_block = Profile.objects.filter(is_active=False).count()
    count_all = Profile.objects.all().count()
    msg = (f"umumiy hisob : {count_all}\n"
           f"faol foydalanuvchilar soni : {count_active}\n"
           f"nofaol foydalanuvchilar soni : {count_block}\n")
    return msg


def users_count(update: Update, context: CallbackContext):
    msg = Statistic(Profile)
    update.message.reply_text(msg, reply_markup=admin_buttons)
    return 'adminpanel'

def user_data(update, context):
    msg = ''
    num = 1
    for i in Profile.objects.all():
        msg += f"""{num}. {i.user_id} -> {i.username} -> {i.fistname} -> {i.lastname}\n"""
        num += 1
    update.message.reply_text(msg, reply_markup=admin_buttons)

    return 'adminpanel'


def finder_user_text(update: Update, context: CallbackContext):
    update.message.reply_text(
        'username yoki  id ni  yuboring : \n masalan:   @username yoki @1234567890')

    return 'adminpanel'


def finder_user(update: Update, context: CallbackContext):
    msg = update.message.text
    if msg.startswith('@'):
        msg = msg[1:]
        try:
            user = Profile.objects.get(username=msg)
            msg = f"""{user.user_id} - {user.username} - {user.fistname} - {user.lastname}"""
            update.message.reply_text(msg, reply_markup=admin_buttons)
            return 'adminpanel'
        except:
            try:
                user=Profile.objects.get(user_id=msg)
                msg = f"""{user.user_id} - {user.username} - {user.fistname} - {user.lastname}"""
                update.message.reply_text(msg, reply_markup=admin_buttons)
                return 'adminpanel'
            except:
                msg = 'bunday foydalanuvchi mavjud emas'
                update.message.reply_text(msg, reply_markup=admin_buttons)
                return 'adminpanel'



def bot_admins(update: Update, context: CallbackContext):
    msg = ''
    num = 1
    for i in Admin_bots.objects.filter(bot__name='getmyid').all():
        bots = ''
        for j in i.bot.all():
            bots += f""" --{j.name}"""
        msg += f"""{num}. {i.telegram_id} ->  name: {i.name} -> status: {i.status} -->  his bots:  {bots}\n"""
        num += 1
    update.message.reply_text(msg, reply_markup=admin_buttons)
    return 'adminpanel'





list_admin = [


    MessageHandler(Filters.regex('^(' + 'user_counts' + ')$'), users_count),
    MessageHandler(Filters.regex('^(' + 'user_data' + ')$'), user_data),
    MessageHandler(Filters.regex('^(' + 'user_finder' + ')$'), finder_user_text),
    MessageHandler(Filters.regex('^(' + 'bot_admins' + ')$'), bot_admins),
    MessageHandler(Filters.regex(r'@[\w]+.*'), finder_user),



]


#######################


button = ReplyKeyboardMarkup([["GetMyID"]], resize_keyboard=True)


def start(update, context):
    user = update.effective_user
    User_create_or_update(user, Profile)

    id = update.effective_user.id
    if Admin_bots.objects.filter(bot__name='getmyid').filter(telegram_id=id).exists():
        update.message.reply_text(f"""Hello Admin""")
        update.message.reply_text(f""" 
        🖐️Hello {user.username} 
        ✅ Your id :  {user.id}
        ✅ Current message id :  {update.message.message_id}
        ✅ Update id : {update.update_id}
        ✅ Chat id  : {update.message.chat_id}
        ✅ From user id :  {update.message.from_user.id}
        ✅ https://t.me/{user.username}"
            """, reply_markup=admin_buttons, parse_mode=ParseMode.HTML)

        return 'adminpanel'
    else:
        update.message.reply_text(f""" 
    🖐️Hello {user.username} 
    ✅ Your id :  {user.id}
    ✅ Current message id :  {update.message.message_id}
    ✅ Update id : {update.update_id}
    ✅ Chat id  : {update.message.chat_id}
    ✅ From user id :  {update.message.from_user.id}
    ✅ https://t.me/{user.username}"
        """, reply_markup=button, parse_mode=ParseMode.HTML)

        return 'bot'


conv_handler = ConversationHandler(
    entry_points=[
        CommandHandler('start', start),
        CommandHandler('admin', start),
        MessageHandler(Filters.regex('^GetMyID$'), start),

    ],
    states={

        'adminpanel': list_admin,
        'bot': [

            MessageHandler(Filters.text, start),
        ],

    },
    fallbacks=[

        MessageHandler(Filters.all, start),

    ]
)
