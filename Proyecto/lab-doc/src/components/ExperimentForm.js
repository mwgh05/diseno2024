import React, { useState } from 'react';
import './styles/ExperimentForm.css';

const ExperimentForm = ({ onSubmit }) => {
  const [experimentData, setExperimentData] = useState({
    inventory: '',
    reagents: '',
    procedureType: '',
  });

  const handleChange = (e) => {
    setExperimentData({
      ...experimentData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit(experimentData);
  };

  return (
    <div className="experiment-form">
      <h2>Enter Experiment Details</h2>
      <form onSubmit={handleSubmit}>
        <label>Inventory:</label>
        <input type="text" name="inventory" value={experimentData.inventory} onChange={handleChange} />
        
        <label>Reagents:</label>
        <input type="text" name="reagents" value={experimentData.reagents} onChange={handleChange} />

        <label>Procedure Type:</label>
        <input type="text" name="procedureType" value={experimentData.procedureType} onChange={handleChange} />
        
        <button type="submit">Start Experiment</button>
      </form>
    </div>
  );
};

export default ExperimentForm;
