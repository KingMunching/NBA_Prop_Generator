import React from 'react';
import KeyPlayersList from './PlayerList'
import Navbar from './Navbar';
function Today() {
    const testTeamId = 1

    return (
        
        <div>
            <Navbar/>
            <KeyPlayersList teamID={testTeamId} />
        </div>
    )
}
export default Today

