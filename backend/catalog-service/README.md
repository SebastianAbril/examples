# catalog-service [Python and Django]
This project use python and Django framework with a hexagonal architecture style.

## Folder Structure
```
├── apps            --> Module for the delivery mechanism
│    ├── api        --> Django and Django Rest Framework [HTTP & JSON]
│    └── amqp       --> xxxx
├── core            --> Module for the use cases, domain and repositories
└── core_test       --> Unit tests
```

## Unit Test (CORE)
```bash
python manage.py test 
```