import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import Home from './components/Home';
import ExperimentForm from './components/ExperimentForm';
import Recording from './components/Recording';
import AIQuestions from './components/AIQuestions';
import ResolveQuestions from './components/ResolveQuestions';
import Documentation from './components/Documentation';
import { Image, View, StyleSheet, Dimensions } from 'react-native';
import logo from './assets/logo.png';

const Stack = createNativeStackNavigator();
const { width, height } = Dimensions.get('window');

function App() {
  return (
    <NavigationContainer>
      <View style={styles.appContainer}>
        <View style={styles.sidebar}>
          <Image source={logo} style={styles.logo} />
        </View>
        <View style={styles.content}>
          
            <Stack.Navigator initialRouteName="Home" screenOptions={{ headerShown: false }}>
              <Stack.Screen name="Home" component={Home} />
              <Stack.Screen name="ExperimentForm" component={ExperimentForm} />
              <Stack.Screen name="Recording" component={Recording} />
              <Stack.Screen name="AIQuestions" component={AIQuestions} />
              <Stack.Screen name="ResolveQuestions" component={ResolveQuestions} />
              <Stack.Screen name="Documentation" component={Documentation} />
            </Stack.Navigator>
            <View style={[styles.triangle]} />
          
        </View>
      </View>
    </NavigationContainer>
  );
}

const styles = StyleSheet.create({
  appContainer: {
    flex: 1,
    flexDirection: 'row',
    backgroundColor: 'white',
    justifyContent: 'center'
  },
  sidebar: {
    height: '15%',
    justifyContent: 'center',
    alignItems: 'flex-start',
    padding: 10,
    backgroundColor: '#f0f0f0',
  },
  logo: {
    width: 100,
    height: 100,
  },
  content: {
    flex: 1,
    position: 'relative',
    backgroundColor: 'white',
  },
  diagonalSplit: {
    ...StyleSheet.absoluteFillObject,
    zIndex: 1,
  },
  topLeft: {
    width: width * 2,
    height: height * 2,
    backgroundColor: 'white',
    transform: [{ rotate: '-45deg' }],
    position: 'absolute',
    top: -height,
    left: -width,
  },
  bottomRight: {
    width: width * 2,
    height: height * 2,
    backgroundColor: '#72a1cb',
    transform: [{ rotate: '-45deg' }],
    position: 'absolute',
    bottom: -height,
    right: -width,
  },
  navigatorContainer: {
    flex: 1,
    zIndex: 2,
  },
  triangle: {
    position: 'absolute',
    right: 0,
    bottom: 0,
    width: 0,
    height: 0,
    backgroundColor: 'blue',
    borderStyle: 'solid',
    borderLeftWidth: 0,
    borderRightWidth: Dimensions.get('window').width,
    borderTopWidth: 100,
    borderLeftColor: 'transparent',
    borderRightColor: 'transparent',
    borderTopColor: '#fff',
  },
});

export default App;