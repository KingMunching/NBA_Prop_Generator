// src/App.jsx
// ... other imports ...
import TeamDetail from './components/test'; 
import api from './api';

function App() {
  // ... your existing state and useEffect for fetching all teams ...
  // ... handlePropsGenerated function ...

  // For testing, let's pick a team ID.
  // Make sure a team with this ID exists in your database.
  const testTeamId = 3 // Change this to an ID of an existing team in your DB

  return (
    <div className="App">
      <header>
        <h1>NBA Prop Bet Analytics</h1>
        <p><a href={`${api.defaults.baseURL}/docs`} target="_blank" rel="noopener noreferrer">API Docs</a></p>
      </header>

      <main>
        {/* ... your PropGeneratorForm and results section ... */}

        <section className="single-team-test-section">
          <h3>Test Single Team Fetch</h3>
          <TeamDetail teamId={testTeamId} />
        </section>

        {/* ... your existing teams-section for displaying all teams ... */}
      </main>
    </div>
  );
}

export default App;