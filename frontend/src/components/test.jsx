// src/components/TeamDetail.jsx (create this file if it doesn't exist)
import React, { useEffect, useState } from "react";
import api from "../api"; // Assuming this is your configured axios instance

function TeamDetail({ teamId }) { // Pass teamId as a prop
  const [team, setTeam] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    if (!teamId) { // Don't fetch if no ID is provided
      setLoading(false);
      return;
    }

    const fetchTeam = async () => {
      setLoading(true);
      setError(null);
      try {
        // Use the teamId in the URL
        const response = await api.get(`/teams/${teamId}`);
        setTeam(response.data);
      } catch (err) {
        setError(err.response?.data?.detail || err.message || "Failed to fetch team details");
        console.error(`Error fetching team ${teamId}:`, err);
      } finally {
        setLoading(false);
      }
    };

    fetchTeam();
  }, [teamId]); // Re-run effect if teamId changes

  if (loading) return <p>Loading team details...</p>;
  if (error) return <p style={{ color: 'red' }}>Error: {error}</p>;
  if (!team) return <p>No team data to display. Select a team or provide a valid ID.</p>;

  return (
    <div className="team-detail">
      <h2>Team Details</h2>
      <h3>{team.name}</h3>
      <p><strong>ID:</strong> {team.id}</p>
      <p><strong>NBA ID:</strong> {team.nba_id}</p>
      {/* You can display players if your TeamResponse includes them */}
      {team.players && team.players.length > 0 && (
        <div>
          <h4>Players:</h4>
          <ul>
            {team.players.map(player => (
              <li key={player.id}>{player.name} (NBA ID: {player.nba_id})</li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

export default TeamDetail;