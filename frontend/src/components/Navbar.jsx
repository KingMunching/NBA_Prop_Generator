import React from 'react';
import { Trophy, Bell, User } from 'lucide-react';
import { Button } from "@/components/ui/button";
import { Link } from 'react-router-dom';

import {
  NavigationMenu,
  NavigationMenuContent,
  NavigationMenuItem,
  NavigationMenuLink,
  NavigationMenuList,
  NavigationMenuTrigger,
} from "@/components/ui/navigation-menu";

function Navbar() {
  return (
    <nav className="bg-gradient-to-r from-slate-900 to-slate-700">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between h-16">
          {/* Logo */}
          <div className="flex items-center space-x-2">
            <img 
              src="/proplogo.png" 
              alt="PropBets AI Logo" 
              className="h-8 w-8 object-contain"
            />
            <span className="text-white text-xl font-bold">NBA Props </span>
          </div>

          {/* Navigation Links */}
          <NavigationMenu className="hidden md:flex">
            <NavigationMenuList className="flex space-x-1">
              <NavigationMenuItem>
                <Link to="/home">
                <NavigationMenuLink 
                  className="text-white hover:text-blue-400 px-3 py-2 rounded-md text-sm font-medium transition-colors"
                >
                  Home
                </NavigationMenuLink>
                </Link>
              </NavigationMenuItem>

              <NavigationMenuItem>
                <NavigationMenuTrigger className="text-white hover:text-blue-400 bg-transparent hover:bg-slate-800 data-[state=open]:bg-slate-800">
                  Picks
                </NavigationMenuTrigger>
                <NavigationMenuContent>
                  <div className="grid gap-3 p-6 w-[400px] bg-slate-800 border border-slate-700">
                    <NavigationMenuLink 
                      href="/picks/today"
                      className="text-white hover:text-blue-400 block px-3 py-2 rounded-md text-sm hover:bg-slate-700 transition-colors"
                    >
                      Today's Picks
                    </NavigationMenuLink>
                    <NavigationMenuLink 
                      href="/picks/upcoming"
                      className="text-white hover:text-blue-400 block px-3 py-2 rounded-md text-sm hover:bg-slate-700 transition-colors"
                    >
                      Upcoming Games
                    </NavigationMenuLink>
                    <NavigationMenuLink 
                      href="/picks/favorites"
                      className="text-white hover:text-blue-400 block px-3 py-2 rounded-md text-sm hover:bg-slate-700 transition-colors"
                    >
                      My Favorites
                    </NavigationMenuLink>
                  </div>
                </NavigationMenuContent>
              </NavigationMenuItem>

              <NavigationMenuItem>
                <NavigationMenuLink 
                  href="/leaderboard"
                  className="text-white hover:text-blue-400 px-3 py-2 rounded-md text-sm font-medium transition-colors"
                >
                  Leaderboard
                </NavigationMenuLink>
              </NavigationMenuItem>

              <NavigationMenuItem>
                <NavigationMenuLink 
                  href="/stats"
                  className="text-white hover:text-blue-400 px-3 py-2 rounded-md text-sm font-medium transition-colors"
                >
                  Stats
                </NavigationMenuLink>
              </NavigationMenuItem>

              <NavigationMenuItem>
                <NavigationMenuTrigger className="text-white hover:text-blue-400 bg-transparent hover:bg-slate-800 data-[state=open]:bg-slate-800">
                  Tools
                </NavigationMenuTrigger>
                <NavigationMenuContent>
                  <div className="grid gap-3 p-6 w-[400px] bg-slate-800 border border-slate-700">
                    <NavigationMenuLink 
                      href="/tools/calculator"
                      className="text-white hover:text-blue-400 block px-3 py-2 rounded-md text-sm hover:bg-slate-700 transition-colors"
                    >
                      Odds Calculator
                    </NavigationMenuLink>
                    <NavigationMenuLink 
                      href="/tools/analytics"
                      className="text-white hover:text-blue-400 block px-3 py-2 rounded-md text-sm hover:bg-slate-700 transition-colors"
                    >
                      Player Analytics
                    </NavigationMenuLink>
                    <NavigationMenuLink 
                      href="/tools/trends"
                      className="text-white hover:text-blue-400 block px-3 py-2 rounded-md text-sm hover:bg-slate-700 transition-colors"
                    >
                      Trend Analysis
                    </NavigationMenuLink>
                  </div>
                </NavigationMenuContent>
              </NavigationMenuItem>
            </NavigationMenuList>
          </NavigationMenu>

          {/* Right side - Notifications and Profile */}
          <div className="flex items-center space-x-4">
            <Button 
              variant="ghost" 
              size="icon"
              className="text-white hover:text-blue-400 hover:bg-slate-800"
            >
              <Bell className="h-5 w-5" />
            </Button>
            
            <div className="flex items-center space-x-2">
              <div className="w-8 h-8 bg-orange-500 rounded-full flex items-center justify-center">
                <User className="h-5 w-5 text-white" />
              </div>
            </div>
          </div>

          {/* Mobile menu button */}
          <div className="md:hidden">
            <Button 
              variant="ghost" 
              size="icon"
              className="text-white hover:text-blue-400 hover:bg-slate-800"
            >
              <svg className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 6h16M4 12h16M4 18h16" />
              </svg>
            </Button>
          </div>
        </div>
      </div>

      {/* Mobile Navigation Menu */}
      <div className="md:hidden bg-slate-800 border-t border-slate-700">
        <div className="px-2 pt-2 pb-3 space-y-1">
          <a href="/" className="text-white hover:text-blue-400 block px-3 py-2 rounded-md text-base font-medium">
            Home
          </a>
          <a href="/picks" className="text-white hover:text-blue-400 block px-3 py-2 rounded-md text-base font-medium">
            Picks
          </a>
          <a href="/leaderboard" className="text-white hover:text-blue-400 block px-3 py-2 rounded-md text-base font-medium">
            Leaderboard
          </a>
          <a href="/stats" className="text-white hover:text-blue-400 block px-3 py-2 rounded-md text-base font-medium">
            Stats
          </a>
          <a href="/tools" className="text-white hover:text-blue-400 block px-3 py-2 rounded-md text-base font-medium">
            Tools
          </a>
        </div>
      </div>
    </nav>
  );
}

export default Navbar;