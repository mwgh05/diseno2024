import React from 'react';
import { View, Text, StyleSheet, ScrollView } from 'react-native';

const Documentation = ({ document }) => {
  return (
    <ScrollView contentContainerStyle={styles.container}>
      <Text style={styles.title}>Experiment Documentation</Text>
      <Text style={styles.content}>{JSON.stringify(document, null, 2)}</Text>
    </ScrollView>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 20,
    paddingTop: 50,
    backgroundColor: 'white',
  },
  title: {
    fontSize: 24,
    marginBottom: 20,
    textAlign: 'center',
  },
  content: {
    flex: 1,
    fontSize: 16,
    fontFamily: 'monospace',
    borderWidth: 1,
    borderColor: '#ccc',
    padding: 10,
  },
});

export default Documentation;