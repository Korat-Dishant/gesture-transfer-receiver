# import ngrok
# import time
# from dotenv import load_dotenv
# import os

# load_dotenv()


# def listTunnels():
#     listeners = ngrok.get_listeners()
#     print("listeners : " , listeners)

# def tunneling():
# #  listener = ngrok.forward("localhost:8000", authtoken_from_env=True,basic_auth=["username1:password1", "username2:password2"])
#     listener = ngrok.forward("localhost:8000", authtoken=os.getenv("NGROK_AUTHTOKEN") )

#     print(f"Ingress established at: {listener.url()}")

#     time.sleep(60)
#     listTunnels()
#     print("end program")



# if __name__ == "__main__" :
#     tunneling()