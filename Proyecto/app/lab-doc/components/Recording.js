import React, { useState, useRef, useEffect } from 'react';
import { View, Text, Button, StyleSheet, Animated, Easing, Dimensions } from 'react-native';
import { Camera, CameraType } from 'expo-camera/legacy';

const Recording = ({ navigation }) => {
  const [hasPermission, setHasPermission] = useState(null);
  const [isRecording, setIsRecording] = useState(false);
  const [isPaused, setIsPaused] = useState(false);
  const [type, setType] = useState(CameraType.back);
  const { width, height } = Dimensions.get('window');
  const cameraRef = useRef(null);
  const lineAnimation = useRef(new Animated.Value(0)).current;

  useEffect(() => {
    (async () => {
      const { status } = await Camera.requestCameraPermissionsAsync();
      setHasPermission(status === 'granted');
    })();
  }, []);

  useEffect(() => {
    if (isRecording) {
      startLineAnimation();
    } else {
      lineAnimation.setValue(0);
    }
  }, [isRecording]);

  const startLineAnimation = () => {
    Animated.loop(
      Animated.sequence([
        Animated.timing(lineAnimation, {
          toValue: 1,
          duration: 2000,
          easing: Easing.linear,
          useNativeDriver: true,
        }),
        Animated.timing(lineAnimation, {
          toValue: 0,
          duration: 2000,
          easing: Easing.linear,
          useNativeDriver: true,
        }),
      ])
    ).start();
  };

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

  const lineTranslateX = lineAnimation.interpolate({
    inputRange: [0, 1],
    outputRange: [0, width * 0.8], // Adjust to match the width of the camera view
  });

  return (
    <View style={styles.recording}>
      <Text style={styles.status}>
        {isRecording ? 'Recording...' : isPaused ? 'Recording Paused' : 'Ready to Record'}
      </Text>
      <View style={styles.cameraContainer}>
        <Camera
          ref={cameraRef}
          style={styles.preview}
          type={type}
        />
        {isRecording && (
          <Animated.View
            style={[
              styles.scannerLine,
              { transform: [{ translateX: lineTranslateX }] },
            ]}
          />
        )}
      </View>
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
  cameraContainer: {
    position: 'relative',
    width: '80%',
    height: '60%',
  },
  preview: {
    flex: 1,
  },
  buttonContainer: {
    position: 'relative',
    width: '100%',
    padding: 20,
    justifyContent: 'space-around',
    alignItems: 'center',
    flexDirection: 'row',
  },
  scannerLine: {
    position: 'absolute',
    top: 0,
    bottom: 0,
    width: 2,
    backgroundColor: 'green',
  },
});

export default Recording;