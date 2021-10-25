class ShoppingCart:
    def __init__(self):
    	self.quantity=0
 
       
    def additems(self,quantity):
    	if quantity>5:
    		return "cart cannot have more than 5 items"
    	else:
    		suffix = '' if quantity == 1 else 's'
    		return f'Successfully added {quantity} item{suffix} to cart!'
    	
