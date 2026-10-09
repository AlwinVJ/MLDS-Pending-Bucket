from enum import Enum
from pydantic import BaseModel, Field

# Course category for brototype students
class CourseCategory(str, Enum):
    DATA_SCIENCE = 'data_science'
    MACHINE_LEARNING = 'machine_learning'
    
# Creating pending topics for each modules
class TopicCreate(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    description: str = Field(min_length=1)
    module: int = Field(ge=1)
    category: CourseCategory
    hashtags: list[str] = Field(default_factory=list)


class TopicResponse(BaseModel):
    id: int
    title: str
    description: str
    module: int
    category: CourseCategory
    hashtags: list[str]