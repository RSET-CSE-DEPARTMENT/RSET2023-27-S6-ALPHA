from pydantic import BaseModel

class UserCreate(BaseModel):
    email: str
    password: str


class SchemeCreate(BaseModel):
    name: str
    sector: str
    description: str
    eligibility_text: str
    official_link: str
