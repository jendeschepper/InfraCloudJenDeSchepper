import unittest
import ipv4 as prf

class test_ipv4(unittest.XXXXAXXXXX):

   def test_get_net_prefix(self):
       self.XXXXBXXXXX(prf.get_net_prefix('255.255.255.252'), '/30')   
      
   def test_get_netmask(self):
       self.XXXXCXXXXX(prf.get_netmask('/30'), '255.255.255.252')   

   def test_get_number_ip_addresses(self):
       self.assertEqual(prf.get_number_ip_addresses('/30'), XXXXDXXXXX)   

   def test_get_number_ip_hosts(self):
       self.assertEqual(prf.get_number_ip_hosts('/30'), XXXXEXXXXX)

   def test_get_network_bits(self):
       self.assertEqual(prf.get_network_bits(XXXXFXXXXX),'1111 1111 1111 1111 1111 1111 1111 1100')

if __name__ == '__main__':
   unittest.XXXXGXXXXX()
