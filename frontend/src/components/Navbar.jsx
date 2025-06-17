  import React from 'react';
  import './Navbar.css';
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



  function Navbar() {
    return (
      <div className="flex w-full bg-transparent items-center text-white">
        <div className="container mx-auto px-4">
          <div className="flex items-center justify-between py-4">
      <NavigationMenu>
      <NavigationMenuList>
        
        {/* Dropdown Menu Example */}
        <NavigationMenuItem className="flex gap-4 list-none">
          <NavigationMenuTrigger className="bg-transparent">Games</NavigationMenuTrigger>
          <NavigationMenuContent>
            <div className="grid gap-3 p-6 w-[400px]">
              <NavigationMenuLink href="/games/today">
                Today's Games
              </NavigationMenuLink>
              <NavigationMenuLink href="/games/upcoming">
                Upcoming Games
              </NavigationMenuLink>
            </div>
          </NavigationMenuContent>
        </NavigationMenuItem>

        {/* Another Dropdown */}
        <NavigationMenuItem>
          <NavigationMenuTrigger className="bg-transparent">Player Props</NavigationMenuTrigger>
          <NavigationMenuContent>
            <div className="grid gap-3 p-6 w-[400px]">
              <NavigationMenuLink href="/props/points">
                Points
              </NavigationMenuLink>
              <NavigationMenuLink href="/props/rebounds">
                Rebounds
              </NavigationMenuLink>
              {/* Add more prop types */}
            </div>
          </NavigationMenuContent>
        </NavigationMenuItem>

        {/* Simple Link Example */}
        

      </NavigationMenuList>
    </NavigationMenu>
        </div>
      </div>
    </div>
    );
  }

  export default Navbar;