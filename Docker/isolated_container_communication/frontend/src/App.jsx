import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from './assets/vite.svg'
import heroImg from './assets/hero.png'
import './App.css'

function App() {
  const callAPI=async()=>{
    const res=await fetch("http://localhost:3000");
    const data=await res.text();
    alert(data);
  }
  return (
    <>
      <div>
        <h1>React Frontend</h1>
        <button onClick={callAPI}>Call Backend</button>
      </div>
    </>
  )
}

export default App
