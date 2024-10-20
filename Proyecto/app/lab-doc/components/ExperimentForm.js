import React, { useState } from 'react';
import { View, Text, TextInput, Button, StyleSheet } from 'react-native';

const ExperimentForm = ({ navigation }) => {
  const [experimentData, setExperimentData] = useState({
    procedureType: '',
  });

  const handleChange = (name, value) => {
    setExperimentData({
      ...experimentData,
      [name]: value,
    });
  };

  const handleSubmit = () => {
    navigation.navigate('Recording');
  };

  return (
    <View style={styles.experimentForm}>
      <View style={styles.content}>
        <Text style={styles.title}>Enter Procedure</Text>
        <View style={styles.form}>
          <Text>Procedure Type:</Text>
          <TextInput
            style={styles.input}
            value={experimentData.procedureType}
            onChangeText={(value) => handleChange('procedureType', value)}
          />
          <Button title="Start Experiment" onPress={handleSubmit} />
        </View>
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  experimentForm: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: 'white',
  },
  content: {
    width: '80%',
  },
  title: {
    fontSize: 24,
    marginBottom: 20,
    textAlign: 'center',
  },
  form: {
    alignItems: 'center',
  },
  input: {
    width: '100%',
    padding: 10,
    borderWidth: 1,
    borderColor: '#ccc',
    marginBottom: 20,
  },
});

export default ExperimentForm;