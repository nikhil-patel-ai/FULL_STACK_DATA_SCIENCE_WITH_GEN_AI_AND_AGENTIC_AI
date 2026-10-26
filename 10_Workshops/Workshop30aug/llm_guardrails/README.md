# LLM Guardrails Project

This project demonstrates a FastAPI application that uses Gemini LLM safely with input and output guardrails.

## 1. Generate Gemini LLM API key

1. Open Google AI Studio: https://aistudio.google.com/app/apikey
2. Sign in with your Google account.
3. Click Create API key.
4. Copy the generated key.
5. Keep it secure and do not share it publicly.
6. Create a `.env` file in the project root and add:

```env
GEMINI_API_KEY=your_api_key_here
GEMINI_MODEL=gemini-2.5-flash
```

> The app reads this value from the environment using Python dotenv.

## 2. Create a virtual environment

Open the terminal in the project folder and run:

```bash
python -m venv myenv
```

Activate it on Windows:

```bash
myenv\Scripts\activate
```

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 4. Run the application

```bash
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```

Then open:

```text
http://127.0.0.1:8000
```

## 5. Project flow

1. User enters a prompt.
2. Input guardrail checks for unsafe content.
3. Gemini generates a response.
4. Output guardrail checks the response before sending it back.

## 6. Example request

```json
{
  "prompt": "Explain AI in 2 lines."
}
```

## 7. Project files

- `app.py` - FastAPI application
- `config.py` - environment configuration
- `gemini_service.py` - Gemini API call
- `guardrails.py` - input guardrail logic
- `output_guardrails.py` - output guardrail logic
- `requirements.txt` - Python dependencies
- `templates/` - frontend templates
- `static/` - frontend assets

## 8. Safety checks included

The project checks for:

- dangerous keywords
- prompt injection attempts
- jailbreak patterns
- sensitive output like API keys or passwords

## 9. Troubleshooting

If the app fails because the API key is missing:

- verify the `.env` file exists
- confirm `GEMINI_API_KEY` is spelled correctly
- restart the server after updating the environment

## 10. Summary

This project is a simple example of using LLM guardrails to make Gemini-based applications safer and more controlled.

