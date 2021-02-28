# Did The Rocket Launch Yet?

![Rocket launch](media/rocketLaunch.jpg)

## Description
This app is a bot for telegram that show images of a rocket launching and ask if
the rocket is launched yet, the user can answer yes or not according if the
rocket is launched in the image or not. The purpouse of this bot is find the
pinpoint when the rocket is launched.

## Dependencies
  1. [Docker](https://docs.docker.com/engine/install/ubuntu/)
  2. [Docker Compose](https://docs.docker.com/compose/install/)
  2. [Ngrok](https://ngrok.com/) account
  3. Telegram account (You can create one with Telegram mobile app)

## Create accounts and get tokens

If you have a Telegram and Ngrok token you can skip this step

### What I have to do in Telegram

You have two ways to use the app:
  1. Use the created bot whose username is _@DidRocketLaunchYet_bot_
  2. Create a new bot in Telegram

#### Create New bot in Telegram

To create new bot in telegram you have to follow the next steps:

  1. Start conversation with *@botfather*, it reply you with a lot of commands
     that you can write it.
  2. You have to write <span style="color: cornflowerblue">/newbot</span>.
  3. *@BotFather* will ask you the name of your bot (the name not the username).
  4. Next *@BotFather* will ask you what is the username of your both
  5. when you have answered the questions, *@BotFather* will reply with a url
     where you can to find your bot an the most important, your access token.
  6. You have to copy this token and stored it in a safetly location. This token
     will be used next to connect the backend with the Telegram API.

Now you have created your bot and you have an access token with connect it with
the backend.

Optionally you can configure your bot with more info:
  * Add description <span style="color: cornflowerblue">/setdescription</span>
  * Add a profile picture <span style="color: cornflowerblue">/setuserpic</span>
  * Add about info <span style="color: cornflowerblue">/setabouttext</span>

### What I have to do in Ngrok
  1. First you have to be registered in [ngrok](https://ngrok.com/).
  2. When you are logged you can to view the
     [nrock token](https://dashboard.ngrok.com/auth/your-authtoken) in the
     Authentication/Your Authtoken section.
  3. You have to copy this token and stored it in a safetly location. This token
     will be used next to connect the backend with the Telegram API.

## Config app

You have to create a **private-env** file inside private folder.
This file must contain the next environment variables:
  * **TELEGRAM_TOKEN:** You have to set this variable with the token provided
    by *@BotFather* when you create the Telegram bot
  * **NGROK_AUTH_TOKEN**: This environment variable will be setted with the
    auth token provided in Authtoken section of ngrok web page.

You have an example of this file in **./private/private-env.example**

## Build app

Before launch the app you have to build the docker images. Is important do this
launching the next script:

  > ./build.sh

## Launch app

If you have followed all the steps, you are ready to start the application. To
do it you have to run the next command:

  > docker-compose up
