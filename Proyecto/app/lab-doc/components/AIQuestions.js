import React from 'react';
import { View, Text, StyleSheet } from 'react-native';

const AIQuestions = () => {
  return (
    <View style={styles.container}>
      <Text>AI Questions</Text>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
});

export default AIQuestions;