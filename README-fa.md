<p align="center">
  <a href="https://github.com/gfwfuckers/marzgosha" target="_blank" rel="noopener noreferrer">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://github.com/Gozargah/Marzban-docs/raw/master/screenshots/logo-dark.png">
      <img width="160" height="160" src="https://github.com/Gozargah/Marzban-docs/raw/master/screenshots/logo-light.png">
    </picture>
  </a>
</p>

<h1 align="center"/>مرزگشا</h1>

<p align="center">
     راه حل یکپارچه برای مدیریت پروتکل های مختلف. قدرت گرفته از <a href="https://github.com/XTLS/Xray-core">Xray</a>
</p>

<br/>
<p align="center">
    <a href="#">
        <img src="https://img.shields.io/github/actions/workflow/status/gfwfuckers/marzgosha/build.yml?style=flat-square" />
    </a>
    <a href="https://hub.docker.com/r/gfwfuckers/marzgosha" target="_blank">
        <img src="https://img.shields.io/docker/pulls/gfwfuckers/marzgosha?style=flat-square&logo=docker" />
    </a>
    <a href="#">
        <img src="https://img.shields.io/github/license/gfwfuckers/marzgosha?style=flat-square" />
    </a>
   <a href="#">
        <img src="https://img.shields.io/badge/twitter-commiunity-blue?style=flat-square&logo=twitter" />
    </a>
    <a href="#">
        <img src="https://img.shields.io/github/stars/gfwfuckers/marzgosha?style=social" />
    </a>
</p>

<p align="center">
	<a href="./README.md">
	English
	</a>
	/
	<a href="./README-fa.md">
	فارسی
	</a>
  /
  <a href="./README-zh-cn.md">
	简体中文
	</a>
   /
  <a href="./README-ru.md">
 Русский
 </a>
</p>

<p align="center">
  <a href="https://github.com/gfwfuckers/marzgosha" target="_blank" rel="noopener noreferrer" >
    <img src="https://github.com/Gozargah/Marzban-docs/raw/master/screenshots/preview.png" alt="Elk screenshots" width="600" height="auto">
  </a>
</p>

## فهرست مطالب

