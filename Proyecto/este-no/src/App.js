import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Home from './components/Home';
import ExperimentForm from './components/ExperimentForm';
import './App.css';
import logo from './logo.png';

import ParentRecording from './components/ParentRecording';
import AIQuestions from './components/AIQuestions';
import ResolveQuestions from './components/ResolveQuestions';
import Documentation from './components/Documentation';
import Recording from './components/Recording';
/*
function App() {
  return (
    <Router>
      <Switch>
        <Route path="/" exact component={Home} />
        <Route path="/experiment-form" component={ExperimentForm} />
        <Route path="/recording" component={Recording} />
        <Route path="/ai-questions" component={AIQuestions} />
        <Route path="/resolve-questions" component={ResolveQuestions} />
        <Route path="/documentation" component={Documentation} />
      </Switch>
    </Router>
  );
}
*/

function App() {
  return (
    <div className="app-container diagonal-split">
      <div className="sidebar">
            <img src={logo} className="App-logo" alt="logo" />
      </div>    
      <div className="content">
        <Router>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/experiment-form" element={<ExperimentForm />} />
            <Route path="/recording" element={<Recording />} /> 
            <Route path="/ai-questions" element={<AIQuestions />} />
            <Route path="/resolve-questions" element={<ResolveQuestions />} />
            <Route path="/documentation" element={<Documentation />} />
          </Routes>
        </Router>
      </div>    
         
    </div>
  );
}

export default App;

