from dataclasses import dataclass

@dataclass
class CryptoStatement:
    """Class for keeping track of an item in inventory."""
    buy_or_sell: str
    crypto_name: str
    price_per_coin: float = 0
    quantity: float = 0


class __main__:
    crypto_sum = []
    count = 0
    net_profit = 0
    with open("file.txt") as fp:
        while True:
            count = count+1
            line = fp.readline()
            if not line:
                break

            x = line.split()
            crypto_sum.append(CryptoStatement(str(x[0]),str(x[1]),float(x[2]),float(x[3])))
            length = len(crypto_sum)
            if(crypto_sum[-1].buy_or_sell == 'S'):
                crypto_indices = []
                b_crypto_sum = 0
                for i in range(len(crypto_sum)-1):
                    if crypto_sum[i].crypto_name == crypto_sum[-1].crypto_name and crypto_sum[i].buy_or_sell == 'B':
                        crypto_indices.append(i)
                        b_crypto_sum = b_crypto_sum + crypto_sum[i].quantity
                if (b_crypto_sum-crypto_sum[-1].quantity<0):
                    print('error')
                    exit()
                else:
                    for j in range(len(crypto_indices)):
                        index = crypto_indices[j]
                        quantity_sum = crypto_sum[-1].quantity-crypto_sum[index].quantity
                        net_profit = net_profit+ (crypto_sum[index].price_per_coin-crypto_sum[i].price_per_coin)*crypto_sum[-1].quantity
                        crypto_sum[index].quantity = 0
                        crypto_sum[-1].quantity = quantity_sum
        print(net_profit)