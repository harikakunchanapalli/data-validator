RULES = {
    "Order ID": {
        "required": True,
        "unique": True
    },

    "Order Date": {
        "required": True,
        "date": True
    },

    "Customer Name": {
        "required": True
    },

    "Email": {
        "required": True,
        "email": True
    },

    "Region": {
        "required": True
    },

    "Product": {
        "required": True
    },

    "Quantity": {
        "required": True,
        "numeric": True,
        "min": 1
    },

    "Unit Price": {
        "required": True,
        "numeric": True,
        "min": 0
    },

    "Status": {
        "required": True
    },

    "Order Total": {
        "required": True,
        "numeric": True
    }
}