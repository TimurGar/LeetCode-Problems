# Solved with HASH MAP
# beats 95.18%, the idea is adapted and improved from online

def findRestaurant(list1, list2):
    # list[i] : i
    map = {}
    res = [1]
    sum = 0
    min_ind = float('inf')

    # Adding list1 elements to hash map
    for i in range(len(list1)):
        map[list1[i]] = i
    
    # iterating through list2 elements
    for i in range(len(list2)):
        
        # checking if the store exists in both lists
        if list2[i] in map:
            # calcuating the sum of indexes
            sum = map[list2[i]] + i

            if sum < min_ind:
                min_ind = sum
                res.clear()
                res.append(list2[i])
        
            elif sum == min_ind:
                res.append(list2[i])

print(findRestaurant(list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]))
print(findRestaurant(list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KFC","Shogun","Burger King"]))
print(findRestaurant(list1 = ["happy","sad","good"], list2 = ["sad","happy","good"]))
