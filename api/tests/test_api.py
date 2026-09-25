from fastapi.testclient import TestClient
from main import app
client = TestClient(app)
def payload(): return {"tasks":[{"name":"Control panel wiring","minutes":42,"steps":14,"complexity":5,"environment":"shop floor"},{"name":"Motor diagnosis","minutes":35,"steps":11,"complexity":5,"environment":"plant room"}],"capture_mode":"smart-glasses","privacy_screening":True,"worker_rate_per_hour":72,"buyer_rate_per_hour":165}
def test_health(): assert client.get("/health").json()=={"status":"ok"}
def test_builds_paid_pilot_plan():
    response=client.post("/capture-plan",json=payload()); assert response.status_code==200
    body=response.json(); assert body["total_minutes"]==77; assert body["worker_payout_usd"]==92; assert body["readiness_score"]==96; assert body["recommendation"]=="Ready for a paid capture pilot"
def test_flags_privacy_and_confined_space():
    data=payload(); data["privacy_screening"]=False; data["tasks"][0]["environment"]="confined"
    assert len(client.post("/capture-plan",json=data).json()["warnings"])==2
def test_rejects_invalid_rates_and_duplicates():
    data=payload(); data["buyer_rate_per_hour"]=50; assert client.post("/capture-plan",json=data).status_code==422
    data=payload(); data["tasks"][1]["name"]="CONTROL PANEL WIRING"; assert client.post("/capture-plan",json=data).status_code==422
