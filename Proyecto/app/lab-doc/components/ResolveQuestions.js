import React from 'react';
import { View, Text, StyleSheet } from 'react-native';

const ResolveQuestions = () => {
  return (
    <View style={styles.container}>
      <Text>Resolve Questions</Text>
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

export default ResolveQuestions;