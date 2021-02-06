# catalog-service [Python and Django]

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