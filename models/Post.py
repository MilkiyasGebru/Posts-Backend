from database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey


class Post(Base):

    __tablename__ = "post"

    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str] = mapped_column()
    email: Mapped[str] = mapped_column(ForeignKey("user.email"))
    user: Mapped["User"] = relationship(back_populates="post")
