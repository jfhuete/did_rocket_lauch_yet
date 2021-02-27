FROM shkoliar/ngrok:latest

ARG ngrok_auth_token

RUN ngrok authtoken $ngrok_auth_token

# Execute ngrok bin

CMD /start.sh
