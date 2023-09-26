def linear_search_product(products, target_product):
  indices = []
  for i in range(len(products)):
    if products[i] == target_product:
      indices.append(i)
  return indices


# Example usage:
product_list = ["Apple", "Banana", "Orange", "Apple", "Mango", "Apple"]
target_product_name = "Apple"
result = linear_search_product(product_list, target_product_name)
print("Indices of", target_product_name, ":", result)
