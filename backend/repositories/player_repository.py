from sqlalchemy.orm import Session
from models.player_model import Player as PlayerModel

class PlayerRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_players(self):
        return self.db.query(PlayerModel).all()

    #def get_player_by_id(self, player_id: int):
    #   return self.db.query(PlayerModel).filter(PlayerModel.nb == player_id).first()

    def get_player_by_nba_id(self, nba_id: int):
        return self.db.query(PlayerModel).filter(PlayerModel.nba_id == nba_id).first()

    def create_player(self, player: PlayerModel):
        self.db.add(player)
        self.db.commit()
        self.db.refresh(player)
        return player

    def update_player(self, player_id: int, player_data: dict):
        db_player = self.db.query(PlayerModel).filter(PlayerModel.id == player_id).first()
        if db_player:
            for key, value in player_data.items():
                setattr(db_player, key, value)
            self.db.commit()
            self.db.refresh(db_player)
        return db_player

    def delete_player(self, player_id: int):
        db_player = self.db.query(PlayerModel).filter(PlayerModel.id == player_id).first()
        if db_player:
            self.db.delete(db_player)
            self.db.commit()
        return db_player