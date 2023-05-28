# Quiz API Documentation

This documentation provides details about the Quiz API endpoints and their functionalities.

## Base URL

The base URL for all API endpoints is `https://main-quiz.onrender.com/`. 

(Due to the initial setup and configuration process on the platform where I hosted the API, it is possible that the API may take approximately 30-40 seconds to fully load upon the first visit. Rest assured, this delay is temporary and subsequent access to the API will work seamlessly and without any noticeable delay.)

## Endpoints

### Create a Quiz

**URL**: `/quizzes/`

**Method**: `POST`

**Description**: Creates a new quiz.

**Request Body**:

```json
{
  "question": "Your_question_here",
  "options": [
    "Option_1",
    "Option_2",
    "Option_3",
    "Option_4"
  ],
  "rightAnswer": 1, <---(Index of correct option)
  "startDate": "2023-06-01T09:00:00Z", <---(June 1, 2023 - 9 a.m. | UTC time zone | Format: `YYYY-MM-DDTHH:MM:SSZ`)
  "endDate": "2023-06-01T10:00:00Z"
}
```

**Response**:
- Status Code: 201 (Created)
- Body: JSON object representing the created quiz.

### Get Active Quizzes

**URL**: `/quizzes/active/`

**Method**: `GET`

**Description**: Retrieves all the active quizzes.

**Response**:
- Status Code: 200 (OK)
- Body: JSON objects representing the active quizzes.


### Get Specific Active Quiz by ID

**URL:** `/quizzes/active/{quiz_id}/`

**Method:** `GET`

**Description:** Retrieve a specific active quiz by its ID.

**URL Parameters**:
- `quiz_id` (integer): ID of the quiz.

**Response:**
  - Status: 200 OK
  - Body: JSON representation of the active quiz.

### Get Quiz Result

**URL**: `/quizzes/{quiz_id}/result/`

**Method**: `GET`

**Description**: Retrieves the result of a quiz by its ID.

**URL Parameters**:
- `quiz_id` (integer): ID of the quiz.

**Response**:
- Status Code: 200 (OK)
- Body: JSON object representing the quiz result.

### Get All Quizzes

**URL**: `/quizzes/all/`

**Method**: `GET`

**Description**: Retrieves all quizzes.

**Response**:
- Status Code: 200 (OK)
- Body: JSON array containing objects representing all quizzes.

## Error Handling

The API handles various error scenarios and returns appropriate error responses with relevant error messages.

- Status Code: 400 (Bad Request)
- Body: JSON object with an `"error"` key containing an error message.

## Status Field

Each quiz has a `"status"` field that indicates its status.

- `"inactive"`: Before the start time of the quiz.
- `"active"`: During the time when the quiz is available.
- `"finished"`: After the end time of the quiz.

The status field is automatically updated based on the start and end time of each quiz.

---

