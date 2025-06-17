import React, { useEffect, useState } from "react";
import api from "../api";
import PlayerCard from "./PlayerCard";
import "./PlayerCard.css";

function KeyPlayersList({teamID}){
    const[players, setPlayers] = useState([]);
    const[loading, setLoading] = useState(true);
    const[error, setError] = useState(null);

    useEffect(()=> {
        if (!teamID) {
        setLoading(false);
        return;
        }

        const fetchPlayers = async() => {
            try{
                const response = await api.get(`/teams/${teamID}/key-players`);
                setPlayers(response.data);
                setLoading(false);
            } catch(error){
                setError("Failed to Load Key Players")
                setLoading(false);
                console.error("API Error:", err);
            }
        }
        fetchPlayers();
    }, []);
    if (loading) return <div className="loading">Loading key players...</div>;
    if (error) return <div className="error">{error}</div>;

    return (
    <div className="">
      <div className="players-grid">
        {players.length > 0 ? (
          players.map((player) => (
            <PlayerCard key={player.id} player={player} />
          ))
        ) : (
          <div>No key players found</div>
        )}
      </div>
    </div>
  );
}

export default KeyPlayersList;