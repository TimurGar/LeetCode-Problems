# Solved with HASH MAP


# Notes
# add the item to hash map, if the item already exists, 
# add the current ind to the exisiting index
# and check if the current ind is less than the min_index (append the new min to res)
# also add if to see if the current ind == min_index
# name : sum index
# 

def findRestaurant(list1, list2):
    map1 = {}
    map2 = {}
    res = [1]
    min_ind = float('inf')    

    for i in range(len(list1)):
        
        if list1[i] not in map1:
            map1[list1[i]] = i
        
    for i in range(len(list2)):

        if list2[i] not in map2:
            map2[list2[i]] = i

    sum = 0
    for ind, store in enumerate(map1):
        if store in map2:

            sum = ind + map2[store]

            if sum < min_ind:
                min_ind = sum
                res[0] = store

            elif sum == min_ind:
                res.append(store)
                
    return res

print(findRestaurant(list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]))
print(findRestaurant(list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KFC","Shogun","Burger King"]))
print(findRestaurant(list1 = ["happy","sad","good"], list2 = ["sad","happy","good"]))