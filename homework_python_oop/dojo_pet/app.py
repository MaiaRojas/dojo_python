import product
import store

costeno =  product.Product('costeno', 50, 'rice')
costeno.printInfo()
faraon =  product.Product('faraon', 40, 'rice')
paisana =  product.Product('paisana', 50, 'rice')
gloria =  product.Product('gloria', 10, 'milk')
laive =  product.Product('laive', 12, 'milk')
store = store.Store('donPepe', [costeno, faraon, paisana])

# Print
laive.printInfo()
# Update price
laive.updatePrice(5, True).printInfo()
# Add Products
store.addProduct(gloria)
store.addProduct(laive)

print(len(store.products))
# Sell product
deleted_id = store.products[0].id
store.sellProduct(deleted_id)
print(len(store.products))

# Bonus: inflacion
store.inflation(5)
store.products[1].printInfo()
#store.makeLiquidation('abarrotes', 10)