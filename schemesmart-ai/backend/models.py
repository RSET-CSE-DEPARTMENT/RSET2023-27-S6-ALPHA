
from sqlalchemy import Column, Integer, String, Boolean, Text, ForeignKey
from sqlalchemy.orm import relationship
from backend.database import Base

from sqlalchemy import Column, Integer, String, Boolean, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from backend.database import Base




# ----------------------------
# USER TABLE
# ----------------------------
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)

    profile = relationship("UserProfile", back_populates="user", uselist=False)

    email = Column(String, unique=True, index=True)
    password_hash = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

    # ✅ ADD THIS
    bookmarks = relationship("Bookmark", back_populates="user")



# ----------------------------
# USER PROFILE TABLE
# ----------------------------
class UserProfile(Base):
    __tablename__ = "user_profiles"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))

    full_name = Column(String)
    date_of_birth = Column(String)
    gender = Column(String)
    marital_status = Column(String)
    state = Column(String)
    district = Column(String)
    education = Column(String)
    occupation = Column(String)
    annual_income = Column(String)
    category = Column(String)
    disability_status = Column(String)
    preferred_sectors = Column(String)

    landholding_size = Column(String, nullable=True)
    type_of_farming = Column(String, nullable=True)

    msme_status = Column(String, nullable=True)
    business_turnover = Column(String, nullable=True)

    single_girl_child = Column(String, nullable=True)

    user = relationship("User", back_populates="profile")


# ----------------------------
# SCHEME TABLE (UPGRADED)
# ----------------------------
class Scheme(Base):
    __tablename__ = "schemes"

    id = Column(Integer, primary_key=True, index=True)

    # Basic Info
    name = Column(String, nullable=False)
    sector = Column(String)                # Education, Agriculture, Health
    state = Column(String)                 # Kerala, All India
    category = Column(String)              # SC, ST, OBC, Minority, General
    income = Column(String)                # Below 2L, Below 2.5L
    gender = Column(String)                # Male, Female, All

    # Description
    description = Column(Text)
    eligibility_text = Column(Text)


    # Extra Details for Scheme Page
    ministry = Column(String)
    benefits = Column(Text)
    documents = Column(Text)               # Comma-separated list
    deadline = Column(String)
    official_link = Column(String)

    official_link = Column(String)

    bookmarks = relationship("Bookmark", back_populates="scheme")


class Bookmark(Base):
    __tablename__ = "bookmarks"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    scheme_id = Column(Integer, ForeignKey("schemes.id"))
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="bookmarks")
    scheme = relationship("Scheme", back_populates="bookmarks")

