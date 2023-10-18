"""Importing necessary modules"""
import uvicorn

#Variables SSL
SSL = 'FALSE'
SECURE = 'FALSE'
HOST = 'localhost'
PORT = 8432
RELOAD = True
SSL_KEY_FILE = 'localhost+2-key.pem'
SSL_CERT_FILE = 'localhost+2.pem'

#Run program
if __name__ == '__main__':
    if SECURE == 'TRUE':
        #Variable equals True
        if SSL == 'TRUE':
            uvicorn.run("main:app",
                        host=HOST, port=PORT, reload=RELOAD,
                        ssl_keyfile=SSL_KEY_FILE,
                        ssl_certfile=SSL_CERT_FILE)
        #Varibale equals False
        else:
            uvicorn.run("main:app",
                        host=HOST, port=PORT, reload=RELOAD)
    else:
        uvicorn.run("mainunsecure:app",
                    host=HOST, port=PORT, reload=RELOAD)
