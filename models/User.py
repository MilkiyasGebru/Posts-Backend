from database import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

class User(Base):

    __tablename__ = "user"

    email: Mapped[str] = mapped_column(primary_key=True)
    password: Mapped[str] = mapped_column()
    post: Mapped[list["Post"]] = relationship(back_populates="user")