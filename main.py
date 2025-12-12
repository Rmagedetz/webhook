from fastapi import FastAPI, Request

app = FastAPI()


@app.post("/tilda-webhook")
async def tilda_webhook(request: Request):
    try:
        form_data = await request.form()
        data = dict(form_data)
        print("Получены данные формы (form-data):", data)
        return {"status": "ok", "source": "form"}
    except Exception:
        json_data = await request.json()
        print("Получены данные формы (JSON):", json_data)
        return {"status": "ok", "source": "json"}