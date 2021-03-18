# graphQLSimpleTutorial
This is the code based on https://blog.sethcorker.com/how-to-create-a-react-flask-graphql-project. Just a simple example of GraphQL implementation

You will need to install all neccesary dependencies, python, ariadne, flask..

To put data into the orders we can simply use the playground and do queries:

mutation {
        orderCoffee(size: REGULAR , name: "dddd" , type: FLAT_WHITE) {
          id
          name
          type
          size
        }
}

To get orders:
query {
        orders {
          id
          name
          type
          size
        }
}
