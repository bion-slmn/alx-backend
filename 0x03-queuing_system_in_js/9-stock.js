import express from 'express';
import { createClient } from 'redis';
const {promisify} = require('util');

const app = express();
const client = createClient()

console.log(client.connected); 


const getAsync = promisify(client.get).bind(client);

const listProducts = [
    { id: 1, name: 'Suitcase 250', price: 50, stock: 4 },
    { id: 2, name: 'Suitcase 450', price: 100, stock: 10 },
    { id: 3, name: 'Suitcase 650', price: 350, stock: 2 },
    { id: 4, name: 'Suitcase 1050', price: 550, stock: 5 }
];


const getItemById = (id) => {
	return listProducts.find((value) => {
		return value.id === id;
	});
}

app.get('/list_products', (req, res) => {
 res.json(listProducts);
}).listen(1245);

async function reserveStockById(itemId, stock){
    return promisify(client.SET).bind(client)(`item.${itemId}`, stock);

}

async function getCurrentReservedStockById(itemId){
  
  return getAsync(`item.${itemId}`)
}

app.get('/list_products/:itemId', async (req, res) => {
  const { itemId } = req.params;
  const item =  getItemById(+itemId);

 if (!item){
  res.json({"status":"Product not found"});
 }

  const result = await getCurrentReservedStockById(+itemId);
  const reservedItem = result || 0;
  console.log(reservedItem);  
  res.json({
  	itemId,
  	'itemName': item['name'],
 	"price": item['price'],
	"initialAvailableQuantity" : item['stock'],
	"currentQuantity": item['stock'] - (reservedItem['stock'] || reservedItem),
  });
})


app.get('/reserve_product/:itemId', async (req, res) => {
	  const { itemId } = req.params;
  const item =  getItemById(+itemId);

 if (!item){
  res.json({"status":"Product not found"});
  return; 
 }

  const result = await getCurrentReservedStockById(+itemId);
        const reservedItem = result || 0
  if (!reservedItem || reservedItem['stock'] < 1) {
    res.json({"status":"Not enough stock available","itemId":+itemId})
   await reserveStockById(itemId, reservedItem.stock);
    return;
  }

 res.json({"status":"Reservation confirmed","itemId":+itemId})
})
