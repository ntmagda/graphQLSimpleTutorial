from ariadne import QueryType, MutationType
from Coffee import Coffee
query = QueryType()
mutation = MutationType()
orders = []


@query.field("orders")
def resolve_orders(_, info):
    return orders

@mutation.field("orderCoffee")
def resolve_order_coffee(_, info, size, name, type):
    newOrder = Coffee(size, name, type)
    orders.append(newOrder)
    return newOrder

#############
# To put data into the orders we can simply use the playground and do queries:

# mutation {
#         orderCoffee(size: REGULAR , name: "dddd" , type: FLAT_WHITE) {
#           id
#           name
#           type
#           size
#         }
# }

# To get orders:
# query {
#         orders {
#           id
#           name
#           type
#           size
#         }
# }

