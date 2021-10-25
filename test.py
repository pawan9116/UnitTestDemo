import ShoppingCart
import unittest


class TestShoppingCart(unittest.TestCase):
	def setUp(self):
		self.cart=ShoppingCart.ShoppingCart()
	def test1(self):
		msg = self.cart.additems(3)
		self.assertEqual(msg,'Successfully added 3 items to cart!')
       
		
	


unittest.main()

