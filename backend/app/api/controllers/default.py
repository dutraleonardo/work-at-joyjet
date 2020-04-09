def delivery_price(cart_total, fees):

    return next(
        total
        for min_price, max_price, total in fees
        if cart_total >= min_price and
        (max_price is None or cart_total < max_price)
    )


def insert_discount(price, discount):

    if discount['type'] == 'percentage':
        percentage = 1 - discount['value'] / 100
        result = price * percentage
        return int(result)

    elif discount['type'] == 'amount':
        result = price - discount['value']
        return result
    else:
        return "Invalid Type"


def calculate_total(items, articles, discounts=None):

    final_price = 0

    for item in items:
        article_id = item['article_id']
        article = articles[article_id]
        article_price = article['price']
        quantity = item['quantity']

        if discounts is not None:
            discount = discounts.get(
                article_id, {'type': 'amount', 'value': 0}
                )
            article_price = insert_discount(article_price, discount)

        final_price += article_price * quantity

    return final_price
