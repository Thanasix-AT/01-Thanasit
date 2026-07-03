def process_payment(wallet_balance, item_price):

    if wallet_balance >= item_price:
        wallet_balance -= item_price
        print("Payment Successful")
        print("Remaining Balance:", wallet_balance)
        return wallet_balance
    else:
        print("Error: Insufficient Balance")
        return wallet_balance

def display_active_queues(queue_list):

    print("\nPending Queues")

    for queue in queue_list:
        if queue["status"] == "Pending":
            print(
                "Queue:",
                queue["queue_id"],
                "| Menu:",
                queue["menu"],
                "| Price:",
                queue["price"]
            )

wallet = 100
price = 50

wallet = process_payment(wallet, price)

orders = [
    {
        "queue_id": 101,
        "menu": "Fried Rice",
        "price": 50,
        "status": "Pending"
    },
    {
        "queue_id": 102,
        "menu": "Noodle Soup",
        "price": 60,
        "status": "Ready"
    },
    {
        "queue_id": 103,
        "menu": "Iced Coffee",
        "price": 40,
        "status": "Pending"
    }
]

display_active_queues(orders)