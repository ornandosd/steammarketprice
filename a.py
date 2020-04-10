import urllib.request, json, urllib.error
import enum
import time
class Exterior():
  ST = "StatTrak%E2%84%A2 "
  FN = " (Factory New)"
  MW = " (Minimal Wear)"
  FT = " (Field-Tested)"
  WW = " (Well-Worn)"
  BS = " (Battle-Scarred)"
  SOUVENIR = "Souvenir "
class AppId(enum.Enum):
  CSGO = 730
  TF2 = 440
  DOTA2 = 570
  PUBG = 578080
  H1Z1 = 433850
  UNTURNED = 304930
  RUST = 252490
class Currency(enum.Enum):
  USD = 1 # United States Dollars
  UKP = 2 # United Kingdom Pounds
  EUR = 3 # European Euros
  CHF = 4 # Swiss Franc
  RUB = 5 # Russian Roubles
  POL = 6 # Polish złoty 
  BZL = 7 # Brazilian real
  JAP = 8 # Japanese Yen
  SWD = 9 # Swedish Krona
  IND = 10 # Indonesian Rupiah
  MAL = 11 # Malaysian Ringgit
class MarketItem():
  sucess = True
  lowest_price = ""
  median_price = ""
  name = ""
  volume = ""
  
def GetMarketItem(appid, name, currency = Currency.IND.value): 
  Item = MarketItem()
  name = name.replace(" ", "+")
  strdat = ""

  try:
    url = urllib.request.urlopen("http://steamcommunity.com/market/priceoverview/?appid=%s&currency=%s&market_hash_name=" % (appid, currency) + name)
    data = json.loads(url.read().decode())
    Item.name = name.replace("+", " ").replace("StatTrak%E2%84%A2 ", "StatTrak ")
    strdat = str(data)
    lowprc = data['lowest_price'].replace(" ", "").replace("Rp","")
    medprc = data['median_price'].replace(" ", "").replace("Rp","")
    volume = data['volume']
    lowprc2 = float(lowprc)
    lowprc3 = int(lowprc2)
    medprc2 = float(medprc)
    medprc3 = int(medprc2)
    profitprc =(lowprc2 - medprc2)
    profitprc2 = int(profitprc)
    profitprc3 = str(profitprc2)
    profitprcent = ((lowprc2-medprc2)/medprc2)*100
    #profitprcent = (float(lowprc2)/float(medprc2))*100
    profitprcent2 = (str(profitprcent))
    recommended_price = (lowprc3 / 100)*20
    reccc = lowprc3 - recommended_price
    recommended_price2 = str(reccc)
    fullurl = ("https://steamcommunity.com/market/listings/%s/" % (appid)+ name)
    fullurl2 = (fullurl.replace("+","%20").replace("|","%7C").replace("(","%28").replace(")","%29"))
    
    
    print(Item.name, ":")
    print("URL       =",fullurl2)
    print("Lowest    = "+data['lowest_price'])
    print("Median    = "+data['median_price'])
    print("Volume    = "+data['volume']+" / Day")

    
  except urllib.error.URLError as e:
    print("ERROR: %s" % e.reason)
    return MarketItem()
  if (strdat.find("success': True") != -1):
    Item.sucess = True
    if (strdat.find('median_price') != -1):
      Item.median_price = data['median_price']
    if (strdat.find('lowest_price') != -1):
      Item.lowest_price = data['lowest_price']
    if (strdat.find('volume') != -1):
      Item.volume = data['volume']
    if  lowprc > medprc:
      print("Profit    = Rp",profitprc3, "Atau",profitprcent2[0:3], "%")
      print("Rec Price = Rp",recommended_price2)
    else:
      print("Tidak Profit")
    if (profitprcent) > 10:
      print("Sangad Profit")
    else:
      pass
  return Item


def PrintMarketItem(it, volume = True):
  #if (len(it.name) > 0):
    #print(it.name + ": ")
  #if (len(it.lowest_price) > 0):
    #print("Lowest    = " + it.lowest_price)
  #if (len(it.median_price) > 0):
    #print("Median    = " + it.median_price)
  #if (len(it.volume) > 0):
    #print("Volume    = " + it.volume + " / Hari")
  #else:
    pass

print("Recommended price = 5% instant profit when u sell again in lowest price")
nama_item = input("Masukkan nama item : ")
pemanis = ("<-------------------------------------------------------------------------------------------------------->")
# - # - # - # - # - # - # - # - # -# - # - # - # - # - # - # - # - # - #
print(pemanis)
PrintMarketItem(GetMarketItem(AppId.CSGO.value,nama_item+ Exterior.BS))
time.sleep(4)
print(pemanis)
PrintMarketItem(GetMarketItem(AppId.CSGO.value,nama_item+ Exterior.WW))
time.sleep(4)
print(pemanis)
PrintMarketItem(GetMarketItem(AppId.CSGO.value,nama_item+ Exterior.FT))
time.sleep(4)
print(pemanis)
PrintMarketItem(GetMarketItem(AppId.CSGO.value,nama_item+ Exterior.MW))
time.sleep(4)
print(pemanis)
PrintMarketItem(GetMarketItem(AppId.CSGO.value,nama_item+ Exterior.FN))
time.sleep(4)
print(pemanis)
PrintMarketItem(GetMarketItem(AppId.CSGO.value,Exterior.ST+ nama_item+ Exterior.BS))
time.sleep(4)
print(pemanis)
PrintMarketItem(GetMarketItem(AppId.CSGO.value,Exterior.ST+ nama_item+ Exterior.WW))
time.sleep(4)
print(pemanis)
PrintMarketItem(GetMarketItem(AppId.CSGO.value,Exterior.ST+ nama_item+ Exterior.FT))
time.sleep(4)
print(pemanis)
PrintMarketItem(GetMarketItem(AppId.CSGO.value,Exterior.ST+ nama_item+ Exterior.MW))
time.sleep(4)
print(pemanis)
PrintMarketItem(GetMarketItem(AppId.CSGO.value,Exterior.ST+ nama_item+ Exterior.FN))
print(pemanis)
print("Done")