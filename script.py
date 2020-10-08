def ground_cost(weight):
  flat = 20
  if weight<=2:
    cost = (1.5*weight)+flat
  elif 2<weight<=6:
    cost = (3*weight)+flat
  elif 6<weight<=10:
    cost = (4*weight)+flat
  else:
    cost = (4.75*weight)+flat
  return cost

premium_cost = 125

def drone_cost(weight):
  if weight<=2:
    cost = (4.5*weight)
  elif 2<weight<=6:
    cost = (9*weight)
  elif 6<weight<=10:
    cost = (12*weight)
  else: cost=14.25*weight
  return cost

def cheap_cost(ground_cost,premium_cost,drone_cost):
  if ground_cost<premium_cost and ground_cost<drone_cost:
    print('Ground cost: ' + str(ground_cost))
  elif premium_cost<ground_cost and premium_cost<drone_cost:
    print('Premium cost: ' + str(premium_cost))
  else: 
    print('Drone cost: ' + str(drone_cost))

cheap_cost(ground_cost(4.8), premium_cost, drone_cost(4.8))

cheap_cost(ground_cost(41.5), premium_cost, drone_cost(41.5))