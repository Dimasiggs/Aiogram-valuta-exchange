# Bot tracking currencies relative to the ruble

### To run the code:

```
docker-compose build

docker-compose up
```

### Bot service:

1. **Responds to the /exchange command, for example: /exchange USD RUB 10 and displays the value of 10 dollars in rubles.**
2. **Responds to the /rates command, sending the user current exchange rates.**

### Service for obtaining exchange rates:

1. **Every day he receives an XML file with exchange rates from the website of the Central Bank of Russia (CBRF) using this link.**
2. **Updates data in Redis, each currency rate has its own key.**

 
 
 
### Requirements
|name  |version|
|-----|-------|
|python|3.11 |
|redis|5.0.7|
|aiogram|3.10.0|
|aiohttp|3.9.5|
