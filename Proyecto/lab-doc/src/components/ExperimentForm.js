import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
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
    //onSubmit(experimentData);
    navigate('/recording');
  };

  const navigate = useNavigate();
/*
  const goToExperiment = () => {
    navigate('/recording');
  };
*/
  return (
    <div className="experiment-form">
      <div className='content'>
        <h2>Enter Procedure</h2>
        <form onSubmit={handleSubmit}>
          <li><label>Procedure Type:</label>
          <input type="text" name="procedureType" value={experimentData.procedureType} onChange={handleChange} /></li>
          
          <button type='submit'>Start Experiment</button>
        </form>
      </div>
    </div>
  );
};

export default ExperimentForm;
//type="submit"