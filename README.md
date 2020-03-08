### Generate Dummy Questions

```
python manage.py generate_question_bank
```

## API Informations

Description : <b>Quiz Listing</b> <br>
URL : /api/v1/quiz/listing <br>
Authorization Required : No <br>
Request Method : GET <br>
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

Description : <b>Question Listing based on Test/Module Id</b> <br>
URL : /api/v1/quiz/questions?module_id={id} <br>
Authorization Required : No <br>
Request Method : GET <br>

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

Description : <b> Initiating Test </b><br>
URL : /api/v1/quiz/initiate <br> 
Authorization Required : No
Request Method : POST <br>

Authorization Header:
```
{
    "Authorization": "Bearer <token>"
}
```
You can get the token from the Login API. You need to pass the <b>access token</b>.

<br><br>

Description : <b>Saving Test Results</b> <br>
Method : POST <br>
URL : /api/v1/quiz/save <br>
Authorization Required : Yes <br>

Sample Request Body
```
{
  "test_information_id" : 1,
  "option_id": 14,
  "question_id": 1
}
```
<br>
Sample Response
<br>

```
{
    "status": true,
    "message": "Saved User Input !",
    "data": null
}
```
<br>

Description : <b>User Test Results Information API</b> <br>
Method : GET <br>
URL : /api/v1/quiz/results <br>
Authorization Required : Yes <br>

Sample Response
<br>

```
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "module": {
                "id": 5,
                "created_at": "2020-03-08T08:15:10.268252Z",
                "updated_at": "2020-03-08T08:15:10.268252Z",
                "test_name": "Python Quiz - 5VykRcaLK1Ob"
            },
            "total_questions": 1,
            "total_right_answers": 1
        }
    ]
}
```