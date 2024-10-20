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
        
          <View style={styles.content}>
          <View style={styles.triangle} />
            <View style={styles.sidebar}>
              <Image source={logo} style={styles.logo} />
            </View>         
            <Stack.Navigator initialRouteName="Home" screenOptions={{ headerShown: false }}>
              <Stack.Screen name="Home" component={Home} />
              <Stack.Screen name="ExperimentForm" component={ExperimentForm} />
              <Stack.Screen name="Recording" component={Recording} />
              <Stack.Screen name="AIQuestions" component={AIQuestions} />
              <Stack.Screen name="ResolveQuestions" component={ResolveQuestions} />
              <Stack.Screen name="Documentation" component={Documentation} />
            </Stack.Navigator>          
            
        </View>
      </View>
    </NavigationContainer>
  );
}

const styles = StyleSheet.create({
  appContainer: {
    flex: 1,
    backgroundColor: 'white',
  },
  sidebar: {
    height: 100,
    width: 100,
    justifyContent: 'center',
    alignItems: 'flex-start',
    padding: 10,
    paddingTop: 40,
    backgroundColor: 'white',
    zIndex: 2,
  },
  logo: {
    width: 100,
    height: 100,
  },
  content: {
    position: 'relative',
    width: '100%',
    height: '100%',
    backgroundColor: 'white',
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
    borderRightWidth: width,
    borderTopWidth: 170,
    borderLeftColor: 'transparent',
    borderRightColor: 'transparent',
    borderTopColor: 'white',
    zIndex: 1,
  },
});

export default App;