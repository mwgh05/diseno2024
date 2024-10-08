import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Home from './components/Home';
import ExperimentForm from './components/ExperimentForm';
/*
import Recording from './components/Recording';
import AIQuestions from './components/AIQuestions';
import ResolveQuestions from './components/ResolveQuestions';
import Documentation from './components/Documentation';

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
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/experiment-form" element={<ExperimentForm />} />
      </Routes>
    </Router>
  );
}

export default App;

