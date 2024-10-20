import React, { useState, useEffect, useRef } from 'react';
import './styles/Recording.css';

const Recording = ({ onStop }) => {
  const [isRecording, setIsRecording] = useState(false);
  const [isPaused, setIsPaused] = useState(false);
  const videoRef = useRef(null);
  const streamRef = useRef(null);

  useEffect(() => {
    // Access the camera
    navigator.mediaDevices.getUserMedia({ video: true })
      .then(stream => {
        streamRef.current = stream;
        if (videoRef.current) {
          videoRef.current.srcObject = stream;
        }
      })
      .catch(err => {
        console.error('Error accessing camera: ', err);
      });

    // Cleanup function to stop the video stream
    return () => {
      if (streamRef.current) {
        streamRef.current.getTracks().forEach(track => track.stop());
      }
    };
  }, []);

  const startRecording = () => {
    setIsRecording(true);
    setIsPaused(false);
  };

  const stopRecording = () => {
    setIsRecording(false);
    setIsPaused(false);
    if (streamRef.current) {
      streamRef.current.getTracks().forEach(track => track.stop());
    }
   // onStop();
  };

  const pauseRecording = () => {
    setIsPaused(true);
    setIsRecording(false);
  };

  return (
    <div className="recording">
      <h2>{isRecording ? 'Recording...' : isPaused ? 'Recording Paused' : 'Ready to Record'}</h2>
      <video ref={videoRef} autoPlay playsInline className="camera-view"></video>
      {!isRecording  && <button onClick={startRecording}>Start Recording</button>}
      {isRecording && <button onClick={pauseRecording}>Pause Recording</button>}
      {(isRecording || isPaused) && <button onClick={stopRecording}>Finish Recording</button>}
    </div>
  );
};

export default Recording;
