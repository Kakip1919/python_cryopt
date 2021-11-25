from binance.client import Client


class BinanceAPI:

    def __init__(self):
        api_key = ''
        api_secret = ''

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
