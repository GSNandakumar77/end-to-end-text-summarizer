from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from src.end_to_end_textSummarizer.pipeline.prediction_pipeline import PredictionPipeline

app = FastAPI()

class TextRequest(BaseModel):
    text: str

@app.get("/", tags=["authentication"])
async def index():
    from starlette.responses import RedirectResponse
    return RedirectResponse(url="/docs")

@app.post("/predict")
async def predict_route(request: TextRequest):
    try:
        obj = PredictionPipeline()
        result = obj.predict(request.text)
        return {"summary": result}
    except Exception as e:
        return {"error": str(e)}
from fastapi.responses import HTMLResponse
from fastapi.responses import HTMLResponse

@app.get("/test", response_class=HTMLResponse)
async def test_page():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <title>AI Text Summarizer Demo</title>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            body {
                background: #f8f9fa;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                padding: 2rem;
            }
            .container {
                max-width: 700px;
                margin: auto;
                background: white;
                padding: 2rem;
                border-radius: 0.5rem;
                box-shadow: 0 0 15px rgba(0,0,0,0.1);
            }
            textarea {
                resize: none;
            }
            #resultCard {
                margin-top: 1rem;
                display: none;
            }
            #loadingSpinner {
                display: none;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1 class="mb-4 text-center">AI Text Summarizer Demo</h1>
            <form id="textForm">
                <div class="mb-3">
                    <label for="textInput" class="form-label">Enter Text to Summarize</label>
                    <textarea id="textInput" class="form-control" rows="6" placeholder="Paste or type text here..."></textarea>
                </div>
                <button type="submit" class="btn btn-primary w-100">Summarize</button>
            </form>

            <div id="loadingSpinner" class="text-center mt-3">
                <div class="spinner-border text-primary" role="status">
                    <span class="visually-hidden">Loading...</span>
                </div>
                <p>Summarizing text, please wait...</p>
            </div>

            <div id="resultCard" class="card">
                <div class="card-header bg-primary text-white">
                    Summary Result
                </div>
                <div class="card-body">
                    <p id="summaryText" class="card-text"></p>
                </div>
            </div>
        </div>

        <script>
            const form = document.getElementById('textForm');
            const spinner = document.getElementById('loadingSpinner');
            const resultCard = document.getElementById('resultCard');
            const summaryText = document.getElementById('summaryText');

            form.onsubmit = async function(e) {
                e.preventDefault();
                resultCard.style.display = 'none';
                spinner.style.display = 'block';
                summaryText.textContent = '';

                const text = document.getElementById('textInput').value.trim();
                if (!text) {
                    spinner.style.display = 'none';
                    alert('Please enter some text to summarize.');
                    return;
                }

                try {
                    const response = await fetch('/predict', {
                        method: 'POST',
                        headers: {'Content-Type': 'application/json'},
                        body: JSON.stringify({text: text})
                    });

                    const data = await response.json();
                    spinner.style.display = 'none';

                    if (data.summary) {
                        summaryText.textContent = data.summary;
                        resultCard.style.display = 'block';
                    } else if (data.error) {
                        alert('Error: ' + data.error);
                    } else {
                        alert('Unexpected response from server.');
                    }
                } catch (error) {
                    spinner.style.display = 'none';
                    alert('Failed to summarize text: ' + error.message);
                }
            };
        </script>
    </body>
    </html>
    """

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8081)
