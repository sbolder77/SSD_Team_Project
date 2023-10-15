#Importing necessary modules
import uvicorn

#Variables SSL 
SSL = 'FALSE'

#Run program
if __name__ == '__main__': 
#Variable equals True
    if SSL == 'TRUE':
        uvicorn.run("main:app",
                    host="localhost", port=8432, reload=True,
                    ssl_keyfile="localhost+2-key.pem",
                    ssl_certfile="localhost+2.pem")
#Varibale equals False
    else:
        uvicorn.run("main:app",
                    host="localhost", port=8432, reload=True)
