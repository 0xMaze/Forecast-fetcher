from pydantic import BaseModel


# Shared properties
class CityBase(BaseModel):
    name: str
    web_id: int


# Properties to receive on item creation
class CityCreate(CityBase):
    pass


# Properties shared by models stored in DB
class CityInDBBase(CityBase):
    id: int

    class Config:
        orm_mode = True


# Properties to return to client
class City(CityInDBBase):
    pass
