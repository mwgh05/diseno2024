import React from 'react';
import './styles/AIQuestions.css';

const AIQuestions = ({ questions, onResolve }) => {
  return (
    <div className="ai-questions">
      <h2>Questions from AI</h2>
      {questions.map((question, index) => (
        <div key={index}>
          <p>{question}</p>
          <button onClick={() => onResolve(index)}>Resolve</button>
        </div>
      ))}
    </div>
  );
};

export default AIQuestions;
