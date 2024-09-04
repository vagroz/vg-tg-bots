from common import global_var
from fastapi import APIRouter

test_router = APIRouter()

@test_router.get("/test")
async def get_var():
    return "Counter is: %d" % global_var

@test_router.get("/test/inc")
async def inc(i = 1):
    global global_var
    global_var += 1
    return
