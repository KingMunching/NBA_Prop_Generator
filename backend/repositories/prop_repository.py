from models.prop_model import Prop
from schemas import PropCreate
from sqlalchemy.orm import Session

def create_prop(db: Session, prop: PropCreate):
    db_prop = Prop(**prop.model_dump())
    db.add(db_prop)
    db.commit()
    db.refresh(db_prop)
    return db_prop

def get_props_by_user(db: Session, user_id):
    return db.query(Prop).filter(Prop.user_id == user_id).all()
