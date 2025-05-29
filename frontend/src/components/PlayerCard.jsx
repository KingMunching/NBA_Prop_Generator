import React from "react";


function PlayerCard({ player }){
     if (!player) return <div className="error">Player data missing</div>;

     return (
        <div className="player-card">
      <div className="player-header">
        <h2>{player.name}</h2>
        <div className="player-id">ID: {player.id}</div>
      </div>
      
      <div className="player-details">
        <div className="detail">
          <span className="label">NBA ID:</span>
          <span className="value">{player.nba_id}</span>
        </div>
       </div>
    </div>
    );
}

export default PlayerCard;