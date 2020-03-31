
def deleteProducts(ids, m):
    # Write your code here
    # 
    ids = [1,1,5,5]
    m = 0
    for i in ids:
        if ids.count(i) > 1:
            m += 1
        else: 
            ids.count(i) == 1
            m += 1
    return m


