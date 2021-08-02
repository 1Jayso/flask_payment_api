
To run the apllication make sure you are in the payment_API directory.

Use the command below to build the application
docker-compose build 
docker-compose up


Once the application has started: you can reach on localhost:5000 in postman or any http client

-------           --------
METHOD            ENDPOINT
-------           --------

[GET]            all-transactions

[GET]            balance

[POST]           pay


To send payment with the "pay" endpoint, use form fields below

card_type   -----------> [the value should be set to card]
card_number -----------> [any test card from stripe]
card_month  -----------> [any month number e.g 9]
card_year   -----------> [any year in the future e.g 2022]
card_cvc    -----------> [any three  digit number]
product_price ---------> [any amount in cent]










































    

    # card_type = request.form.get('type')
    # card_number = request.form.get('number')
    
    # card_month = request.form.get('exp_month')
    # card_year = request.form.get('exp_year')
    # card_cvc = request.form.get('cvc')
    # data = request.json
    # print(data)
    
    # card_type = "type"
    # card_number = data['number']
    # card_month = data['card']['exp_month']
    # card_year = data['card']['exp_year']
    # card_cvc = data['card']['cvc']

    
    # card_type = request.form.get('type')
    # card = request.form.get('card')
    # card_number=card['number']
    # card_month=card['exp_month']
    # card_year=card['exp_year']
    # card_cvc=card['cvc']


    # # card = request.form.get('card')
    # card_number = request.form.get('card_number')
    # card_month = request.form.get('card_month')
    # card_year = request.form.get('card_year')
    # card_cvc = request.form.get('card_cvc')
    







# import stripe
# stripe.api_key = "sk_test_51JJGstJAJEBd0WXZJ47l1Ii2k6As3ItH0rMVVCQDAlu9hAOWNlOvGPWjKYY1cff8Cqita46lGdSs50SOXYjtkKVM00xWn0CXJX"





# stripe.PaymentMethod.create(
#   type="card",
#   card={
#     "number": "4242424242424242",
#     "exp_month": 7,
#     "exp_year": 2022,
#     "cvc": "314",
#   },
# )



# @app.route ('/payment', methods=['POST'])
# def payment():
    
#     # card_type = request.form.get('type')
#     # card_number= request.form.get('number')
#     # card_exp_month = request.form.get('exp_month')
#     # card_exp_year = request.form.get('exp_month')
#     # card_cvc = request.form.get('cvc')


#     # payment =  stripe.PaymentMethod.create(
#     #     card_type, card_number, card_exp_month, card_exp_year, card_cvc
#     # )


#     payment = stripe.PaymentMethod.create(
#     type="card",
#     card={
#         "number": "4242424242424242",
#         "exp_month": 7,
#         "exp_year": 2022,
#         "cvc": "314",
#     },
#     )
#     return jsonify(message="payment has been made!"), 200

