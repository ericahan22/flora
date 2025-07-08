import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import React, { useEffect, useState } from 'react'

function App() {
  const [speciesData, setSpeciesData] = useState([])

  useEffect(() => {    // ??? 
    fetch('http://127.0.0.1:8000/top_species')
    .then(response => response.json())
    .then(data => setSpeciesData(data))
    .catch(error => console, error(error))
  }, [])

  return (
    <div>
      <h1>Top Observed Species</h1>
      <ul>
        {speciesData.map((item, index) => (
          <li key={index}>{item.scientific_name}: {item.count}</li>
        ))}
      </ul>
    </div>
  )
}

export default App
