import math

def decommissioning_year(population):
    """Function that decommisions 
    1 % of robots
    """
    return math.floor(population/100)
    
def reproduction_day(A,B, alpha,beta):
    """Create couples for reproduction"""
    couples = min(A,B)
    reproduction_year = math.floor(couples*2/100)
    acrobots = math.floor(reproduction_year*alpha / 100)
    bouncoids = math.floor(reproduction_year*beta / 100) 
    remain_bots = reproduction_year - acrobots - bouncoids 
    
    acrobots = acrobots + (remain_bots//2)
    bouncoids = bouncoids + (remain_bots//2)
    
    if remain_bots % 2 == 1:
        bouncoids +=1
    
    return acrobots, bouncoids
    
def population_evolution(A,B):
    """Defines what is happening across all these 3 days"""
    # 2nd day ( add the new babies born)
    acrobots, bouncoids = reproduction_day(A,B, alpha,beta)
    # 3rd day (substract the decommissioned bots)
    acrobots_dec = decommissioning_year(A)
    bouncoids_dec = decommissioning_year(B)
    
    acrobots_def = acrobots - acrobots_dec
    bouncoids_def = bouncoids - bouncoids_dec
    return acrobots , bouncoids

### Iterate over the Years to see the pop dec
acrobots_0 , bouncoids_0 = population_evolution(A,B)
for i in range(1,Y):
    
    acrobots_1 , bouncoids_1 = population_evolution(acrobots_0 , bouncoids_0)
        if acrobots_0 == acrobots_1:
            return "Case" + "#"str(Y) + acrobots_0  bouncoids_0 )
        else:
            acrobots_0 , bouncoids_0 = acrobots_1, bouncoids_1