- [بررسی اجمالی](#بررسی-اجمالی)
<<<<<<< HEAD
  - [چرا مرزگشا؟](#چرا-مرزگشا)
=======
  - [چرا مرزبان؟](#چرا-مرزبان)
>>>>>>> 6b59661 (Bump version to v0.5.0)
    - [امکانات](#امکانات)
- [راهنمای نصب](#راهنمای-نصب)
- [تنظیمات](#تنظیمات)
- [استفاده از API](#استفاده-از-api)
- [پشتیبان گیری از مرزگشا](#پشتیبان-گیری-از-مرزگشا)
- [ربات تلگرام](#ربات-تلگرام)
- [رابط خط فرمان (CLI) مرزگشا](#رابط-خط-فرمان-cli-مرزگشا)
- [ارسال اعلان‌ها به آدرس وبهوک](#ارسال-اعلانها-به-آدرس-وبهوک)
- [کمک مالی](#کمک-مالی)
- [لایسنس](#لایسنس)
- [مشارکت در توسعه](#مشارکت-در-توسعه)

# بررسی اجمالی

مرزگشا یک نرم افزار (وب اپلیکیشن) مدیریت پروکسی است که امکان مدیریت چند صد حساب پروکسی را با قدرت و دسترسی بالا فراهم میکند. مرزگشا از [Xray-core](https://github.com/XTLS/Xray-core) قدرت گرفته و با Python و React پیاده سازی شده است.

## چرا مرزگشا؟

مرزگشا دارای یک رابط کاربری ساده است که قابلیت های زیادی دارد. مرزگشا امکان ایجاد چند نوع پروکسی برای کاربر ها را فراهم میکند بدون اینکه به تنظیمات پیچیده ای نیاز داشته باشید. به کمک رابط کاربری تحت وب مرزگشا، شما میتوانید کاربران را مانیتور، ویرایش و در صورت نیاز، محدود کنید.

### امکانات

- **رابط کاربری تحت وب** آماده
- به صورت **REST API** پیاده سازی شده
- پشتیبانی از پروتکل های **Vmess**, **VLESS**, **Trojan** و **Shadowsocks**
- امکان فعالسازی **چندین پروتکل** برای هر یوزر
- امکان ساخت **چندین کاربر** بر روی یک inbound
- پشتیبانی از **چندین inbound** بر روی **یک port** (به کمک fallbacks)
- محدودیت بر اساس مصرف **ترافیک** و **تاریخ انقضا**
- محدودیت **ترافیک دوره ای** (به عنوان مثال روزانه، هفتگی و غیره)
- پشتیبانی از **Subscription link** سازگار با **V2ray** _(مثل نرم افزار های V2RayNG, OneClick, Nekoray و...)_ و **Clash**
- ساخت **لینک اشتراک گذاری** و **QRcode** به صورت خودکار
- مانیتورینگ منابع سرور و **مصرف ترافیک**
- پشتیبانی از تنظیمات xray
- پشتیبانی از **TLS**
- **ربات تلگرام**
- **رابط خط فرمان (CLI)** داخلی
- قابلیت ایجاد **چندین مدیر** (تکمیل نشده است)

# راهنمای نصب

برای نصب کافیه دستور زیر رو اجرا کنید

```bash
sudo bash -c "$(curl -sL https://github.com/GFWFuckers/MarzGosha-scripts/raw/master/marzgosha.sh)" @ install
```

وقتی نصب تمام شد:

- شما لاگ های مرزگشا رو مشاهده میکنید که می‌توانید با بستن ترمینال یا فشار دادن `Ctrl+C` از آن خارج شوید
- فایل های مرزگشا در پوشه `/opt/marzgosha` قرار می‌گیرند
- فایل تنظیمات در مسیر `/opt/marzgosha/.env` قرار می‌گیرد ([تنظیمات](#تنظیمات) را مشاهده کنید)
- فایل های مهم (اطلاعات) مرزگشا در مسیر `/usr/lib/marzgosha` قرار می‌گیرند
- شما از طریق آدرس `http://YOUR_SERVER_IP:8000/dashboard/` می‌توانید وارد داشبورد مرزگشا شوید (YOUR_SERVER_IP را با آیپی سرور خود عوض کنید)

در مرحله بعد, باید یک ادمین سودو بسازید

```bash
marzgosha cli admin create --sudo
```

تمام! حالا با این اطلاعات می‌توانید وارد مرزگشا شوید

برای مشاهده راهنمای اسکریپت مرزگشا دستور زیر را اجرا کنید

```bash
marzgosha --help
```

اگر مشتاق هستید که مرزگشا رو با پایتون و به صورت دستی اجرا کنید، مراحل زیر را مشاهده کنید

<details markdown="1">
<summary><h3>نصب به صورت دستی (پیچیده)</h3></summary>

لطفا xray را نصب کنید.
شما میتواند به کمک [Xray-install](https://github.com/XTLS/Xray-install) این کار را انجام دهید.

```bash
bash -c "$(curl -L https://github.com/XTLS/Xray-install/raw/main/install-release.sh)" @ install
```

پروژه را clone کنید و dependency ها را نصب کنید. دقت کنید که نسخه پایتون شما Python>=3.8 باشد.

```bash
git clone https://github.com/GFWFuckers/MarzGosha.git
cd MarzGosha
wget -qO- https://bootstrap.pypa.io/get-pip.py | python3 -
python3 -m pip install -r requirements.txt
```

همچنین میتواند از , [Python Virtualenv](https://pypi.org/project/virtualenv/) هم استفاده کنید.

سپس کامند زیر را اجرا کنید تا دیتابیس تنظیم شود.

```bash
alembic upgrade head
```

اگر می خواهید از `marzgosha-cli` استفاده کنید، باید آن را به یک فایل در `$PATH` خود لینک و قابل اجرا (executable) کنید. سپس تکمیل خودکار (auto-completion) آن را نصب کنید:

```bash
sudo ln -s $(pwd)/marzgosha-cli.py /usr/bin/marzgosha-cli
sudo chmod +x /usr/bin/marzgosha-cli
marzgosha-cli completion install
```

حالا یک کپی از `.env.example` با نام `.env` بسازید و با یک ادیتور آن را باز کنید و تنظیمات دلخواه خود را انجام دهید. یه عنوان مثال نام کاربری و رمز عبور را می توانید در این فایل تغییر دهید.

```bash
cp .env.example .env
nano .env
```

> برای اطلاعات بیشتر بخش [تنظیمات](#تنظیمات) را مطالعه کنید.

در انتها, مرزگشا را به کمک دستور زیر اجرا کنید.

```bash
python3 main.py
```

اجرا با استفاده از systemctl در لینوکس

```
systemctl enable /var/lib/marzgosha/marzgosha.service
systemctl start marzgosha
```

اجرا با nginx

```
server {
    listen 443 ssl http2;
    listen [::]:443 ssl http2;
    server_name  example.com;

    ssl_certificate      /etc/letsencrypt/live/example.com/fullchain.pem;
    ssl_certificate_key  /etc/letsencrypt/live/example.com/privkey.pem;

    location ~* /(dashboard|api|docs|redoc|openapi.json) {
        proxy_pass http://0.0.0.0:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```

or

```
server {
    listen 443 ssl http2;
    listen [::]:443 ssl http2;
    server_name  marzgosha.example.com;

    ssl_certificate      /etc/letsencrypt/live/example.com/fullchain.pem;
    ssl_certificate_key  /etc/letsencrypt/live/example.com/privkey.pem;

    location / {
        proxy_pass http://0.0.0.0:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```

به صورت پیشفرض مرزگشا در آدرس `http://localhost:8000/dashboard` اجرا میشود. شما میتوانید با تغییر `UVICORN_HOST` و `UVICORN_PORT`، هاست و پورت را تغییر دهید.

</details>

# تنظیمات

> متغیر های زیر در فایل ‍`env` یا `.env` استفاده میشوند. شما می توانید با تعریف و تغییر آن ها، تنظیمات مرزگشا را تغییر دهید.

|                                                                                                                 توضیحات |                                                        متغیر                                                         |
| ----------------------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------------------: |
|                                                                                                      نام کاربری مدیر کل |                                                    SUDO_USERNAME                                                     |
|                                                                                                        رمز عبور مدیر کل |                                                    SUDO_PASSWORD                                                     |
|          آدرس دیتابیس ([بر اساس مستندات SQLAlchemy](https://docs.sqlalchemy.org/en/20/core/engines.html#database-urls)) |                                               SQLALCHEMY_DATABASE_URL                                                |
|                                                              آدرس هاستی که مرزبان روی آن اجرا میشود (پیشفرض: `0.0.0.0`) |                                                     UVICORN_HOST                                                     |
|                                                                      پورتی که مرزبان روی آن اجرا میشود (پیشفرض: `8000`) |                                                     UVICORN_PORT                                                     |
|                                                                               اجرای مرزبان بر روی یک Unix domain socket |                                                     UVICORN_UDS                                                      |
|                                                                              آدرس گواهی SSL به جهت ایمن کردن پنل مرزبان |                                                 UVICORN_SSL_CERTFILE                                                 |
|                                                                                                     آدرس کلید گواهی SSL |                                                 UVICORN_SSL_KEYFILE                                                  |
|                                                                مسیر فایل json تنظیمات xray (پیشفرض: `xray_config.json`) |                                                      XRAY_JSON                                                       |
|                                                                        مسیر باینری xray (پیشفرض: `/usr/local/bin/xray`) |                                                 XRAY_EXECUTABLE_PATH                                                 |
|                                                                   مسیر asset های xray (پیشفرض: `/usr/local/share/xray`) |                                                   XRAY_ASSETS_PATH                                                   |
| پیشوند (یا هاست) آدرس های اشتراکی (زمانی کاربرد دارد که نیاز دارید دامنه subscription link ها با دامنه پنل متفاوت باشد) |                                             XRAY_SUBSCRIPTION_URL_PREFIX                                             |
|                                                                        تگ inboundای که به عنوان fallback استفاده میشود. |                                              XRAY_FALLBACKS_INBOUND_TAG                                              |
|                                                تگ های inbound ای که لازم نیست در کانفیگ های ساخته شده وجود داشته باشند. |                                              XRAY_EXCLUDE_INBOUND_TAGS                                               |
|                                                                               آدرس محل template های شخصی سازی شده کاربر |                                              CUSTOM_TEMPLATES_DIRECTORY                                              |
|                                           تمپلیت مورد استفاده برای تولید کانفیگ های Clash (پیشفرض: `clash/default.yml`) |                                             CLASH_SUBSCRIPTION_TEMPLATE                                              |
|                                                     تمپلیت صفحه اطلاعات اشتراک کاربر (پیشفرض `subscription/index.html`) |                                              SUBSCRIPTION_PAGE_TEMPLATE                                              |
|                                                                             تمپلیت صفحه اول (پیشفرض: `home/index.html`) |                                                  HOME_PAGE_TEMPLATE                                                  |
|                                                       توکن ربات تلگرام (دریافت از [@botfather](https://t.me/botfather)) |                                                  TELEGRAM_API_TOKEN                                                  |
|                                          آیدی عددی ادمین در تلگرام (دریافت از [@userinfobot](https://t.me/userinfobot)) |                                                  TELEGRAM_ADMIN_ID                                                   |
|                                                                                               اجرای ربات از طریق پروکسی |                                                  TELEGRAM_PROXY_URL                                                  |
|                            مدت زمان انقضا توکن دسترسی به پنل مرزبان, `0` به معنای بدون تاریخ انقضا است (پیشفرض: `1440`) |                                           JWT_ACCESS_TOKEN_EXPIRE_MINUTES                                            |
|                                                       فعال سازی داکیومنتیشن به آدرس `/docs` و `/redoc`(پیشفرض: `False`) |                                                         DOCS                                                         |
|                                                                     فعالسازی حالت توسعه (development) (پیشفرض: `False`) |                                                        DEBUG                                                         |
| آدرس webhook که تغییرات حالت یک کاربر به آن ارسال می‌شوند. اگر این متغیر مقدار داشته باشد، ارسال پیام‌ها انجام می‌شوند.    |                                                    WEBHOOK_ADDRESS                                                   |
|                    متغیری که به عنوان `x-webhook-secret` در header ارسال می‌شود. (پیشفرض: `None`)                        |                                                    WEBHOOK_SECRET                                                    |
|                             تعداد دفعاتی که برای ارسال یک پیام، در صورت تشخیص خطا در ارسال تلاش دوباره شود (پیشفرض `3`) |                                          NUMBER_OF_RECURRENT_NOTIFICATIONS                                           |
|                                   مدت زمان بین هر ارسال دوباره پیام در صورت تشخیص خطا در ارسال به ثانیه (پیشفرض: `180`) |                                           RECURRENT_NOTIFICATIONS_TIMEOUT                                            |
|                                    هنگام رسیدن مصرف کاربر به چه درصدی پیام اخطار به آدرس وبهوک ارسال شود (پیشفرض: `80`) |                                             NOTIFY_REACHED_USAGE_PERCENT                                             |
|                                          چند روز مانده به انتهای سرویس پیام اخطار به آدرس وبهوک ارسال شود (پیشفرض: `3`) |                                                   NOTIFY_DAYS_LEFT                                                   |
حذف خودکار کاربران منقضی شده (و بطور اختیاری محدود شده) پس از گذشت این تعداد روز (مقادیر منفی این قابلیت را به طور پیشفرض غیرفعال می کنند. پیشفرض: `-1`) |                                                   USERS_AUTODELETE_DAYS                                                   |
تعیین اینکه کاربران محدودشده شامل حذف خودکار بشوند یا نه |                                                   USER_AUTODELETE_INCLUDE_LIMITED_ACCOUNTS                                 |
| فعال کردن کانفیگ سفارشی JSON برای همه برنامه‌هایی که از آن پشتیبانی می‌کنند (پیش‌فرض: `False`)                                                   | USE_CUSTOM_JSON_DEFAULT |
| فعال کردن کانفیگ سفارشی JSON فقط برای برنامه‌ی V2rayNG (پیش‌فرض: `False`)                                                            | USE_CUSTOM_JSON_FOR_V2RAYNG |
| فعال کردن کانفیگ سفارشی JSON فقط برای برنامه‌ی Streisand (پیش‌فرض: `False`)                                                          | USE_CUSTOM_JSON_FOR_STREISAND |
| فعال کردن کانفیگ سفارشی JSON فقط برای برنامه‌ی V2rayN (پیش‌فرض: `False`)                                                             | USE_CUSTOM_JSON_FOR_V2RAYN |


# استفاده از API

مرزگشا به توسعه دهندگانAPI REST ارائه می دهد. برای مشاهده اسناد API در قالب Swagger UI یا ReDoc، متغیر `DOCS=True` را در تنظیمات خود ست کنید و در مرورگر به مسیر `/docs` و `/redoc` بروید.

# پشتیبان گیری از مرزگشا

بهتر است همیشه از فایل های مرزگشا خود نسخه پشتیبان تهیه کنید تا در صورت خرابی سیستم یا حذف تصادفی اطلاعات از دست نروند. مراحل تهیه نسخه پشتیبان از مرزگشا به شرح زیر است:

1. به طور پیش فرض، تمام فایل های مهم مرزگشا در `/var/lib/marzgosha` ذخیره می شوند (در نسخه داکر). کل پوشه `/var/lib/marzgosha` را در یک مکان پشتیبان مورد نظر خود، مانند هارد دیسک خارجی یا فضای ذخیره سازی ابری کپی کنید.
2. علاوه بر این، مطمئن شوید که از فایل env خود که حاوی متغیرهای تنظیمات شما است و همچنین فایل پیکربندی Xray خود نسخه پشتیبان تهیه کنید.

با انجام این مراحل، می توانید اطمینان حاصل کنید که از تمام فایل ها و داده های مرزگشا خود یک نسخه پشتیبان تهیه کرده اید. به خاطر داشته باشید که نسخه های پشتیبان خود را به طور مرتب به روز کنید تا آنها را به روز نگه دارید.

# ربات تلگرام

مرزگشا دارای یک ربات تلگرام داخلی است که می تواند مدیریت سرور، ایجاد و حذف کاربر و ارسال نوتیفیکیشن را انجام دهد. این ربات را می توان با انجام چند مرحله ساده به راحتی فعال کرد

برای فعال کردن ربات تلگرام:

1. در تنظیمات، متغیر`TELEGRAM_API_TOKEN` را به API TOKEN ربات تلگرام خود تنظیم کنید.
2. همینطور، متغیر`TELEGRAM_ADMIN_ID` را به شناسه عددی حساب تلگرام خود تنظیم کنید. شما می‌توانید شناسه خود را از [@userinfobot](https://t.me/userinfobot) دریافت کنید.

# رابط خط فرمان (CLI) مرزگشا

مرزگشا دارای یک رابط خط فرمان (Command Line Interface / CLI) داخلی است که به مدیران اجازه می دهد با مرزگشا ارتباط مستقیم داشته باشند.

اگر از Docker برای مرزگشا استفاده می کنید، بهتر است از دستور های `docker exec` یا `docker-compose exec` استفاده کنید تا به پوسته (shell) تعاملی کانتینر مرزگشا دسترسی پیدا کنید.

برای مثال، به پوشه ی `docker-compose.yml` مرزگشا بروید و دستور زیر را اجرا کنید:

```bash
$ sudo docker-compose exec -it marzgosha bash
```

رابط خط فرمان (CLI) مرزگشا از طریق دستور `marzgosha-cli` هرکجا در دسترس خواهد بود!

برای کسب اطلاعات بیشتر می توانید [مستندات CLI مرزگشا](./cli/README.md) را مطالعه کنید.

# ارسال اعلان‌ها به آدرس وبهوک

شما می‌توانید آدرسی را برای مرزگشا فراهم کنید تا تغییرات کاربران را به صورت اعلان برای شما ارسال کند.

اعلان‌ها به صورت یک درخواست POST به آدرسی که در `WEBHOOK_ADDRESS` فراهم شده به همراه مقدار تعیین شده در `WEBHOOK_SECRET` به عنوان `x-webhook-secret` در header درخواست ارسال می‌شوند.

نمونه‌ای از درخواست ارسال شده توسط مرزگشا:

```
Headers:
Host: 0.0.0.0:9000
User-Agent: python-requests/2.28.1
Accept-Encoding: gzip, deflate
Accept: */*
Connection: keep-alive
x-webhook-secret: something-very-very-secret
Content-Length: 107
Content-Type: application/json



Body:
{"username": "marzgosha_test_user", "action": "user_updated", "enqueued_at": 1680506457.636369, "tries": 0}
```

انواع مختلف actionهایی که مرزگشا ارسال می‌کند: `user_created`, `user_updated`, `user_deleted`, `user_limited`, `user_expired`, `user_disabled`, `user_enabled`

# کمک مالی

اگر مرزگشا را برای شما مفید بوده و می‌خواهید از توسعه آن حمایت کنید، می‌توانید در یکی از طریق یکی از شبکه های کریپتو زیر کمک مالی کنید:

- TRON network (TRC20): `TCYj3X9r9s7Fd45LCdFYUdjdg812ogNidf`
- ETH, BNB, MATIC network (ERC20, BEP20): `0x03ebDa025D639Cf46f9926cdd7402253C9De7f38`
- Bitcoin network: `bc1qvm4tstzsyrkvg9yv83ma92d9sydet6sa807ytt`
- Dogecoin network: `DSFfmESjw4whX77kbaGeNx1YTX4ZuhZcsw`
- TON network: `EQCUfz9BqiDHkpJtSJ7XMFec0tSdNmbcgutTC2zuAh_wQtmG`

از حمایت شما متشکرم!

# لایسنس

توسعه یافته شده در [ناشناس!] و منتشر شده تحت لایسنس [AGPL-3.0](./LICENSE).

# مشارکت در توسعه

این ❤️‍🔥 تقدیم به همه‌ی کسایی که در توسعه مرزگشا مشارکت می‌کنند! اگر می‌خواهید مشارکت داشته باشید، لطفاً [دستورالعمل‌های مشارکت](CONTRIBUTING.md) ما را بررسی کنید و در صورت تمایل Pull Request ارسال کنید یا یک Issue باز کنید. همچنین از شما برای پیوستن به گروه [تلگرام](https://t.me/gfwfuckers_marzgosha) ما برای حمایت یا کمک به راهنمایی استقبال می کنیم.

لطفا اگر امکانش رو دارید، با بررسی [لیست کار ها](https://github.com/gfwfuckers/marzgosha/issues) به ما در بهبود مرزگشا کمک کنید. کمک های شما با آغوش باز پذیرفته میشه.
