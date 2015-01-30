import decimal

def return_change(cost, amount):
    """
    Simple program to calulate change return
    :param float cost: cost of thing ex. 2.22
    :param float amount:  how much money you have
    :return: string with number of 1zl, 50 gr, 20gr, 10gr, 5gr, 2gr, 1gr
    :rtype: string
    """
    if cost > amount:
        return "You have not enough money"
    
    zl200, zl100, zl50, zl20, zl10, zl5 ,zl2 ,zl1 = 0, 0, 0, 0, 0, 0, 0, 0
    gr50, gr20, gr10, gr5, gr2, gr1 = 0, 0, 0, 0, 0, 0
    
    zlotys = int(amount - cost)
    change = round((amount - zlotys - cost), 3) * 100
    
    if zlotys >= 200 :
        zl200 = int(zlotys/ 200)
        zlotys = zlotys % 200
        
    if zlotys >= 100 :
        zl100 = int(zlotys/ 100)
        zlotys = zlotys % 100
        
    if zlotys >= 50 :
        zl50 = int(zlotys/ 50)
        zlotys = zlotys % 50
        
    if zlotys >= 20 :
        zl20 = int(zlotys/ 20)
        zlotys = zlotys % 20
        
    if zlotys >= 10 :
        zl10 = int(zlotys/ 10)
        zlotys = zlotys % 10
        
    if zlotys >= 5 :
        zl5 = int(zlotys/ 5)
        zlotys = zlotys % 5
    
    if zlotys >= 2 :
        zl2 = int(zlotys/ 2)
        zlotys = zlotys % 2
        
    if zlotys >= 1 :
        zl1 = zlotys
    
    if change >= 50:
        gr50 = int(change/ 50)
        change = change % 50
       
    if change >= 20:
        gr20 = int(change/ 20)
        change = change % 20
        
    if change >= 10:
        gr10 = int(change/ 10)
        change = change % 10
    
    if change >= 5:
        gr5 = int(change/ 5)
        change = change % 5
    
    if change >= 2:
        gr2 = int(change/ 2)
        change = change % 2
        
    if change >= 1:
        gr1 = change
        
    return """ 
    You got {0} bills of 200zl, {1} bills of 100zl, {2} bills of 50 zl,
    {3} bills of 20zl, {4} bills of 10zl, {5} bills of 5zl, {6} bills of 2zl, 
    {7} bills of 1zl and {8} coins of 50gr, {9} coins of 20gr, {10} coins of 10gr,
    {11} coins of 5gr, {12} coins of 2gr and {13} of 1gr
    
    """.format(zl200, zl100, zl50, zl20, zl10, zl5 ,zl2 ,zl1, \
    gr50, gr20, gr10, gr5, gr2, gr1)
    
    
def main():
    cost = float(raw_input("Give cost >> "))
    amount = float(raw_input("Give amount >> "))
    print return_change(cost, amount)

if __name__ == "__main__":
    main()
