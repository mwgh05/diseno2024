import React, { useState } from 'react';
import Recording from './Recording';

const ParentRecording = () => {
  const [isRecording, setIsRecording] = useState(false);

  const handleStop = () => {
    console.log('Recording stopped');
    setIsRecording(false);
  };

  return (
    <div>
      <h1>Camera Recording</h1>
      {isRecording ? (
        <Recording onStop={handleStop} />
      ) : (
        <button onClick={() => setIsRecording(true)}>Start Recording</button>
      )}
    </div>
  );
};

export default ParentRecording;