import React, { useState, useRef, useEffect } from 'react';
import { View, Text, Button, StyleSheet } from 'react-native';
import { Camera, CameraType } from 'expo-camera/legacy';

const Recording = ({ navigation }) => {
  const [hasPermission, setHasPermission] = useState(null);
  const [isRecording, setIsRecording] = useState(false);
  const [isPaused, setIsPaused] = useState(false);
  const [type, setType] = useState(CameraType.back);
  const cameraRef = useRef(null);

  useEffect(() => {
    (async () => {
      const { status } = await Camera.requestCameraPermissionsAsync();
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
    navigation.navigate('AIQuestions');
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
        type={type}
      />
      <View style={styles.buttonContainer}>
        {!isRecording && <Button title="Start Recording" onPress={startRecording} />}
        {isRecording && <Button title="Pause Recording" onPress={pauseRecording} />}
        {(isRecording || isPaused) && <Button title="Finish Recording" onPress={stopRecording} />}
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  recording: {
    flex: 1,
    justifyContent: 'flex-start',
    alignItems: 'center',
    backgroundColor: 'white',
  },
  status: {
    fontSize: 18,
    marginBottom: 10,
  },
  preview: {
    justifyContent: 'flex-start',
    alignItems: 'center',
    width: '80%',
    height: '60%', 
  },
  buttonContainer: {
    position: 'relative',
    width: '100%',
    padding: 20,
    justifyContent: 'space-around',
    alignItems: 'center',
    flexDirection: 'row',
  },
});

export default Recording;