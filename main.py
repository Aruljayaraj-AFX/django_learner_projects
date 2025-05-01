from fastapi import FastAPI
import uvicorn

app=FastAPI()

app.include_router(router,prefix="/try_works/v.1/signup", tags=["user_signup"])

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8001)