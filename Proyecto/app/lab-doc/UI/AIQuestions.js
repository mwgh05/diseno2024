import React from 'react';
import { View, Text, Button, StyleSheet } from 'react-native';

const AIQuestions = ({ questions = [], onResolve, navigation }) => {

  const handleResolve = (index) => {
    onResolve(index);
    navigation.navigate('ResolveQuestions');
  };

  const dummy = () => {
    navigation.navigate('ResolveQuestions');
  }
  const finish = () => {
    navigation.navigate('Documentation');
  }

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Questions from AI</Text>
      <View style={styles.content}>
        {questions.map((question, index) => (
          <View key={index} style={styles.questionContainer}>
            <Text style={styles.question}>{question}</Text>
            <Button title="Resolve" onPress={() => handleResolve(index)} />         
          </View>
        ))}
        <Button title="Resolve" onPress={dummy} />
      </View>
      <Button title="Finish" onPress={finish} />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    padding: 20,
    backgroundColor: 'white',
  },
  title: {
    fontSize: 24,
    marginBottom: 20,
  },
  questionContainer: {
    marginBottom: 20,
    alignItems: 'center',
  },
  question: {
    fontSize: 18,
    marginBottom: 10,
  },
  content: {
    fontSize: 16,
    fontFamily: 'monospace',
    borderWidth: 1,
    borderColor: '#ccc',
    padding: 10,
  },
});

export default AIQuestions;