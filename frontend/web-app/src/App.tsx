import React from 'react';
import './App.css';
import HomeScreen from "./app/screens/HomeScreen";

function App() {
  fetch('/catalog/api/v1/brand/get_brands')
      .then(response => response.json())
      .then(data => console.log(data));

  return (
    <div className="App">
      <HomeScreen />
    </div>
  );
}

export default App;
