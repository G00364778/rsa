import psutil as _psutil

def pc_show_mac():
  net_if=_psutil.net_if_addrs()
  #print(f'{net_if}')
  fam={-1: 'MAC', 2: 'IPV4', 23: 'IPV6'}
  for item,vals in net_if.items():
    #print(f'{item}\n\t{vals}')
    for val in vals:
      print(f'{item:>28}  {fam[val.family]:>4}  {val.address:^20}')

if __name__ == "__main__":
  pc_show_mac()