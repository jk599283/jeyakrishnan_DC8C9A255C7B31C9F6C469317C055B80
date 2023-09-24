def lenersearchprodect(prodectlist,targetprodect):
    indices=[]
    for index,prodect in enumerate(prodectlist):
        if prodect==targetprodect:
            indices.append(index)
    return indices
prodects=['Dragonfruit','Banana','Blacberry','Blueberry','Banana','Cherry','Banana']
target='Banana'
print(lenersearchprodect(prodects,target))

