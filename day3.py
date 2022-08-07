def Remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list


# Driver Code
duplicate = [1,2,3,4,1,3,1,3,100,4,1,4]
print(Remove(duplicate))
