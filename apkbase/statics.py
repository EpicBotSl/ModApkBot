@Client.on_message(filters.regex(pattern="📊 Statistics"))   
async def startprivate(bot, message):
    splatform = platform.system()
    platform_release = platform.release()
    platform_version = platform.version()
    architecture = platform.machine()
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(socket.gethostname())
    mac_address = ":".join(re.findall("..", "%012x" % uuid.getnode()))
    processor = platform.processor()
    ram = humanbytes(round(psutil.virtual_memory().total))
    cpu_freq = psutil.cpu_freq().current
    if cpu_freq >= 1000:
        cpu_freq = f"{round(cpu_freq / 1000, 2)}GHz"
    else:
        cpu_freq = f"{round(cpu_freq, 2)}MHz"
    du = psutil.disk_usage(bot.workdir)
    psutil.disk_io_counters()
    disk = f"{humanbytes(du.used)} / {humanbytes(du.total)} " f"({du.percent}%)"
    cpu_len = len(psutil.Process().cpu_affinity())
    countb = await db.total_users_count()
    countb = await db.total_users_count()
    count = await bot.get_chat_members_count(-1001210985373)
    counta = await bot.get_chat_members_count(-1001759991131)
    text=f"""**Bot Advanced Statistics 📊**
** 👥Members Counts in Our channel:**
◉──────────────────────────────────◉
 **MemeHub Telegram 🇱🇰  Users** : `{count}`
 **⚜️MemeHub Family⚜️ (Admins)**   : `{counta}`
 **ᴍᴇᴍᴇʜᴜʙ ᴏᴍғғɪᴄɪᴀʟ ʙᴏᴍᴛ 『🇱🇰』 Users** : `{countb}`
◉──────────────────────────────────◉
