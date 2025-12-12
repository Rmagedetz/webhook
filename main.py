from fastapi import FastAPI, Request
from datetime import datetime
import sql

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
        sql.Ankets.add_object(
            email=json_data['email'],
            name=json_data['name'],
            child_birthday=datetime.strptime(json_data['dob'], '%d.%m.%Y'),
            parent_main_name=json_data['custom_roditel'],
            phone_add=json_data['custom_dopolnitelnyytelefon_2'],
            addr=json_data['custom_adresprozhivaniya'],
            disease=json_data['custom_disease'],
            allergy=json_data['custom_allergy'],
            other=json_data['custom_other'],
            physic=json_data['custom_physical'],
            swimm=json_data['custom_swimming'],
            jacket_swimm=json_data['custom_jacket_swimm'],
            school=json_data['school'],
            additional_info=json_data['custom_dop'],
            referer=json_data['custom_gorodok'],
            ok=json_data['ok_2'],
            mailing=json_data['rassylka'],
            personal_accept=json_data['personal-data'],
            oms=json_data['custom_polis']
        )
        return {"status": "ok", "source": "json"}