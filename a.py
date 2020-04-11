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
    url                = urllib.request.urlopen("http://steamcommunity.com/market/priceoverview/?appid=%s&currency=%s&market_hash_name=" % (appid, currency) + name)
    data               = json.loads(url.read().decode())
    Item.name          = name.replace("+", " ").replace("StatTrak%E2%84%A2 ", "StatTrak ")
    strdat             = str(data)
    lowest_price       = data['lowest_price'].replace(" ", "").replace("Rp","")
    median_price       = data['median_price'].replace(" ", "").replace("Rp","")
    volume             = data['volume']
    lp_float           = float(lowest_price)
    mp_float           = float(median_price)
    lp_int             = int(lp_float)
    mp_int             = int(mp_float)
    selisih            = lp_int - mp_int
    selisih_str        = str(selisih)
    profitpersen       = ((lp_int - mp_int)/ mp_float)* 100
    profitpersen_str   = str(profitpersen)
    tax                = 15/100
    rec_buy            = lp_int*(1-20/100)#remember tax = 15% so we only takes 5% profit
    rec_buy_str        = str(rec_buy)
    gain_sell          = lp_int - (15/100)
    est_profit         = rec_buy*(1-95/100)
    est_profit_str     = str(est_profit)
    fullurl            = ("https://steamcommunity.com/market/listings/%s/" % (appid)+ name)
    fullurl2           = (fullurl.replace("+","%20").replace("|","%7C").replace("(","%28").replace(")","%29"))
    
    
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
    if  lowest_price > median_price:
      print("Selisih   = Rp",selisih_str[0:8], "Atau",profitpersen_str[0:4], "%")
      print("Rec Buy   = Rp",rec_buy_str)
      print("Est Profit= Rp",est_profit_str)
    else:
      print("Tidak Profit")
    if (profitpersen) > 10:
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
PrintMarketItem(GetMarketItem(AppId.CSGO.value,(nama_item)+ Exterior.BS))
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