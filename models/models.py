from sqlalchemy import Column, String
from utils.database import Base


class Config(Base):
    """
    Config model for storing configuration key-value pairs with path-based organization

    Attributes:
        path: The hierarchical path where the config belongs (e.g., 'my-local-key')
        key: The configuration key
        value: The configuration value stored as a string
    """
    __tablename__ = "config"

    # Composite primary key of path + key
    path = Column(String, primary_key=True, index=True)
    key = Column(String, primary_key=True, index=True)
    value = Column(String)

    def __repr__(self):
        return f"<Config(path='{self.path}', key='{self.key}', value='{self.value}')>"
