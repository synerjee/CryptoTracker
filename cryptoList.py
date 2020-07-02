import urllib.request
import json

class CryptoList:
    def __init__(self):
        id = ["bitcoin","ethereum","ripple","bitcoin-cash","tether","litecoin","eos",
              "cardano","dogecoin","binancecoin", "tezos", "chainlink","stellar",
              "monero", "usd-coin", "tron", "neo", "dash", "huobi-token", "cosmos"]
        url = "https://api.coingecko.com/api/v3/coins/list"
        cList = json.loads(urllib.request.urlopen(url).read())
        self.comboBoxList = []
        self.cryptoDict = {}

        for i in range(len(cList)):
            if (cList[i]["id"] in id):
                self.comboBoxList.append(cList[i]["name"]+" - "+cList[i]["symbol"].upper())
                self.cryptoDict[cList[i]["name"]+" - "+cList[i]["symbol"].upper()] = cList[i]["id"]

    def getComboBoxList(self):
        return self.comboBoxList

    def getCryptoDict(self):
        return self.cryptoDict
