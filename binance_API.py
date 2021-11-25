from binance.client import Client


class BinanceAPI:

    def __init__(self):
        api_key = 'mZdbP1239L6TjscUB0brUNoUM4WMfTTWQ36Q6YNFh2drAs22J0MnJo4LzW3QOEO6'
        api_secret = 'lVPLwgGFUivV9BWY510Roy4rSO91XnaP8zYs9N3FJfJPSkoXIeTwaIzKUgV0DTgw'

        self.client = Client(api_key, api_secret)

    def get_ticker(self, pair):
        try:
            value = self.client.get_ticker(symbol=pair)
            return value
        except Exception as e:
            print('Exception Messege : {}'.format(e))
            return None


def main():
    binance_set = BinanceAPI()
    ticker = binance_set.get_ticker('MBLUSDT')
    print(ticker)
    print(ticker['lastPrice'])


if __name__ == "__main__":
    main()