from pydantic import BaseModel
from typing import List

# request body에 data가 알맞게 작성되었는지를 검증해주는 model이다.
# FastAPI에서 모델은 데이터가 어떻게 전달되고 처리돼야 하는지를 정의하는 구조화된 클래스이다.
# 모델은 pydantic의 BaseModel 클래스의 하위 클래스로 생성된다.
class Todo(BaseModel):
    id: int
    item: str

# 이렇게 pydantic 모델을 사용하지 않았다면. dict를 사용했다면, 빈 dictionary를 보내더라도 오류가 발생하지 않는다.
# 그러나 pydantic 모델을 사용한다면, 모델을 검증하여 request body 형식이 알맞지 않으면 오류메시지를 반환한다.
# 모델은 중첩하여 사용이 가능하다.

# model for request body of update route
class TodoItem(BaseModel):
    item: str
    
    class Config:
        schema_exta = {
            "example": {
            "item": "Read the next chapter of the book."
            }
        }

class TodoItems(BaseModel):
    todos: List[TodoItem]
    
    class Config:
        schema_exta = {
            "example": {
                "todos": [
                    {
                        "item": "Example schema 1!"
                    },
                    {
                        "item": "Example schema 2!"
                    }
                ]
            }
        }
