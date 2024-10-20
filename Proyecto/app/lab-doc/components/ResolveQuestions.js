import React from 'react';
import { View, Text, TextInput, Button, StyleSheet } from 'react-native';

const ResolveQuestions = ({ question, onSubmit, navigation }) => {
  const [answer, setAnswer] = React.useState('');

  const handleSubmit = () => {
    //onSubmit(answer);
    navigation.navigate('AIQuestions');
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Resolve Question</Text>
      <Text style={styles.question}>{question}</Text>
      <TextInput
        style={styles.input}
        value={answer}
        onChangeText={setAnswer}
      />
      <Button title="Submit Answer" onPress={handleSubmit} />
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
  question: {
    fontSize: 18,
    marginBottom: 20,
    textAlign: 'center',
  },
  input: {
    width: '100%',
    padding: 10,
    borderWidth: 1,
    borderColor: '#ccc',
    marginBottom: 20,
  },
});

export default ResolveQuestions;