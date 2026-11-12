from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class WorkoutBase(BaseModel):
    exercise: str
    sport: str = "Gym"
    type: str
    sets: int = 0
    reps: int = 0
    weight: float = 0
    distance: float = 0
    duration: int = 0
    notes: str = ""

class WorkoutCreate(WorkoutBase): pass
class WorkoutOut(WorkoutBase):
    id: int
    workout_date: Optional[datetime]
    class Config: from_attributes = True

class NutritionBase(BaseModel):
    food: str
    serving_size: float = 100
    calories: float = 0
    protein: float = 0
    carbs: float = 0
    fats: float = 0
    fiber: float = 0

class NutritionCreate(NutritionBase): pass
class NutritionOut(NutritionBase):
    id: int
    food_date: Optional[datetime]
    class Config: from_attributes = True

class WaterCreate(BaseModel):
    amount_ml: float
class WaterOut(WaterCreate):
    id: int
    recorded_at: Optional[datetime]
    class Config: from_attributes = True

class GoalBase(BaseModel):
    goal_name: str
    description: str = ""
    status: str = "Active"

class GoalCreate(GoalBase): pass
class GoalOut(GoalBase):
    id: int
    class Config: from_attributes = True