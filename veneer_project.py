# this is a Codecademy project i've made to pratice some of the basic concepts
# related to oriented object programming in python

class Art:
  def __init__(self, artist, title, medium, year, owner):
    self.artist = artist
    self.title = title
    self.medium = medium
    self.year = year
    self.owner  = owner
  def __repr__(self):
    return '{artist}. "{name}". {year}, {medium}. {owner}, {location}.'.format(artist=self.artist, name=self.title, year=self.year, medium=self.medium, owner=self.owner.name, location=self.owner.location)
  
class Marketplace:
  def __init__(self):
    self.listings = []
    
  def add_listing(self, new_listing):
    self.listings.append(new_listing)
  def remove_listing(self, to_remove):
    self.listings.remove(to_remove)
  def show_listings(self):
    for listing in self.listings:
      print(listing)

class Client:
  def __init__(self, name, location, is_museum):
    self.name = name
    self.location = location
    self.is_museum = is_museum
    
  def sell_artwork(self, artwork, price):
    if self == artwork.owner:
      new_listing = Listing(artwork, price, self)
      veneer.add_listing(new_listing)
  def buy_artwork(self, artwork):
      if artwork.owner != self:
          for listing in veneer.listings:
              if artwork == listing.art:
                  art_listing = listing
          art_listing.art.owner = self
          veneer.remove_listing(art_listing)
            
      
class Listing:
  def __init__(self, art, price, seller):
    self.art = art
    self.price = price
    self.seller = seller
  
  def __repr__(self):
    return '{}: {}'.format(self.art.title, self.price)
  

# Create a marketPlace  
veneer = Marketplace()
# It shoudln't print anything because the listing is empty
veneer.show_listings()

# Creates the first two clients
edytta = Client('Edytta Halpirt', 'Private Collection', False)
moma = Client('The MOMA', 'New York', True)
# Creates an artwork
girl_with_mandolin = Art('Picasso, Pablo',"Girl with a Mandolin (Fanny Tellier)" , 'oil on canvas', '1910', edytta)

# Put it for selling
edytta.sell_artwork(girl_with_mandolin, '$6M (USD)')

# Now, girl with mandolin should be in the artwork listing
veneer.show_listings()

# Test if a client is able to buy an artwork
moma.buy_artwork(girl_with_mandolin)

# Check if the owner has changed
print(girl_with_mandolin)

# check if the listing is empty again
veneer.show_listings()




    

  