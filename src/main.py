import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from sqlalchemy.orm import Session
from src.manager.database.models import BASE
from src.manager.database.core import engine

BASE.metadata.create_all(bind=engine)

