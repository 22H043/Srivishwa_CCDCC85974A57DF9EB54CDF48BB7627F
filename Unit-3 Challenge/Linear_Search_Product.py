def linear_search_product(product_list, target_product):
    indices = []
    for i in range(len(product_list)):
        if product_list[i] == target_product:
            indices.append(i)
    return indices

# Example usage:
products = ["apple", "banana", "apple", "grape", "apple", "kiwi"]
target = "apple"

result = linear_search_product(products, target)

if result:
    print(f"The target product '{target}' was found at indices: {result}")
else:
    print(f"The target product '{target}' was not found in the list.")
