import React, { useState } from 'react'
import Header from "./Header";
import MustangPage from "./MustangPage";



function App() {
  const [theme, setTheme] = useState('light')

  const appClass = theme === 'dark' ? "App dark" : "App light";

  const handleDarkModeToggle = () => {
      setTheme(theme === 'light' ? 'dark' : 'light');
    };


    return (
      <div className={appClass}>
        <header>
         <Header />
        <button onClick={handleDarkModeToggle}>
          {theme === 'light' ? 'Dark Mode' : 'Light Mode'}
          </button>
        </header>
        <MustangPage  />
        </div>
    );
  }

export default App;
