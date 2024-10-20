import React, { useState, useRef } from 'react';
import { View, Text, Button, StyleSheet } from 'react-native';
import { Camera } from 'expo-camera';

const Recording = ({ navigation }) => {
  const [hasPermission, setHasPermission] = useState(null);
  const [isRecording, setIsRecording] = useState(false);
  const [isPaused, setIsPaused] = useState(false);
  const cameraRef = useRef(null);

  React.useEffect(() => {
    (async () => {
      const { status } = await Camera.requestPermissionsAsync();
      setHasPermission(status === 'granted');
    })();
  }, []);

  const startRecording = async () => {
    if (cameraRef.current) {
      setIsRecording(true);
      setIsPaused(false);
      const video = await cameraRef.current.recordAsync();
      console.log('Video saved to: ', video.uri);
    }
  };

  const stopRecording = () => {
    if (cameraRef.current && isRecording) {
      cameraRef.current.stopRecording();
      setIsRecording(false);
      setIsPaused(false);
    }
  };

  const pauseRecording = () => {
    setIsPaused(true);
    setIsRecording(false);
  };

  if (hasPermission === null) {
    return <View />;
  }
  if (hasPermission === false) {
    return <Text>No access to camera</Text>;
  }

  return (
    <View style={styles.recording}>
      <Text style={styles.status}>
        {isRecording ? 'Recording...' : isPaused ? 'Recording Paused' : 'Ready to Record'}
      </Text>
      <Camera
        ref={cameraRef}
        style={styles.preview}
        type={Camera.Constants.Type.back}
      />
      {!isRecording && <Button title="Start Recording" onPress={startRecording} />}
      {isRecording && <Button title="Pause Recording" onPress={pauseRecording} />}
      {(isRecording || isPaused) && <Button title="Finish Recording" onPress={stopRecording} />}
    </View>
  );
};

const styles = StyleSheet.create({
  recording: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  status: {
    fontSize: 18,
    marginBottom: 10,
  },
  preview: {
    flex: 1,
    justifyContent: 'flex-end',
    alignItems: 'center',
    width: '100%',
    height: '100%',
  },
});

export default Recording;