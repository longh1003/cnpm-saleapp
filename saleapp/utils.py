def count_cart(cart):
    total_quantity, total_price = 0,0

    if cart:
        for p in cart.values():
            total_quantity += p["quantity"]
            total_price += p["quantity"]*p["price"]

    return {
        "total_quantity": total_quantity,
        "total_price": total_price
    }