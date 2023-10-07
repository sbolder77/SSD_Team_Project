''''''
import uvicorn

ssl = 'TRUE'

if __name__ == '__main__': 
    if ssl == 'TRUE':
        uvicorn.run("main:app",
                    host="localhost", port=8432, reload=True,
                    ssl_keyfile="localhost+2-key.pem",
                    ssl_certfile="localhost+2.pem")
    else:
        uvicorn.run("main:app",
                    host="localhost", port=8432, reload=True)