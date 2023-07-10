from web3 import Web3
web3 = Web3(web3.HTTPProvider("https://long-sly-shape.bsc-testnet.discover.quiknode.pro/73f269388e8df89527f5a02c864e317a928d444d/"))
print(web3.isConnected)