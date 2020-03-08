python manage.py generate_question_bank


Description : Quiz Listing <br>
URL : /api/v1/quiz/listing <br>
Method : GET <br>

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

Description : Question Listing based on Test/Module Id <br>
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

Description : Initiating Test
<br>
Method : POST
<br>
URL : /api/v1/quiz/initiate
<br>
Authorization Header:
```angular2
{
    "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTgzODMwMzkxLCJqdGkiOiJiOGFkZWUxNjY1YTk0MDk1ODNkYjcwNWU5ZDMwYTczZSIsInVzZXJfaWQiOjF9.VHOV_sicCdDbHBBFExi6JbbVJ-U2BI5x6AgN6zu8qgI"
}

```
You can get the token from the Login API. You need to pass the access token.

