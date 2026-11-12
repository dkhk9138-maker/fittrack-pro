from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from database import Base

class Workout(Base):
    __tablename__ = "workouts"
    id = Column(Integer, primary_key=True, index=True)
    exercise = Column(String(150), nullable=False)
    sport = Column(String(50), default="Gym")
    type = Column(String(50), nullable=False)
    sets = Column(Integer, default=0)
    reps = Column(Integer, default=0)
    weight = Column(Float, default=0)
    distance = Column(Float, default=0)
    duration = Column(Integer, default=0)
    notes = Column(String(255), default="")
    workout_date = Column(DateTime(timezone=True), server_default=func.now())

class Nutrition(Base):
    __tablename__ = "nutrition"
    id = Column(Integer, primary_key=True, index=True)
    food = Column(String(150), nullable=False)
    serving_size = Column(Float, default=100)
    calories = Column(Float, default=0)
    protein = Column(Float, default=0)
    carbs = Column(Float, default=0)
    fats = Column(Float, default=0)
    fiber = Column(Float, default=0)
    food_date = Column(DateTime(timezone=True), server_default=func.now())

class WaterLog(Base):
    __tablename__ = "water_logs"
    id = Column(Integer, primary_key=True, index=True)
    amount_ml = Column(Float, nullable=False)
    recorded_at = Column(DateTime(timezone=True), server_default=func.now())

class Goal(Base):
    __tablename__ = "goals"
    id = Column(Integer, primary_key=True, index=True)
    goal_name = Column(String(100), nullable=False)
    description = Column(String(255), default="")
    status = Column(String(50), default="Active")