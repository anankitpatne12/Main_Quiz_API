# Quiz API Documentation

This documentation provides details about the Quiz API endpoints and their functionalities.

## Base URL

The base URL for all API endpoints is `http://localhost:8000/`. Replace `localhost` and `8000` with the appropriate host and port if you're running the API on a different server.

## Endpoints

### Create a Quiz

**URL**: `/quizzes/`

**Method**: `POST`

**Description**: Creates a new quiz.

**Request Body**:

```json
{
  "question": "What is the capital of France?",
  "options": [
    "London",
    "Paris",
    "Berlin",
    "Rome"
  ],
  "rightAnswer": 1,
  "startDate": "2023-06-01T09:00:00Z",
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
- Body: JSON object representing the active quiz.


### Get Specific Active Quiz by ID

**URL:** `/quizzes/active/{quiz_id}/`

**Method:** GET 

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

