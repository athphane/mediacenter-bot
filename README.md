# Media Center Bot
A Telegram Bot to take control of your Media Center, built with [Pyrogram](https://github.com/pyrogram/pyrogram)

I assume you will read this whole README.md file before continuing.

### Development in progress.

## Requirements
You're gonna need to get the following programs and services either installed on your server
or signed up for. You must do all. It is a cardinal sin if you don't.

* `virtualenv` installed so that the packages don't interfere with other system packages. 
* [MongoDB](https://www.mongodb.com) on your server or a free server from
[MongoDB Atlas](https://www.mongodb.com/cloud/atlas). Installation instructions are out of 
scope for this README.

## Installing
#### One Click Deploy

There is no one click deploy.. It was all a ruse. You have to deploy like how I deploy it...

#### The way I deploy
```bash
git clone https://github.com/athphane/mediacenter-bot.git
cd mediacenter-bot
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
python -m mediacenter.
```


## Credits, and Thanks to
* [Dan](https://t.me/haskell) for his [Pyrogram Library](https://github.com/pyrogram/pyrogram)
