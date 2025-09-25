from models.prop_model import Prop
from schemas import PropCreate
from sqlalchemy.orm import Session
from sqlalchemy.dialects.postgresql import UUID


def create_prop(db: Session, prop: PropCreate, user_id: str):
    db_prop = Prop(
        user_id=user_id,
        prop_type=prop.prop_type,
        stat=prop.stat,
        threshold=prop.threshold,
        num_games=prop.num_games,
        player_name = prop.player_name,
    )
    db.add(db_prop)
    db.commit()
    db.refresh(db_prop)
    return db_prop

def get_props_by_user(db: Session, user_id):
    return db.query(Prop).filter(Prop.user_id == user_id).all()

def delete_prop(db: Session, user_id, prop_id: UUID):
    db.query(Prop).filter(Prop.id == prop_id, Prop.user_id == user_id).delete()
    db.commit()