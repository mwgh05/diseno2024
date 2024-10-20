import React from 'react';
import './styles/Documentation.css';

const Documentation = ({ document }) => {
  return (
    <div className="documentation">
      <h2>Experiment Documentation</h2>
      <pre>{JSON.stringify(document, null, 2)}</pre>
    </div>
  );
};

export default Documentation;
