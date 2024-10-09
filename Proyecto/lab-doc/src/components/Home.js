import React from 'react';
import { useNavigate } from 'react-router-dom';
import './styles/Home.css';

const Home = () => {
  const navigate = useNavigate();

  const goToExperiment = () => {
    navigate('/experiment-form');
  };

  return (
    <div className="home">
      <h1>Bienvenido a Lab.Doc</h1>
      <button onClick={goToExperiment}>Start</button>
    </div>
  );
};

export default Home;

