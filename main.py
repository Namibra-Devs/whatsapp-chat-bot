from wa_automate_socket_client import SocketClient

class WhatsAppBot:
    def __init__(self, server_url, client_token):
        self.client = SocketClient(server_url, client_token)
        self.client.onMessage(self.handle_message)
        print("WhatsApp Bot launched!")

    def handle_message(self, message):
        try:
            data = message["data"]
            text = data["text"]
            number = data["from"]
            
            print("Received message:", text, "from number:", number)
            
            buttons = [{
                "id": "1",
                "text": "Click"
            }]
            
            self.send_response(number, text, buttons)
            
        except KeyError:
            print("Malformed message:", message)
        except Exception as e:
            print("An error occurred:", e)

    def send_response(self, recipient, text, buttons):
        try:
            self.client.sendButtons(recipient, text, buttons, "Title", "Footer")
            self.client.sendText(recipient, "")
            # self.client.sendImage(recipient, image_url, "Image", "Caption")
            # self.client.sendSeen(recipient)
            
            print("Response sent to:", recipient)
            
        except Exception as e:
            print("Failed to send response:", e)

if __name__ == "__main__":
    server_url = 'http://localhost:5340/'
    client_token = 'jl6gAQpTH5H4J7IQiN428pyeIaNkTQXo'
    
    bot = WhatsAppBot(server_url, client_token)
