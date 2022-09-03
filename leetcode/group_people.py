# 1282. Group the People Given the Group Size They Belong To
def groupThePeople(groupSizes):
        groups = {}
        ans = []
        for i in range(len(groupSizes)):
            group_key = groupSizes[i]
            if group_key in groups:
                groups[group_key].append(i)
            else:
                groups[group_key] = [i]

        for size in groups.keys():
            group_size = len(groups[size]) // size
            for i in range(group_size):
                temp = []
                count = 0
                while count < size:
                    count += 1
                    temp.append(groups[size].pop(0))
                ans.append(temp)
        return ans
      
# groupSizes = [3,3,3,3,3,1,3]
groupSizes = [2,1,3,3,3,2]

print(groupThePeople(groupSizes))
