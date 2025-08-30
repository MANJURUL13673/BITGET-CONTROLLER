import json
import bitget.bitget_api as bitgetApi

from bitget.exceptions import BitgetAPIException

class BitgetConn:
    
    def __init__(self):
        self.load_config()
    
    def load_config(self):
        try:
            with open('config.json') as config_file:
                config = json.load(config_file)
                self.api_key = config["api_key"]
                self.api_secret = config["api_secret"]
                self.passphrase = config["passphrase"]
        except FileNotFoundError:
            print("Config file not found.")
        except json.JSONDecodeError:
            print("Error decoding JSON from config file.")
        except Exception as e:
            print(f"An error occurred: {e}")

    # initial connection
    def Connect(self):
        try:
            self.client = bitgetApi.BitgetApi(self.api_key, self.api_secret, self.passphrase)
            userInfo = self.client.get("/api/v2/spot/account/info", {})
            print("Connected to Bitget API.")
            return True
        except BitgetAPIException as e:
            print(f"Bitget API error occurred: {e}")
            return False
        except Exception as e:
            print(f"Failed to connect to Bitget API: {e}")
            return False
    
    # frequent test of connection
    def APITest(self, params):
        try:
            #symbols = self.client.get("/api/v2/mix/market/symbols", {})
            #params = {"symbol": "ETHUSDT", "productType": "USDT-FUTURES"}
            toUSDT = self.client.get("/api/v2/mix/market/ticker", params)
            #toUSDT = self.client.get("/fapi/v1/ticker/24hr", params)
            return True, toUSDT["data"][0]["lastPr"]
        except BitgetAPIException as e:
            print(f"Bitget API error occurred: {e}")
            return False, 0
        except Exception as e:
            print(f"Failed to connect to Bitget API: {e}")
            return False, 0
    
    # Buy/Sell instantly with/without auto profit
    def PlaceOrder(self, params):
        try:
            order = self.client.post("/api/v2/mix/order/place-order", params)
            print(order)
            return True, order
        except BitgetAPIException as e:
            print(f"Bitget API error occurred: {e}")
            return False, str(e)
        except Exception as e:
            print(f"Failed to place buy order: {e}")
            return False, str(e)
