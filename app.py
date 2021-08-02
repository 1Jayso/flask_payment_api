from flask import Flask, json, jsonify, request
from stripe.api_resources import balance, card, payment_method
import stripe
from flask import Flask, jsonify



app = Flask(__name__)

stripe_keys = {
    "secret_key": "sk_test_51JJGstJAJEBd0WXZJ47l1Ii2\
        k6As3ItH0rMVVCQDAlu9hAOWNlOvGPWjKYY1cff8Cq\
            ita46lGdSs50SOXYjtkKVM00xWn0CXJX",

    "publishable_key": "pk_test_51JJGstJAJEBd0WXZ0s1TeY\
        STGddYeIoYsE1PIqa6A6zLNdYhB1viEcwFx0LmGsxQCjL5\
            sNZOE1LETMffxEtnIFTm00LqplSfIZ",

    "endpoint_secret": "whsec_ZzDsvjPXIrtbHG09iMjLYGqav6JGwQFM",
}

stripe.api_key = stripe_keys["secret_key"]



@app.route('/pay', methods=['POST'])
def create_payment_method():
    request_data = request.get_data()
    print("This is the request data: ", request_data)
    card_type = request.form.get('card_type')
    print("Card type is : ", card_type)
    card_number = request.form.get('card_number') 
    card_month = request.form.get('card_month')
    card_year = request.form.get('card_year')
    card_cvc = request.form.get('card_cvc')
    card_mth = str(card_month)
    card_yr = str(card_year)
    price = request.form.get('product_price')

    try:
        pay = stripe.PaymentMethod.create(
            type=card_type,
            card={
                "number": card_number,
                "exp_month": card_mth,
                "exp_year": card_yr,
                "cvc": card_cvc,
                },
        )
        print(f" Payment data: {pay}")
        create_payment_intent(price)
        return jsonify("Payment has been made!", {'id': pay.id}), 200
    except Exception as e:
        return jsonify(error=str(e)), 401



# @app.route('/payment-intent', methods=['POST'])
def create_payment_intent(price):
    intent = stripe.PaymentIntent.create(
            amount=price,
            currency="usd",
            payment_method_types=["card"],
            payment_method="pm_card_visa",
            )
    try:
        intent
        return jsonify("Payment intent has been created!", {'id': intent.id}), 200
    except Exception as e:
        return jsonify(error=str(e)), 401

    # finally:
    #     confirm = stripe.PaymentIntent.confirm(
    #     intent.id,
    #     payment_method="pm_card_visa",
    # )

    #     return jsonify("Payment confirmed, check stripe dashboard", {"id": confirm}), 200








@app.route('/all-transactions', methods=['GET'])
def get_all_transactions():

    try:
        stripe.api_key = stripe_keys["secret_key"]

        list_of_transaction=stripe.PaymentIntent.list(limit=3)

        # print("The lsit of transaction: ", list_of_transaction.data[2] )
        
    
        return jsonify("The list of all transaction are as follows", {'object': list_of_transaction}), 200

    except Exception as e:
        return jsonify(error=str(e)), 401



@app.route('/balance', methods=['GET'])
def get_balance():

    try:
        stripe.api_key = stripe_keys["secret_key"]

        balance=stripe.Balance.retrieve()

        # print("The lsit of transaction: ", list_of_transaction)
    
        return jsonify("Your balance is as follows ", {'balance': balance}), 200

    except Exception as e:
        return jsonify(error=str(e)), 401





@app.route("/webhook", methods=["POST"])
def stripe_webhook():
    payload = request.get_data(as_text=True)
    sig_header = request.headers.get("Stripe-Signature")
    print(sig_header)

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, stripe_keys["endpoint_secret"]

        )

        print(event)

    except ValueError as e:
        # Invalid payload
        return "Invalid payload", 400
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return "Invalid signature", 400

    event_dict = event.to_dict()
    if event_dict['type'] == "payment_intent.created":
        intent = event_dict['data']['object']
        confirm = stripe.PaymentIntent.confirm(
        intent.id,
        payment_method="pm_card_visa",
    )
        print ("Payment successful: ", confirm.id)


        # Fulfill the customer's purchase
    elif event_dict['type'] == "payment_intent.payment_failed":
        intent = event_dict['data']['object']
        error_message = intent['last_payment_error']['message']\
             if intent.get('last_payment_error') else None
        print("Failed: ", intent['id'], error_message)
        # Notify the customer that payment failed
    return jsonify("success"), 200




if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=False)



























    # print("Card cvc is : ", card_cvc)
    # card_num = f"'{card_number}'"
    # type_of_card = f"'{card_type}'"
    
    # print(f"X{type_of_card}X")
    # cvc = f'"{card_cvc}"'
    # print("This is the card number: ", card_num)
    # print()
    # print("This is the card type: ", type_of_card)
    # print()
    # print("This is the cvc: ", cvc)
    




# stripe.api_key = 'sk_test_51HYxoFFsExQBHc34bCJ9S2nLHBoO4QV90VhJ5Sil58EQAzL1D4HMOI01ti7taoiAubyA0cunR0Aw3shFe0AN1Mh500gEbusnhI'
# app = Flask(__name__,
#             static_url_path='',
#             static_folder='.')
# CORS(app)


# app.config["DEBUG"] = True

# YOUR_DOMAIN = 'http://localhost:3000/'


# @app.route('/create-checkout-session', methods=['POST'])
# def create_checkout_session():
#     try:
#         checkout_session = stripe.checkout.Session.create(
#             payment_method_types=['card'],
#             line_items=[
#                 {
#                     'price_data': {
#                         'currency': 'usd',
#                         'unit_amount': 2000,
#                         'product_data': {
#                             'name': 'Massage Therapy Session',
#                             'images': ['https://www.msccollege.edu/wp-content/uploads/2019/05/how-long-to-become-a-massage-therapist.jpg'],
#                         },
#                     },
#                     'quantity': 1,
#                 },
#             ],
#             mode='payment',
#             success_url=YOUR_DOMAIN + 'rewards',
#             cancel_url=YOUR_DOMAIN + 'appointment',
#         )
#         return jsonify({'id': checkout_session.id})
#     except Exception as e:
#         return jsonify(error=str(e)), 403
# if __name__ == '__main__':
#     app.run(port=4242)




    # type="card",
            # card={
            #     "number": "4242424242424242",
            #     "exp_month": 8,
            #     "exp_year": 2022,
            #     "cvc": "314",
            #     },
        # )






  