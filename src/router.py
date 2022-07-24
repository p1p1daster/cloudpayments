from src.handler import charge_payment_handler as handler

post_api_charge_rout = ("/api/charge/", handler)

endpoint_url = "payments/cards/charge"
