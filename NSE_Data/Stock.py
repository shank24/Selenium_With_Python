from nsetools import Nse

nse = Nse()
print nse
adv_dec = nse.get_advances_declines()
print(adv_dec)