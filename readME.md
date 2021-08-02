
**This is a Flask payment microservice built with stripe Payment gateway API integration**

*To run the apllication with docker-compose make sure you are in the flask_payment_api directory.*

Use the following commands to build and start the payment_api container

```[docker-compose build] ```

```[docker-compose up]```


Once the application has started: you can reach on localhost:5000 in postman or any http client

-------------------------------------
|METHOD           |ENDPOINT         |
|-----------------|-----------------|
|                 |                 |
|[GET]            |all-transactions |
|                 |                 |
|[GET]            |balance          |
|                 |                 |
|[POST]           |pay              |
-------------------------------------

*To send payment with the "pay" endpoint, use the form fields below as a guide*
--------------------------------------------------------
|   Field            | Value                           |
|------------------- |---------------------------------|
|card_type           |[the value should be set to card]|
|card_number         |[any test card from stripe]      |
|card_month          |[any month number e.g 9]         |
|card_year           |[any year in the future e.g 2022]|
|card_cvc            |[any three  digit number]        |
|product_price       |[any amount in cent]             |
--------------------------------------------------------

