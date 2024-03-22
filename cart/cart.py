from store.models import Product

class Cart():
    def __init__(self, request):
        self.session = request.session

        #get the current session key if it exists
        cart = self.session.get('session_key')

        # if the user is new no session key! create a new one
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}
                        
        # make sure cart available on all pages of site
        self.cart = cart

    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = str(quantity)

        # logic
        if product_id in self.cart:
            pass
        else:
            # self.cart[product_id] = {'price': str(product.price)}
            self.cart[product_id] = int(product_qty)

        self.session.modified = True

    # for length of cart
    def __len__(self):
        return len(self.cart)
    
    # To lookup Products in cart
    def get_prods(self):
        #get ids from cart
        product_ids = self.cart.keys()
        # use ids to lookup products in database model
        products = Product.objects.filter(id__in = product_ids)
        # return those lookup products
        return products
    
    def get_quants(self):
        quantities = self.cart
        return quantities
    
    def update(self, product, quantity):
        product_id = str(product)
        product_qty = int(quantity)
        # get cart
        ourcart = self.cart
        # update dictionary/cart
        ourcart[product_id] = product_qty

        self.session.modified = True

        thing = self.cart
        return thing
    
    def delete(self, product):
        product_id = str(product)
        
        if product_id in self.cart:
            del self.cart[product_id]

        self.session.modified = True
    

