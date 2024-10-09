import React, { useState } from 'react';
import './styles/Recording.css';

const Recording = ({ onStop }) => {
  const [isRecording, setIsRecording] = useState(true);

  const stopRecording = () => {
    setIsRecording(false);
    onStop();
  };

  return (
    <div className="recording">
      <h2>{isRecording ? 'Recording...' : 'Recording Stopped'}</h2>
      <button onClick={stopRecording}>Stop Recording</button>
    </div>
  );
};

export default Recording;
