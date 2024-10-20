import React from 'react';
import { View, Text, Button, StyleSheet } from 'react-native';

const Home = ({ navigation }) => {
  const goToExperiment = () => {
    navigation.navigate('ExperimentForm');
  };

  return (
    <View style={styles.home}>
      <Text style={styles.title}>Bienvenido a Lab.Doc</Text>
      <Button title="Start" onPress={goToExperiment} />
    </View>
  );
};

const styles = StyleSheet.create({
  home: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: 'white',
  },
  title: {
    fontSize: 24,
    marginBottom: 20,
  },
});

export default Home;