##You have a collection of coins, and you know the values of the coins and the ##quantity of each type of coin in it. You want to know how many distinct sums you ##can make from non-empty groupings of these coins.

##Example

##For coins = [10, 50, 100] and quantity = [1, 2, 1], the output should be
##possibleSums(coins, quantity) = 9.

##Here are all the possible sums:

##50 = 50;
##10 + 50 = 60;
##50 + 100 = 150;
##10 + 50 + 100 = 160;
##50 + 50 = 100;
##10 + 50 + 50 = 110;
##50 + 50 + 100 = 200;
##10 + 50 + 50 + 100 = 210;
##10 = 10;
##100 = 100;
##10 + 100 = 110.
##As you can see, there are 9 distinct sums that can be created from non-empty ##groupings of your coins.

coins = [10, 50, 100]
quantity = [1, 2, 1]


def possibleSums(coins, quantity):
    ## we should store our possible sums in a hasmap
    possible_sums = set()   
    possible_sums.add(0)
    
    i = 0
    ## combined coins and quantity into a hashmap
    
    # for x in range(0, len(coins)):
        
    #     if coins[x] not in coins_quant:
    #         coins_quant[coins[x]] = quantity[x]
            
    #     if coins[x] in coins_quant:
    #         coins_quant[coins[x]] += quantity[x]

    loop = 1
    
    for j in range(0, len(coins)):
        
        print("loop: ", loop)
        key = coins[j]
        quant = quantity[j]
        ## frozenset creates a immutable copy of possible_sums
        for item in frozenset(possible_sums):
           
            for i in range(1, quant+1):
                possible_sums.add(item + key*i)
                print(possible_sums)
                print("poo poo pee pee")
        loop +=1
    
    
    possible_sums.remove(0)
    ##print(possible_sums)
    
    return len(possible_sums)
