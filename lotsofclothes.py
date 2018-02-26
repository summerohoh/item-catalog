from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from catalog_dbsetup import Category, User, Base, Item

engine = create_engine('sqlite:///clothingcatalog.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

#initial user - Me 
user1 = User(name="Summer Oh", email="jo289@cornell.edu",
             picture="https://lh3.googleusercontent.com/-BY8urdernQE/AAAAAAAAAAI/AAAAAAAAAHs/lyYzSOVwZRo/s120-p-rw-no/photo.jpg")
session.add(user1)
session.commit()

#6 items for Tshirts
category1 = Category(user=user1, name="Tshirts")
session.add(category1)
session.commit()

item1 = Item(user=user1, name="patch logo T-shirt", img="https://cdn-images.farfetch-contents.com/12/58/79/09/12587909_12047551_480.jpg",
	brand = "MOSCHINO", shopURL="https://www.farfetch.com/shopping/women/moschino-patch-logo-t-shirt-item-12587909.aspx?storeid=9560&from=similar_listing", price="$416", category=category1)

session.add(item1)
session.commit()

item2 = Item(user=user1, name="Rome Pays Off Mona Lisa print t-shirt", img="https://cdn-images.farfetch-contents.com/12/39/08/66/12390866_11206756_480.jpg",
	brand = "JEAN-MICHEL BASQUIAT X BROWNS", shopURL="https://www.farfetch.com/shopping/women/jean-michel-basquiat-x-browns-rome-pays-off-mona-lisa-print-t-shirt-item-12390866.aspx?storeid=9359&from=listing&tglmdl=1", price="$120", category=category1)

session.add(item2)
session.commit()

item3 = Item(user=user1, name="eye print T-shirt", img="https://cdn-images.farfetch-contents.com/12/62/73/46/12627346_12160565_480.jpg",
	brand = "KENZO", shopURL="https://www.farfetch.com/shopping/women/kenzo-eye-print-t-shirt-item-12627346.aspx?storeid=9068&from=listing&tglmdl=1", price="$125", category=category1)

session.add(item3)
session.commit()

item4 = Item(user=user1, name="Tiger T-shirt", img="https://cdn-images.farfetch-contents.com/12/55/25/67/12552567_11937195_480.jpg",
	brand = "KENZO", shopURL="https://www.farfetch.com/shopping/women/kenzo-tiger-t-shirt-item-12552567.aspx?storeid=9644&from=listing&tglmdl=1", price="$125", category=category1)

session.add(item4)
session.commit()

item5 = Item(user=user1, name="branded T-shirt", img="https://cdn-images.farfetch-contents.com/12/61/12/13/12611213_12128059_480.jpg",
	brand = "MSGM", shopURL="https://www.farfetch.com/shopping/women/msgm-branded-t-shirt-item-12611213.aspx?storeid=9763&from=listing&tglmdl=1", price="$350", category=category1)

session.add(item5)
session.commit()

item6 = Item(user=user1, name="arrows print T-shirt", img="https://cdn-images.farfetch-contents.com/12/64/63/30/12646330_12257536_480.jpg",
	brand = "OFF-WHITE", shopURL="https://www.farfetch.com/shopping/women/off-white-arrows-print-t-shirt-item-12646330.aspx?storeid=10122&from=listing&tglmdl=1", price="", category=category1)

session.add(item6)
session.commit()

#6 items for Blouses
category2 = Category(user=user1, name="Blouses")
session.add(category2)
session.commit()

item1 = Item(user=user1, name="floral asymmetric shirt", img="https://cdn-images.farfetch-contents.com/12/61/78/98/12617898_12119836_480.jpg",
	brand = "LOEWE", shopURL="https://www.farfetch.com/shopping/women/loewe-floral-asymmetric-shirt-item-12617898.aspx?storeid=11025&from=listing&tglmdl=1", price="$709", category=category2)

session.add(item1)
session.commit()

item2 = Item(user=user1, name="Long Sleeved Blouse with Neck Tie", img="https://cdn-images.farfetch-contents.com/12/19/66/43/12196643_10372168_480.jpg",
	brand = "CHLOE", shopURL="https://www.farfetch.com/shopping/women/chloe--long-sleeved-blouse-with-neck-tie-item-12196643.aspx?storeid=10030&from=listing&tglmdl=1", price="$1395", category=category2)

session.add(item2)
session.commit()

item3 = Item(user=user1, name="lip print blouse", img="https://cdn-images.farfetch-contents.com/12/51/92/78/12519278_11806840_480.jpg",
	brand = "L'AGENCE", shopURL="https://www.farfetch.com/shopping/women/l-agence-lip-print-blouse-item-12519278.aspx?storeid=9610&from=listing&tglmdl=1", price="$325", category=category2)

session.add(item3)
session.commit()

item4 = Item(user=user1, name="cold shoulder shirt", img="https://cdn-images.farfetch-contents.com/12/56/19/96/12561996_11983144_480.jpg",
	brand = "STEFFEN SCHRAUT", shopURL="https://www.farfetch.com/shopping/women/steffen-schraut-cold-shoulder-shirt--item-12561996.aspx?storeid=10668&from=listing&tglmdl=1", price="$146", category=category2)

session.add(item4)
session.commit()

item5 = Item(user=user1, name="striped bardot sweater", img="https://cdn-images.farfetch-contents.com/12/62/13/74/12621374_12212851_480.jpg",
	brand = "MARC CAIN", shopURL="https://www.farfetch.com/shopping/women/marc-cain-striped-bardot-sweater--item-12621374.aspx?storeid=9854&from=listing&tglmdl=1", price="$150", category=category2)

session.add(item5)
session.commit()

item6 = Item(user=user1, name="striped bell sleeve tunic top", img="https://cdn-images.farfetch-contents.com/12/62/08/28/12620828_12169803_480.jpg",
	brand = "MICHAEL MICHAEL KORS", shopURL="https://www.farfetch.com/shopping/women/michael-michael-kors-striped-bell-sleeve-tunic-top-item-12620828.aspx?storeid=9644&from=listing&tglmdl=1", price="$172", category=category2)

session.add(item6)
session.commit()

#6 items for Sweaters
category3 = Category(user=user1, name="Sweaters")
session.add(category3)
session.commit()

item1 = Item(user=user1, name="Adidas Originals Adibreak sweatshirt", img="https://cdn-images.farfetch-contents.com/12/66/93/29/12669329_12420459_480.jpg",
	brand = "ADIDAS", shopURL="https://www.farfetch.com/shopping/women/adidas-adidas-originals-adibreak-sweatshirt-item-12669329.aspx?storeid=10218&from=listing&tglmdl=1", price="$109", category=category3)

session.add(item1)
session.commit()

item2 = Item(user=user1, name="Amour sweater", img="https://cdn-images.farfetch-contents.com/12/67/66/29/12676629_12532039_480.jpg",
	brand = "MAISON LABICHE", shopURL="https://www.farfetch.com/shopping/women/maison-labiche-amour-sweater-item-12676629.aspx?storeid=9040&from=listing&tglmdl=1", price="$124", category=category3)

session.add(item2)
session.commit()

item3 = Item(user=user1, name="branded sweatshirt", img="https://cdn-images.farfetch-contents.com/12/65/68/14/12656814_12296150_480.jpg",
	brand = "MSGM", shopURL="https://www.farfetch.com/shopping/women/msgm-branded-sweatshirt-item-12656814.aspx?storeid=9474&from=listing&tglmdl=1", price="$185", category=category3)

session.add(item3)
session.commit()

item4 = Item(user=user1, name="Hear Me Roar sweatshirt", img="https://cdn-images.farfetch-contents.com/12/07/12/03/12071203_10410994_480.jpg",
	brand = "ZOE KARSSEN", shopURL="https://www.farfetch.com/shopping/women/zoe-karssen-hear-me-roar-sweatshirt--item-12071203.aspx?storeid=9214&from=listing&tglmdl=1", price="$155", category=category3)

session.add(item4)
session.commit()

item5 = Item(user=user1, name="raglan sleeve sweatshirt", img="https://cdn-images.farfetch-contents.com/12/69/49/62/12694962_12434578_480.jpg",
	brand = "JOSEPH", shopURL="https://www.farfetch.com/shopping/women/joseph-raglan-sleeve-sweatshirt-item-12694962.aspx?storeid=9523&from=listing&tglmdl=1", price="$272", category=category3)

session.add(item5)
session.commit()

item6 = Item(user=user1, name="embossed logo sweatshirt", img="https://cdn-images.farfetch-contents.com/12/10/68/17/12106817_9866490_480.jpg",
	brand = "FENDI", shopURL="https://www.farfetch.com/shopping/women/fendi-embossed-logo-sweatshirt-item-12106817.aspx?storeid=9140&from=listing&tglmdl=1", price="$1050", category=category3)

session.add(item6)
session.commit()

#6 items for Coats
category4 = Category(user=user1, name="Coats")
session.add(category4)
session.commit()

item1 = Item(user=user1, name="Caban trench coat", img="https://cdn-images.farfetch-contents.com/12/66/81/23/12668123_12319967_480.jpg",
	brand = "STELLA MCCARTNEY", shopURL="https://www.farfetch.com/shopping/women/stella-mccartney-caban-trench-coat-item-12668123.aspx?storeid=9728&from=listing&tglmdl=1", price="$1995", category=category4)

session.add(item1)
session.commit()

item2 = Item(user=user1, name="tartan trench coat", img="https://cdn-images.farfetch-contents.com/12/67/25/88/12672588_12316585_480.jpg",
	brand = "BURBERRY", shopURL="https://www.farfetch.com/shopping/women/burberry-tartan-trench-coat-item-12672588.aspx?storeid=9446&from=listing&tglmdl=1", price="$2577", category=category4)

session.add(item2)
session.commit()

item3 = Item(user=user1, name="sleeveless single breasted coat", img="https://cdn-images.farfetch-contents.com/12/70/09/71/12700971_12482555_480.jpg",
	brand = "NEIL BARRETT", shopURL="https://www.farfetch.com/shopping/women/neil-barrett-sleeveless-single-breasted-coat-item-12700971.aspx?storeid=9107&from=listing&tglmdl=1", price="$2279", category=category4)

session.add(item3)
session.commit()

item4 = Item(user=user1, name="surf surplus trench", img="https://cdn-images.farfetch-contents.com/12/66/40/15/12664015_12412219_480.jpg",
	brand = "LEVI'S: MADE & CRAFTED", shopURL="https://www.farfetch.com/shopping/women/levi-s-made-crafted-surf-surplus-trench-item-12664015.aspx?storeid=9006&from=listing&tglmdl=1", price="$274", category=category4)

session.add(item4)
session.commit()

item5 = Item(user=user1, name="belted trench coat", img="https://cdn-images.farfetch-contents.com/12/24/71/82/12247182_11116340_480.jpg",
	brand = "OSCAR DE LA RENTA", shopURL="https://www.farfetch.com/shopping/women/oscar-de-la-renta-belted-trench-coat-item-12247182.aspx?storeid=10351&from=listing&tglmdl=1", price="$2490", category=category4)

session.add(item5)
session.commit()

item6 = Item(user=user1, name="BURBERRY", img="https://cdn-images.farfetch-contents.com/12/69/82/20/12698220_12387122_480.jpg",
	brand = "laminated check trench coat", shopURL="https://www.farfetch.com/shopping/women/burberry-laminated-check-trench-coat-item-12698220.aspx?storeid=9544&from=listing&tglmdl=1", price="$2524", category=category4)

session.add(item6)
session.commit()

#6 items for Jackets
category5 = Category(user=user1, name="Jackets")
session.add(category5)
session.commit()

item1 = Item(user=user1, name="cropped hooded jacket", img="https://cdn-images.farfetch-contents.com/12/69/31/60/12693160_12483845_480.jpg",
	brand = "LOEWE", shopURL="https://www.farfetch.com/shopping/women/loewe-cropped-hooded-jacket-item-12693160.aspx?storeid=9531&from=listing&tglmdl=1", price="$2150", category=category5)

session.add(item1)
session.commit()

item2 = Item(user=user1, name="embroidered logo bomber jacket", img="https://cdn-images.farfetch-contents.com/12/71/84/27/12718427_12509863_480.jpg",
	brand = "CHIARA FERRAGNI", shopURL="https://www.farfetch.com/shopping/women/chiara-ferragni-embroidered-logo-bomber-jacket-item-12718427.aspx?storeid=9644&from=listing&tglmdl=1", price="$571", category=category5)

session.add(item2)
session.commit()

item3 =Item(user=user1, name="Puffer jacket with hood and contrasting zip", img="https://cdn-images.farfetch-contents.com/12/54/75/49/12547549_11981684_480.jpg",
	brand = "GANNI", shopURL="https://www.farfetch.com/shopping/women/ganni-puffer-jacket-with-hood-and-contrasting-zip-item-12547549.aspx?storeid=9249&from=listing&tglmdl=1", price="$440", category=category5)

session.add(item3)
session.commit()

item4 = Item(user=user1, name="double breasted tweed blazer", img="https://cdn-images.farfetch-contents.com/12/68/46/58/12684658_12426016_480.jpg",
	brand = "BALMAIN", shopURL="https://www.farfetch.com/shopping/women/balmain-double-breasted-tweed-blazer-item-12684658.aspx?storeid=9462&from=listing&tglmdl=1", price="$1782", category=category5)

session.add(item4)
session.commit()


item5 = Item(user=user1, name="white Like A Man denim jacket", img="https://cdn-images.farfetch-contents.com/12/64/52/09/12645209_12296352_480.jpg",
	brand = "BALENCIAGA", shopURL="https://www.farfetch.com/shopping/women/balenciaga-white-like-a-man-denim-jacket-item-12645209.aspx?storeid=10952&from=listing&tglmdl=1", price="$1295", category=category5)

session.add(item5)
session.commit()

item6 = Item(user=user1, name="PSWL Denim Drawstring Jacket", img="https://cdn-images.farfetch-contents.com/12/26/92/49/12269249_11786056_480.jpg",
	brand = "PROENZA SCHOULER", shopURL="https://www.farfetch.com/shopping/women/proenza-schouler-pswl-denim-drawstring-jacket-item-12269249.aspx?storeid=10225&from=listing&tglmdl=1", price="$575", category=category5)

session.add(item6)
session.commit()

#6 items for Hoodies
category6 = Category(user=user1, name="Hoodies")
session.add(category6)
session.commit()

item1 = Item(user=user1, name="sleeve-logo hooded sweatshirt", img="https://cdn-images.farfetch-contents.com/12/64/95/75/12649575_12268434_480.jpg",
	brand = "DKNY", shopURL="https://www.farfetch.com/shopping/women/dkny-sleeve-logo-hooded-sweatshirt-item-12649575.aspx?storeid=9336&from=listing&tglmdl=1", price="$103", category=category6)

session.add(item1)
session.commit()

item2 =Item(user=user1, name="C'est La Vie hoodie", img="https://cdn-images.farfetch-contents.com/12/67/23/11/12672311_12339763_480.jpg",
	brand = "MAISON LABICHE", shopURL="https://www.farfetch.com/shopping/women/maison-labiche-c-est-la-vie-hoodie-item-12672311.aspx?storeid=9124&from=listing&tglmdl=1", price="$121", category=category6)

session.add(item2)
session.commit()

item3 = Item(user=user1, name="mood board print hoodie", img="https://cdn-images.farfetch-contents.com/12/56/52/57/12565257_12040829_480.jpg",
	brand = "HOUSE OF HOLLAND", shopURL="https://www.farfetch.com/shopping/women/house-of-holland-mood-board-print-hoodie-item-12565257.aspx?storeid=10055&from=listing&tglmdl=1", price="$126", category=category6)

session.add(item3)
session.commit()

item4 = Item(user=user1, name="flag front hoodie", img="https://cdn-images.farfetch-contents.com/12/66/44/85/12664485_12302507_480.jpg",
	brand = "TOMMY HILFIGER", shopURL="https://www.farfetch.com/shopping/women/tommy-hilfiger-flag-front-hoodie-item-12664485.aspx?storeid=9446&from=listing&tglmdl=1", price="$159", category=category6)

session.add(item4)
session.commit()

item5 = Item(user=user1, name="printed hoodie", img="https://cdn-images.farfetch-contents.com/12/66/25/98/12662598_12330269_480.jpg",
	brand = "ALYX", shopURL="https://www.farfetch.com/shopping/women/alyx-printed-hoodie--item-12662598.aspx?storeid=10977&from=listing&tglmdl=1", price="$361", category=category6)

session.add(item5)
session.commit()

item6 = Item(user=user1, name="PSWL Drawstring Hoodie", img="https://cdn-images.farfetch-contents.com/12/26/92/65/12269265_11786089_480.jpg",
	brand = "PROENZA SCHOULER", shopURL="https://www.farfetch.com/shopping/women/proenza-schouler-pswl-drawstring-hoodie-item-12269265.aspx?storeid=10225&from=listing&tglmdl=1", price="$375", category=category6)

session.add(item6)
session.commit()

#6 items for Dresses
category7 = Category(user=user1, name="Dresses")
session.add(category7)
session.commit()

item1 = Item(user=user1, name="sheer panel dress", img="https://cdn-images.farfetch-contents.com/11/53/61/44/11536144_7317515_480.jpg",
	brand = "VALENTINO", shopURL="https://www.farfetch.com/shopping/women/valentino-sheer-panel-dress-item-11536144.aspx?storeid=9796&from=listing&tglmdl=1", price="$4390", category=category7)

session.add(item1)
session.commit()

item2 = Item(user=user1, name="strapless flared dress", img="https://cdn-images.farfetch-contents.com/12/57/02/21/12570221_11972310_480.jpg",
	brand = "C/MEO", shopURL="https://www.farfetch.com/shopping/women/c-meo-strapless-flared-dress-item-12570221.aspx?storeid=9423&from=listing&tglmdl=1", price="$170", category=category7)

session.add(item2)
session.commit()

item3 = Item(user=user1, name="Delta Vichy dress", img="https://cdn-images.farfetch-contents.com/12/58/44/87/12584487_12098692_480.jpg",
	brand = "SEMICOUTURE", shopURL="https://www.farfetch.com/shopping/women/semicouture-delta-vichy-dress--item-12584487.aspx?storeid=9690&from=listing&tglmdl=1", price="$188", category=category7)

session.add(item3)
session.commit()

item4 = Item(user=user1, name="Conceptualise dress", img="https://cdn-images.farfetch-contents.com/12/40/18/60/12401860_11318587_480.jpg",
	brand = "TAYLOR", shopURL="https://www.farfetch.com/shopping/women/taylor-conceptualise-dress-item-12401860.aspx?storeid=10811&from=listing&tglmdl=1", price="$198", category=category7)

session.add(item4)
session.commit()

item5 = Item(user=user1, name="Dustin Vichy dress", img="https://cdn-images.farfetch-contents.com/12/58/45/16/12584516_12101363_480.jpg",
	brand = "SEMICOUTURE", shopURL="https://www.farfetch.com/shopping/women/semicouture-dustin-vichy-dress--item-12584516.aspx?storeid=9709&from=listing&tglmdl=1", price="$189", category=category7)

session.add(item5)
session.commit()

item6 = Item(user=user1, name="frayed detail midi dress", img="https://cdn-images.farfetch-contents.com/12/53/24/98/12532498_11909741_480.jpg",
	brand = "VENROY", shopURL="https://www.farfetch.com/shopping/women/venroy-frayed-detail-midi-dress-item-12532498.aspx?storeid=10329&from=listing&tglmdl=1", price="$102", category=category7)

session.add(item6)
session.commit()

#6 items for Skirts
category8 = Category(user=user1, name="Skirts")
session.add(category8)
session.commit()

item1 = Item(user=user1, name="Joe striped flared skirt", img="https://cdn-images.farfetch-contents.com/12/56/46/47/12564647_12054292_480.jpg",
	brand = "ZADIG & VOLTAIRE", shopURL="https://www.farfetch.com/shopping/women/zadig-voltaire-joe-striped-flared-skirt-item-12564647.aspx?storeid=11037&from=listing&tglmdl=1", price="$248", category=category8)

session.add(item1)
session.commit()


item2 = Item(user=user1, name="Piper Skirt Exposed Obscure", img="https://cdn-images.farfetch-contents.com/12/24/47/19/12244719_10973911_480.jpg",
	brand = "NOBODY DENIM", shopURL="https://www.farfetch.com/shopping/women/nobody-denim-piper-skirt-exposed-obscure-item-12244719.aspx?storeid=9964&from=listing&tglmdl=1", price="$122", category=category8)

session.add(item2)
session.commit()

item3 = Item(user=user1, name="Piper Skirt Ruby", img="https://cdn-images.farfetch-contents.com/12/53/85/39/12538539_11909639_480.jpg",
	brand = "NOBODY DENIM", shopURL="https://www.farfetch.com/shopping/women/nobody-denim-piper-skirt-ruby--item-12538539.aspx?storeid=9964&from=listing&tglmdl=1", price="$159", category=category8)

session.add(item3)
session.commit()

item4 = Item(user=user1, name="Dropped-Back Mini Pleated Skirt ", img="https://cdn-images.farfetch-contents.com/12/31/52/53/12315253_11169378_480.jpg",
	brand = "THOM BROWNE", shopURL="https://www.farfetch.com/shopping/women/thom-browne-dropped-back-mini-pleated-skirt-in-navy-super-130-s-wool-twill-item-12315253.aspx?storeid=10552&from=listing&tglmdl=1", price="$1150", category=category8)

session.add(item4)
session.commit()

item5 = Item(user=user1, name="Austen skirt", img="https://cdn-images.farfetch-contents.com/11/83/54/32/11835432_8916362_480.jpg",
	brand = "MISHA NONOO", shopURL="https://www.farfetch.com/shopping/women/misha-nonoo-austen-skirt--item-11835432.aspx?storeid=10051&from=listing&tglmdl=1", price="$250", category=category8)

session.add(item5)
session.commit()

item6 = Item(user=user1, name="Piper Skirt Angel", img="https://cdn-images.farfetch-contents.com/12/21/97/55/12219755_10699075_480.jpg",
	brand = "NOBODY DENIM", shopURL="https://www.farfetch.com/shopping/women/nobody-denim-piper-skirt-angel-item-12219755.aspx?storeid=9964&from=listing&tglmdl=1", price="$122", category=category8)

session.add(item6)
session.commit()

#6 items for Pants
category9 = Category(user=user1, name="Pants")
session.add(category9)
session.commit()

item1 = Item(user=user1, name="cropped trousers", img="https://cdn-images.farfetch-contents.com/12/61/46/41/12614641_12181753_480.jpg",
	brand = "STYLAND", shopURL="https://www.farfetch.com/shopping/women/styland-cropped-trousers-item-12614641.aspx?storeid=9421&from=listing&tglmdl=1", price="$259", category=category9)

session.add(item1)
session.commit()

item2 = Item(user=user1, name="classic skinny jeans", img="https://cdn-images.farfetch-contents.com/12/56/87/47/12568747_11986302_480.jpg",
	brand = "TWIN-SET", shopURL="https://www.farfetch.com/shopping/women/twin-set-classic-skinny-jeans-item-12568747.aspx?storeid=9206&from=listing&tglmdl=1", price="$137", category=category9)

session.add(item2)
session.commit()

item3 = Item(user=user1, name="buttoned high-waisted trousers", img="https://cdn-images.farfetch-contents.com/12/69/98/43/12699843_12467344_480.jpg",
	brand = "CHLOE", shopURL="https://www.farfetch.com/shopping/women/chloe--buttoned-high-waisted-trousers-item-12699843.aspx?storeid=9462&from=listing&tglmdl=1", price="$1281", category=category9)

session.add(item3)
session.commit()

item4 = Item(user=user1, name="classic flared trousers", img="https://cdn-images.farfetch-contents.com/12/43/59/68/12435968_11485688_480.jpg",
	brand = "FABIANA FILIPPI", shopURL="https://www.farfetch.com/shopping/women/fabiana-filippi-classic-flared-trousers-item-12435968.aspx?storeid=9880&from=listing&tglmdl=1", price="$1980", category=category9)

session.add(item4)
session.commit()

item5 = Item(user=user1, name="tailored trousers", img="https://cdn-images.farfetch-contents.com/12/63/72/18/12637218_12224212_480.jpg",
	brand = "MOSCHINO VINTAGE", shopURL="https://www.farfetch.com/shopping/women/moschino-vintage-tailored-trousers--item-12637218.aspx?storeid=9164&from=listing&tglmdl=1", price="$264", category=category9)

session.add(item5)
session.commit()

item6 = Item(user=user1, name="striped tailored trousers", img="https://cdn-images.farfetch-contents.com/12/64/78/43/12647843_12334136_480.jpg",
	brand = "H BEAUTY&YOUTH", shopURL="https://www.farfetch.com/shopping/women/h-beauty-youth-striped-tailored-trousers-item-12647843.aspx?storeid=10317&from=listing&tglmdl=1", price="$230", category=category9)

session.add(item6)
session.commit()