import './App.css'
import React, { useEffect, useState } from 'react'
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet'
import 'leaflet/dist/leaflet.css'

function App() {
  const [speciesData, setSpeciesData] = useState([])

  useEffect(() => {    // ??? 
    fetch('http://flora-steel-three.vercel.app/')
    .then(res => res.json())
    .then(data => setSpeciesData(data))
  }, [])

  return (
    <div>
      <h1>Observed Species</h1>
      <MapContainer center={[43.47, -80.53]} zoom={12} style={{ height: '600px', width: '100%'}}>
        <TileLayer
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        />
        {speciesData.map((obs, idx) =>
          obs.latitude && obs.longitude ? (
            <Marker key={idx} position={[obs.latitude, obs.longitude]}>
              <Popup>
                <b>Scientific Name:</b> {obs.scientific_name}<br />
                <b>Common Name:</b> {obs.name || "N/A"}<br />
                <b>Date:</b> {obs.date || "N/A"}
              </Popup>
            </Marker>
          ) : null
        )}
      </MapContainer>
    </div>
  )
}

export default App
