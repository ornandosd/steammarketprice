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
    lowprc2 = float(lowprc)
    lowprc3 = int(lowprc2)
    medprc = data['median_price'].replace(" ", "").replace("Rp","")
    medprc2 = float(medprc)
    medprc3 = int(medprc2)
    profitprc =(lowprc2 - medprc2)
    profitprc2 = int(profitprc)
    profitprcent = (float(lowprc2)/float(medprc2))*100
    profitprcent2 = (str(profitprcent))
    recommended_price = (medprc3)-((15/100)*medprc3)
    recommended_price2 = str(recommended_price)
    fullurl = ("https://steamcommunity.com/market/listings/%s/" % (appid)+ name)
    fullurl2 = (fullurl.replace("+","%20").replace("|","%7C").replace("(","%28").replace(")","%29"))
    print(Item.name, ":")
    print("URL       =",fullurl2)

    
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
      print("Profit    = Rp", profitprc2, "=",profitprcent2[2:5], "%")          
      print("Rec Price = Rp",recommended_price2)
    else:
      print("Tidak Profit")
  return Item

def PrintMarketItem(it, volume = True):
  #if (len(it.name) > 0):
    #print(it.name + ": ")
  if (len(it.lowest_price) > 0):
    print("Lowest    = " + it.lowest_price)
  if (len(it.median_price) > 0):
    print("Median    = " + it.median_price)
  if (len(it.volume) > 0):
    print("Volume    = " + it.volume + " / Hari")
  else:
    print("Tolong Masukkan Nama Dengan Benar")

nama_item = input("Masukkan nama item : ")
pemanis = ("<-------------------------------------------------------------------------------------------------------->")
# - # - # - # - # - # - # - # - # -# - # - # - # - # - # - # - # - # - #
print(pemanis)
PrintMarketItem(GetMarketItem(AppId.CSGO.value,nama_item+ Exterior.BS))
time.sleep(3)
print(pemanis)
PrintMarketItem(GetMarketItem(AppId.CSGO.value,nama_item+ Exterior.WW))
time.sleep(3)
print(pemanis)
PrintMarketItem(GetMarketItem(AppId.CSGO.value,nama_item+ Exterior.FT))
time.sleep(3)
print(pemanis)
PrintMarketItem(GetMarketItem(AppId.CSGO.value,nama_item+ Exterior.MW))
time.sleep(3)
print(pemanis)
PrintMarketItem(GetMarketItem(AppId.CSGO.value,nama_item+ Exterior.FN))
time.sleep(3)
print(pemanis)
PrintMarketItem(GetMarketItem(AppId.CSGO.value,Exterior.ST+ nama_item+ Exterior.BS))
time.sleep(3)
print(pemanis)
PrintMarketItem(GetMarketItem(AppId.CSGO.value,Exterior.ST+ nama_item+ Exterior.WW))
time.sleep(3)
print(pemanis)
PrintMarketItem(GetMarketItem(AppId.CSGO.value,Exterior.ST+ nama_item+ Exterior.FT))
time.sleep(3)
print(pemanis)
PrintMarketItem(GetMarketItem(AppId.CSGO.value,Exterior.ST+ nama_item+ Exterior.MW))
time.sleep(3)
print(pemanis)
PrintMarketItem(GetMarketItem(AppId.CSGO.value,Exterior.ST+ nama_item+ Exterior.FN))
print(pemanis)
print("Done")