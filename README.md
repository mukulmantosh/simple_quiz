python manage.py generate_question_bank


Quiz Listing
URL : /api/v1/quiz/listing
```
{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 5,
            "test_name": "Python Quiz - 5VykRcaLK1Ob"
        },
        {
            "id": 6,
            "test_name": "General Quiz - EaYKXaVFBhpG"
        }
    ]
}
```

Question Listing based on Test/Module Id
<br>
URL : /api/v1/quiz/questions?module_id={id}

```
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 4,
            "question": "Who developed Python ?",
            "options": [
                {
                    "id": 13,
                    "option": "James Gosling"
                },
                {
                    "id": 14,
                    "option": "Guido van Rossum"
                },
                {
                    "id": 15,
                    "option": "Bill Gates"
                },
                {
                    "id": 16,
                    "option": "Larry Page"
                }
            ]
        }
    ]
}
```
