import bs4, requests

def getPrice(productUrl,cssSelector):
  res = requests.get(productUrl)
  res.raise_for_status()
  soup = bs4.BeautifulSoup(res.text, 'html.parser')
  elems = soup.select(cssSelector)
  return elems[0].text.strip()

PHLVaporPrice = getPrice('https://www.prohockeylife.com/collections/intermediate-hockey-sticks/products/bauer-vapor-flylite-int-hockey-stick?variant=21041112219725','#shopify-section-product-template > div > div.col-main > div.product > div.col-xs-12.col-sm-5.product-shop > div.col-md-12.col-xs-12.price-label-top > div > div > span')
print('The ProHockey Life Vapor FLYLITE is ', PHLVaporPrice)
CycloneVaporPrice = getPrice('https://cyclonetaylor.com/hockey/composite-sticks/intermediate/bauer-s19-vapor-flylite-grip-hockey-stick-int.html','#product-price-134655 > span')
print('The Cyclone Taylor Vapor FLYLITE is ' + CycloneVaporPrice)
BAUERVaporPrice = getPrice('https://www.bauer.com/en-CA/hockey-sticks/vapor-sticks/vapor-flylite-griptac-stick-intermediate-617669.html?cgid=Sticks-Vapor#start=1','#product-content > div.c-product-details__price.product-price > span')
print('The BAUER Official Vapor FLYLITE is ' + BAUERVaporPrice)
QREdgePrice = getPrice('https://www.prohockeylife.com/collections/intermediate-hockey-sticks/products/warrior-covert-qr-edge-int-hockey-stick?variant=12131982377034', '#shopify-section-product-template > div > div.col-main > div.product > div.col-xs-12.col-sm-5.product-shop > div.col-md-12.col-xs-12.price-label-top > div > div > span')
print('The ProHockey Life Warrior QREdge is ', QREdgePrice)
JetspeedPrice = getPrice('https://www.prohockeylife.com/collections/intermediate-hockey-sticks/products/ccm-jetspeed-pro-2-int-hockey-stick?variant=21041303978061','#shopify-section-product-template > div > div.col-main > div.product > div.col-xs-12.col-sm-5.product-shop > div.col-md-12.col-xs-12.price-label-top > div > div > span')
print('The ProHockey Life JetspeedPro is ' + JetspeedPrice)
