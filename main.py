from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

class Memo(BaseModel):
    id:str
    content:str

memos = []

app = FastAPI()

@app.post("/memos")
def createMemo(memo:Memo):
    memos.append(memo)
    return "메모 추가에 성공했습니다"

@app.get("/memos")
def readMemo():
    return memos

@app.put("/memos/{memo_id}")
def putMemo(req_memo:Memo):
    for memo in memos:
        if memo.id == req_memo.id:
            memo.content = req_memo.content;
            return "성공했습니다"
    return "메모는 없습니다"

@app.delete("/memos/{memo_id}")
def deletMemo(memo_id):
    for index, memo in enumerate(memos):
        if memo.id == memo_id:
            memos.pop(index)
            return "성공했습니다"
    return "메모는 없습니다"
    
    
app.mount("/", StaticFiles(directory = "static", html = True), name = "static")