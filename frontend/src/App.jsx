// src/App.jsx
// ... other imports ...
import TeamDetail from './components/test'; 
import PlayerCard from './components/PlayerCard';
import KeyPlayersList from './components/PlayerList';
import Navbar from './components/Navbar';
import api from './api';


function App() {
  // ... your existing state and useEffect for fetching all teams ...
  // ... handlePropsGenerated function ...

  // For testing, let's pick a team ID.
  // Make sure a team with this ID exists in your database.
  const testTeamId = 1 // Change this to an ID of an existing team in your DB
  const testPlayerId = 111

  return (
    <div className="App">
      <Navbar />
      <header>
      </header>

      <main>
        {/* ... your PropGeneratorForm and results section ... */}

        <section className="single-team-test-section">
         <KeyPlayersList teamID={testTeamId} />
        </section>

        {/* ... your existing teams-section for displaying all teams ... */}
      </main>
    </div>
  );
}

export default App;