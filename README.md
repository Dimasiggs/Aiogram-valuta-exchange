To run the code:

docker-compose build
docker-compose up



Service for obtaining exchange rates:

Every day he receives an XML file with exchange rates from the website of the Central Bank of Russia (CBRF) using this link.
Updates data in Redis, each currency rate has its own key.

Bot service:

Responds to the /exchange command, for example: /exchange USD RUB 10 and displays the value of 10 dollars in rubles.
Responds to the /rates command, sending the user current exchange rates.
