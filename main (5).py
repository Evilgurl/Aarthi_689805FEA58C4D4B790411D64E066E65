def linearsearchprodects(productlist,targetproduct):
  indices = []
  
  for index,product in enumerate(productlist):
    if product == targetproduct:
      indices.append(index)

  return indices


products =["shoes","boot","loafer","shoes","sandal","shoes"]
target = "shoes"
result = linearsearchprodects(products, target)
print(result)


  