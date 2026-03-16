import unittest
from main import Device, Smartphone, Cart

class TestElectronicStore(unittest.TestCase):

    def test_device_creation(self):
        d = Device("Generic Device", 100, 10, 12)
        self.assertEqual(d.name, "Generic Device")
        self.assertEqual(d.price, 100)
        self.assertEqual(d.stock, 10)

    def test_discount(self):
        d = Device("Test Phone", 100, 10, 12)
        d.apply_discount(20) # 20% off
        self.assertEqual(d.price, 80)

    def test_stock_availability(self):
        d = Device("Test Phone", 100, 5, 12)
        self.assertTrue(d.is_available(3))
        self.assertFalse(d.is_available(6))

    def test_cart_calculation(self):
        c = Cart()
        p1 = Smartphone("Phone A", 500, 10, 12, 6.1, 20)
        p2 = Smartphone("Phone B", 300, 10, 12, 5.5, 18)

        c.add_device(p1, 1) # $500
        c.add_device(p2, 2) # $600

        self.assertEqual(c.get_total_price(), 1100)

if __name__ == '__main__':
    unittest.main()