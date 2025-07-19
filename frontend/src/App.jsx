// src/App.jsx
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom'
import { useAuth } from './components/AuthContext'
import TeamDetail from './components/test'
import PlayerCard from './components/PlayerCard'
import KeyPlayersList from './components/PlayerList'
import Navbar from './components/Navbar'
import Auth from './components/Auth'
import Today from './components/PicksToday'
import PropBetForm from './components/PropForm'
import PropDisplay from './components/PropsDisplay'
import api from './api'
import { Button } from "@/components/ui/button"
import {
  NavigationMenu,
  NavigationMenuContent,
  NavigationMenuIndicator,
  NavigationMenuItem,
  NavigationMenuLink,
  NavigationMenuList,
  NavigationMenuTrigger,
  NavigationMenuViewport,
} from "@/components/ui/navigation-menu"

function MainAppContent() {
  const testTeamId = 1
  return (
    <>
      <Navbar /> 
      {}
    </>
  )
}

function App() {
  const { user } = useAuth()

  return (
    <BrowserRouter>
      <Routes>
        <Route path="/login" element={<Auth />} />
        <Route path="/home" element={<MainAppContent />} />
        <Route path="/picks/today" element={<Today />} />
        <Route path="/props" element={<PropBetForm />} />
        <Route path="/props/results" element={<PropDisplay />} />

        <Route 
          path="/*"
          element={
            user ? <MainAppContent /> : <Navigate to="/login" />
          }
        />
      </Routes>
    </BrowserRouter>
  )
}

export default App
