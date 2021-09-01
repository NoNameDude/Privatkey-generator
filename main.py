import blocksmith

def generate_address(key_type):
    kg = blocksmith.KeyGenerator()
    key = kg.generate_key() 

    if key_type == "ETH":
        Text = "Your Public key is {}"
        Text2 = "Your Privat key is {}"
        public_adress = blocksmith.EthereumWallet.generate_address(key)
        print(Text.format(key))
        print(Text2.format(public_adress))
   
    if key_type == "BTC": 
        Text = "Your Public key is {}"
        Text2 = "Your Privat key is {}"
        privat_address = blocksmith.BitcoinWallet.generate_address(key)
        print(Text.format(privat_address))
        print(Text2.format(key)) 

 

#Make a loop for a python interface  
Prog = True
while Prog:
    Prog2 = True
    while Prog2:
        key_type = input("What key do you like to generate BTC or ETH? ")
        if key_type == "BTC" or key_type == "ETH":
            Prog2 = False
        else:
            print("Pls write only BTC for Bitcoin or ETH for Ethereum")

    Prog2 = True
    while Prog2:
        key_amount = input("How many keys do you like to generate ")
        try:
            testing_number = int(key_amount) 
            Prog2 = False
        except: 
            print("{} Variable is not a number ".format(testing_number)) 

    for i in range(int(key_amount)):
        generate_address(key_type)
