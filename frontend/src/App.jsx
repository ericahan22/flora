import './App.css'
import React, { useEffect, useState } from 'react'
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet'
import 'leaflet/dist/leaflet.css'

// Folium-like marker icon
const greenIcon = new L.Icon({
  iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-green.png',
  shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.7.1/images/marker-shadow.png',
  iconSize: [25, 41],
  iconAnchor: [12, 41],
  popupAnchor: [1, -34],
  shadowSize: [41, 41]
})

function formatDate(dateStr) {
  if (!dateStr) return "N/A";
  const iso = dateStr.replace(/_/g, ":");
  const d = new Date(iso);
  if (isNaN(d)) return dateStr;
  return d.toLocaleString(undefined, {
    year: 'numeric',
    month: 'long',
    day: 'numeric',
    hour: '2-digit',
    minute: '2-digit'
  });
}

function App() {
  const [speciesData, setSpeciesData] = useState([])

  useEffect(() => { 
    fetch('https://flora-8f34.onrender.com/api/observations/')
    .then(res => res.json())
    .then(data => setSpeciesData(data))
  }, [])

  return (
    <MapContainer center={[43.47, -80.53]} zoom={12} style={{ height: '100vh', width: '100vw' }}>
      <TileLayer
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
      />
      {speciesData.map((obs, idx) =>
        obs.latitude && obs.longitude ? (
          <Marker key={idx} position={[obs.latitude, obs.longitude]} icon={greenIcon}>
            <Popup>
              <div style={{ minWidth: 180 }}>
                <b>Scientific Name:</b> {obs.scientific_name}<br />
                <b>Common Name:</b> {obs.name || "N/A"}<br />
                <b>Date:</b> {formatDate(obs.date)}
              </div>
            </Popup>
          </Marker>
        ) : null
      )}
    </MapContainer>
  )
}

export default App
